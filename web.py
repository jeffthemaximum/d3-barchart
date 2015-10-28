from app import app
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap()
bootstrap.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
