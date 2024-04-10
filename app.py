from flask import Flask, request
from flasgger import Swagger, LazyString
from flask_jwt_extended import JWTManager
from datetime import timedelta
from Routes.book_routes import bookRoute


app = Flask(__name__)



# JWT configuration, token expiry check #
app.config['JWT_SECRET_KEY'] = 'my-jwt-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=10)
jwt = JWTManager(app)

# Swagger Definition
swagger_template = dict(
info = {
    'title': LazyString(lambda: 'Book Operation APIs'),
    'version': LazyString(lambda: '0.1'),
    'description': LazyString(lambda: 'Swagger UI document'),
    },
    host = LazyString(lambda: request.host)
)

# Swagger Configuration
app.config['SWAGGER'] = {
    'title': "Book Operation APIs",
    'termsOfService': '',
    'uiversion': 3,
    "version": "0.0.1",
    "specs_route": "/swagger",
    "securityDefinitions": {
    "Bearer": {
      "type": "apiKey",
      "name": "Authorization",
      "in": "header"
    }
  }
}


Swagger(app)

app.register_blueprint(bookRoute)


if __name__ == '__main__':
    app.run(debug=True)
