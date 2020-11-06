
from flask import  Blueprint, Response


productos = Blueprint('productos', __name__, url_prefix='/productos')

@productos.route('/<nombre>')
def get_productos(nombre):
    if nombre == "pygroup":
        
        return Response("ERROR! No puede utilizar este nombre",status=400)
    else:
        return Response("Exitoso! Trabajo completado {}".format(nombre),status=200)