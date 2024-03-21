from flask import render_template, render_template_string, request
from flask import Flask
import re

app = Flask(__name__, static_url_path='/static')

forbidden_symbols = ['|join', '[', ']', '(', ')', 'mro', 'base', 'class', ',', '{{', '}}']

def contains_forbidden_symbols(word):
    return any(symbol in word for symbol in forbidden_symbols)

def sanitize_input(payload):
    words = re.findall(r'\w+', payload)
    return any(contains_forbidden_symbols(word) for word in words)
    
    
@app.route('/')
def index_0():
    return render_template('index.html')


@app.route('/flag')
def index():
    code = request.args.get('name')
    contains_forbidden = sanitize_input(code)
    if not contains_forbidden:
    	html = "<h1>привет</h1><p><h3> %s </h3><p>" % (code[:100])
    else:
    	html = "<h1> Содержит запрещенные символы</h1>"
    return render_template_string(html)


if __name__ == '__main__':
    app.run('0.0.0.0', '8000', debug=True)
