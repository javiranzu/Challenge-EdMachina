# Challenge-EdMachina

-----------------------------------------------------------------------------------------------------------

La solución consiste en una api que permite la carga y visualización de los datos de personas que cursan N materias de N carreras.
Se utilizó Flask como "micro" framework para la creación de la aplicación web, y para el front simplemente html, css y javascript.
El motor utlizado es mysql, y al inicio la aplicación verifica y crea la base de datos y las tablas si es necesario.
Se pueden obtener los resultados de los leads a través del recurso "/leads" (para todo el listado de leads) o "/leads/<id_registro>" (para obtener el resultado de uno en específico)
utilizando el método "GET"; ambos resultados son proporcionados en formato JSON.
Para la carga de los datos se utiliza el mismo recurso "/leads" con el metodo "POST" y recibe un JSON del siguiente formato:


{

    "nombre": "ezequiel",
    
    "email": "ezequiel@hotmail.com",
    
    "direccion": "ezequiel",
    
    "telefono": "8853335",
    
    "materias": [
    
        {
        
            "materia": "fisica cuantica",
            
            "tiempo_cursado": 2,
            
            "carrera": "lic en fisica",
            
            "anio_inscripcion": "2018",
            
            "veces_cursado": 1
            
        }
        
    ]
    
}

*El cual se utiliza para la carga desde el formulario.*

El formulario consiste en una sección para datos personales y otra sección para la carga de N materias relacionadas a la persona en cuestión,
donde se pueden ir precargando las materias a una lista y se pueden eliminar de la misma si asi se requiera.
La interfaz posee una validación de datos obligatorios, de mínimo de materias(1) y de email.
Al cumplirse los requisitos del formulario y enviar al información este devuelve el id de registro para su trazabilidad.

PD: adjunto la carpeta 'challenge' donde se encuentran los archivos de la base de datos(aunque no son necesarios).
