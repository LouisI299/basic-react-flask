from flask import Flask

app = Flask(__name__)

@app.route('/test')
def testMessage():
    return {'message': 'Hello, World!'}