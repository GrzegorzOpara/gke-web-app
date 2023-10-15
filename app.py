from flask import Flask, make_response, request
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    if request.method == "GET":
        response = make_response("<h1>Main page<h1>", 200)
    return response


@app.route("/health", methods=['GET'])
def health_check():
    if request.method == "GET":
        response = make_response("healthy", 200)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get("PORT"))