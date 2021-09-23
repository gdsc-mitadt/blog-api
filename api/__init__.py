from flask import Flask

from config import DefaultConfig

app = Flask(__name__)

# Load default configuration for the application (common across environments)
app.config.from_object(DefaultConfig)

# Load environment specific configuration
# app.config.from_envvar('BACKENDAPI_CONFIGURATION', silent=False)

app.config['MONGODB_SETTINGS'] = {
    'db': app.config['DB_NAME'],
    'host': app.config['DB_URI'],
    'connect': False
}

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
