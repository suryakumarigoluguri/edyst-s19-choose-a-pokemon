from flask import Flask,json,render_template

app = Flask(__name__)

@app.route('/api/pokemon')
def index():
    pk={"pokemon":["bulbasaur","charmander","squirtle"]}
    return json.dumps(pk)

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='localhost', port=8006, debug=True)
=======
    app.run(host='localhost', port=8006, debug=True)
>>>>>>> dc2669fcc75bc383d2b9c897964d5e75de3e9bc0
