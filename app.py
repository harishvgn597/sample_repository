from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/index')
def home():
    name='John Doe'
    return render_template('index.html',name=name)

@app.route('/about')
def about():
    return render_template('about.html')
if __name__=='__main__':
    app.run()
