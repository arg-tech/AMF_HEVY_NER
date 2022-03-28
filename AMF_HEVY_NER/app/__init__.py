from flask import Flask, request
import json
import hevyspacy

application = Flask(__name__)

    
from app import routes
