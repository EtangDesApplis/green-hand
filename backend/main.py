from flask import Flask, request
from flask_cors import CORS
import os
from flask import send_from_directory

app = Flask(__name__)
CORS(app)

@app.route('/<path:filePath>')
def get_file(filePath):
  pass

@app.route('/', methods=['POST'])
def post_route():

    #print(request.method)
    try:
      data = request.get_json()
      print(data)

      return {"Status":"OK"}
    except:
      return {"Status":"KO"}

if __name__=="__main__":
  #to test with curl: curl localhost:5000 -d "{\"foo\": \"ok\"}" -H 'Content-Type: application/json'
  #curl localhost:5000/Mandat.pdf

  app.run(host='0.0.0.0')