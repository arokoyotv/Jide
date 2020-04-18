from flask import Flask
import json
app = Flask(_name_)

@app.route('/')
def main():
        message = {'message':'Hello Naija, E go better'}
            return json.dumps(message)

        if _name_ == '_main_':
                app.run(host='0.0.0.0',port=5020)
