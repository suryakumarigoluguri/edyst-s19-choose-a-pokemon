from flask import Flask,json,render_template

app = Flask(__name__)

@app.route('/api/pokemon')
def index():
    pk={"pokemon":["bulbasaur","charmander","squirtle"]}
    return json.dumps(pk)

if __name__ == '__main__':
    app.run(host='localhost', port=8006, debug=True)
