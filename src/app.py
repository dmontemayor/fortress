#!/usr/bin/env python

from flask import Flask

app = Flask(__name__) #app is an obj of class Flask in __name__ of this file 


@app.route('/') #root url of web app is mapped to index function 
def index(): #web app main page is named index by convention
    return '<h1>Hello Group Meeting - Welcome to Fortress! - powered by Flask</h1>' #return to browser


if __name__== '__main__': #start app using Flask web server
    app.run(debug=True)
