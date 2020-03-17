from flask import Flask, render_template, request
from RepoFind import get

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == 'POST':
        org = request.form['org']
        n = request.form['N']
        m = request.form['M']
        repos = get(org, int(n), int(m))
        if(repos == "404"):
            return "There is an error with organization or one of the values of n or m is not poitive"
        return render_template('index.html', repos = repos)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)
    