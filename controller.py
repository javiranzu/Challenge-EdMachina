from markupsafe import re
import pymysql
import json

table_schematic = 'CREATE TABLE IF NOT EXISTS `challenge`.`leads` ( `id` INT NOT NULL AUTO_INCREMENT , `nombre` VARCHAR(200) NOT NULL , `email` VARCHAR(200) NOT NULL , `direccion` VARCHAR(200) NOT NULL , `telefono` VARCHAR(30) NOT NULL , `materia` VARCHAR(80) NOT NULL , `tiempo_cursado` INT NOT NULL , `carrera` VARCHAR(80) NOT NULL , `anio_inscripcion` VARCHAR(4) NOT NULL , `veces_cursado` INT NOT NULL , PRIMARY KEY (`id`));'


def create_connection():
    return pymysql.connect(host='localhost',port=3306, user='root', password='', db='Challenge', cursorclass=pymysql.cursors.DictCursor)

def check_database():
    connection = pymysql.connect(host='localhost',port=3306, user='root', password='', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor() 

    try:
        cursor.execute('CREATE DATABASE IF NOT EXISTS `challenge`')
    except Exception as msg:
            connection.rollback()
    finally:
        connection.close()

    

def check_tables():
    connection = create_connection()
    cursor = connection.cursor()  

    fd = open('challenge.sql', 'r',encoding='utf-8')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
 
    for command in sqlCommands:
        try:
            cursor.execute(command)
        except Exception as msg:
            connection.rollback()
    cursor.close()


def listLeads():

    connection = create_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `leads`;")
        results = cursor.fetchall()
        response = []
        #Primero pido los datos personales
        for row in results:
            row = json.loads(json.dumps(row))

            #Luego llamo todas materias de cada persona para armar el json 
            #(podria haber hecho un JOIN pero me parecio mas cómodo asi porque sino tenia que separar el dato de las materias de los personales para armar el array de materias)

            cursor.execute("SELECT * FROM `materias` WHERE id_registro=(%s);", (row["id_registro"]))
            materias = cursor.fetchall()
            response.append({
                "id_registro":row["id_registro"],
                "nombre":row["nombre"],
                "email":row["email"],
                "direccion":row["direccion"],
                "telefono":row["telefono"],
                "materias":materias,

            })

    connection.close()
    return response


def getLead(id):

    connection = create_connection()

    #El mismo caso que antes, primero los datos personales y despues las materias

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `leads` WHERE id_registro=(%s);", (id))
        results = cursor.fetchone()
         
        response = results
        if results:
            results = json.loads(json.dumps(results))
            cursor.execute("SELECT * FROM `materias` WHERE id_registro=(%s);", (results["id_registro"]))
            materias = cursor.fetchall()

            response={
                    "id_registro":results["id_registro"],
                    "nombre":results["nombre"],
                    "email":results["email"],
                    "direccion":results["direccion"],
                    "telefono":results["telefono"],
                    "materias":materias,

            }
    connection.close()
    return response


def addLead(data):

    #En el parametro data viene un tipo de dato dict por lo que es facil ir desarmando el json para hacer los insert
    connection = create_connection()
    with connection.cursor() as cursor:

        #Primero se graban los datos personales
        cursor.execute("INSERT INTO `leads` (`id_registro`,`nombre`, `email`, `direccion`, `telefono`) VALUES (NULL,%s,%s,%s,%s);", (data["nombre"],data["email"],data["direccion"],data["telefono"]))
        lead_id=connection.insert_id()
        if lead_id:
            #Y luego las materias
            for materia in data['materias']:
                cursor.execute("INSERT INTO `materias` (`id_materia`, `id_registro`, `materia`, `tiempo_cursado`, `carrera`, `anio_inscripcion`, `veces_cursado`) VALUES (NULL,%s,%s,%s,%s,%s,%s);",(lead_id,materia['materia'],materia['tiempo_cursado'],materia['carrera'],materia['anio_inscripcion'],materia['veces_cursado']))
    connection.commit()
    connection.close()
    return lead_id
