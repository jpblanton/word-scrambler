from flask import Flask
from flask import render_template
from flask import request
from scrambler import main, make_line, format_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def func():
    if request.method == 'POST':
        text = request.form['text']
        tmp = format_text(text)
        word_list = tmp.split(' ')
        formatted_text = main(word_list)
        formatted_text = formatted_text.split('\n')
        return render_template('index.html', text=formatted_text)