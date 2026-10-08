from flask import Flask, render_template, request


app = Flask(__name__)

# Основная страница
@app.route('/')
def index():
    return render_template('index.html')

#Вторая страница
@app.route('/<size>')
def Category(size):
    return render_template(
                            'Trash_1.html', 
                            size=size
                           )

#Третья страница
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'Cars.html',                           
                            size=size                          
                           )

app.run(debug=True)