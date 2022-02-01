
import controller# import listLeads,getLead,addLead
from flask import Flask, jsonify, request,render_template
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/leads',methods=['GET'])
def listAllLeads(): 

    leads=controller.listLeads()
    
    return jsonify(leads)


@app.route('/leads/<id>')
def getOneLead(id): 

    lead=controller.getLead(id)

    #Si la respuesta viene vacia es porque no encontro el registro
    if not lead:
        response = {"error":404,"error_message":"id de registro inexistente"}
    else:
        response = lead

    return jsonify(response)


@app.route('/leads',methods=['POST'])
def addOneLead():

    #Se recibe el json y se lo transforma en dict
    data = json.loads(json.dumps(request.json))

    #Se almacena en la base de datos
    id=controller.addLead(data) 

    #Se extrae el registro para enviar la respuesta 
    return jsonify(controller.getLead(id))

if __name__ == '__main__':

    #Creación de base de datos si no esta creada
    controller.check_database()

    #Creación de tablas si no estan creadas
    controller.check_tables()

    app.run(debug=True, port=5000)