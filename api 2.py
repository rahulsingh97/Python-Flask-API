from flask import *
import json

app = Flask(__name__)


@app.route('/')
def home_page():

    data = {'Page': 'Home', 'Message': 'hi'}

    jsondump = json.dumps(data)


    return jsondump


@app.route('/name/', methods=['GET'])
def name_page():


    userquery = str(request.args.get('thename')) #/name/?thename=

    data = {'Page': 'Name', 'Your name is': f'{userquery}'}

    jsondump = json.dumps(data)


    return jsondump

@app.route('/web')
def web_page():

    return render_template('index.html')

@app.route('/gta')
def gta_page():

    return send_file('./gta.py')

@app.route('/gtazip')
def gtazip_page():

    return send_file('./gta.zip')

@app.route('/nameandage/', methods=['GET'])
def namepage_page():


    try:
        userresponse = request.args.to_dict()  #/nameandage/?name=&age=

        name = userresponse['name']
        age = userresponse['age']


        data = {'Your name is': f'{name}', 'Your age is': f'{age}'}

        jsondump = json.dumps(data)


        return jsondump

    except:
        #return redirect(url_for('error_page'))
        return redirect('https://www.youtube.com/', code=404)


@app.route('/error/', methods=['GET'])
def error_page():

    text = 'Sorry page not found'

    return text



if __name__ == '__main__':
    app.run(port=5000, debug=True)