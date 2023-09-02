from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> hello from webservice</h1>"

if __name__ == "__main__":
    app.run('0.0.0.0')