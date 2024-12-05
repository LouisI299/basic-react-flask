# from flask import Flask

# app = Flask(__name__)

# @app.route('/test')
# def testMessage():
#     return {'message': 'Hello, World!'}

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()