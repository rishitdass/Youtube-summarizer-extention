from flask import Flask
from routes import init_routes
from flask_cors import CORS


app = Flask(__name__)

CORS(app) 

# Initialize routes
init_routes(app)

if __name__ == '__main__':
    # app.run(host='192.168.1.5', port=6969)
    app.run(debug=True)
