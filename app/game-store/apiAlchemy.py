from flask import Flask, jsonify, redirect, send_from_directory
from flask_cors import CORS
from controller.usersResource import users
from controller.categoryResource import categories
from controller.tagResource import tags
from controller.gameResource import games
from controller.orderResource import orders
import os

# Configuración de la base de datos
db_user = 'postgres'
db_password = 'flaskroot'
DATABASE_URI = os.environ.get('DATABASE_URI', f"postgresql://{db_user}:{db_password}@db/practica")

def create_api():
    api = Flask(__name__)
    api.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    api.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    CORS(api)

    # Registrar blueprints de los recursos
    api.register_blueprint(users)
    api.register_blueprint(games)
    api.register_blueprint(orders)
    api.register_blueprint(categories)
    api.register_blueprint(tags)

    # Endpoint para verificar si la API está corriendo
    @api.route('/')
    def home():
        return redirect('/swagger/index.html')

    @api.route('/swagger')
    @api.route('/swagger/<path:path>')
    def swagger_ui(path=None):
        if path is None:
            path = 'index.html'
        return send_from_directory('/app/swagger', path)

    # Endpoint para configuración de Swagger (si usas un archivo YAML)
    @api.route('/swagger-config.yaml')
    def swagger_config():
        return send_from_directory('swagger', 'swagger-config.yaml')

    return api


