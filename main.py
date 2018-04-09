from config import DevConfig
from flask import Flask

app = Flask(__name__)

app.config.from_object(DevConfig)

@app.route('/')
def home():
    return 'Hello World!!!!'

if __name__ == '__main__':
    app.run()