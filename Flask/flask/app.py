from flask import Flask ,render_template

'''
it creates an instance of the Flask class.
which will be your WSGI application.
'''

app = Flask(__name__)



@app.route('/')
def welcome():
    return "Welcome to Flask"


@app.route('/hello')
def hello():
    return render_template('hello.html')


#GET backend se webpage me 
#POST webpage se backend me





if __name__ == '__main__':
    app.run(debug = True)