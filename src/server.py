from flask import Flask

from src.routes.clients import client
from src.routes.employees import employee
from src.routes.website import website

app = Flask(__name__)
app.register_blueprint(website)
app.register_blueprint(client)
app.register_blueprint(employee)
