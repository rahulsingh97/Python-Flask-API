from flask import *
import json

app = Flask(__name__)


@app.route('/')
def home_page():

    data = {'Page': 'Home', 'Message': 'hi'}

    jsondump = json.dumps(data)


    return jsondump



if __name__ == '__main__':
    app.run(port=5000, debug=True)