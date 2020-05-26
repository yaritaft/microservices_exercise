from flask import Flask
from flask_restful import Api, Resource
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
api = Api(app)
from bike_rental.httpReq import urls
