from flask import Flask, Response
from productos.models import productos

app = Flask(__name__)

app.register_blueprint(productos)

if __name__ == "__main__":
    app.run(debug=True)
