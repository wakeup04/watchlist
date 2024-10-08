from flask import Flask, render_template
app = Flask(__name__)

name = 'Grey Li'
movies = [
{'title': 'JDFNFIWBWUSD', 'year':'1988'},
{'title': 'JFHFTHDFNSF', 'year':'1975'},
{'title': 'JFGFB DFGEV FSGV', 'year':'1998'},
{'title': 'ZFGGSR FGDF', 'year':'2000'},
{'title': 'sdgfdbc dfbgd', 'year':'1234'},
{'title': 'svdsvs d', 'year':'1345'},
{'title': 'aaa', 'year':'1567'},
{'title': 'cccc', 'year':'1678'},
]

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)