from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_squirrel():
    return "<p>Hello, Squirrel!</p>"

@app.route("/encode", methods=['GET'])
def encode():
  text = request.args.get('text')
  # DO YOUR ENCODE WORK HERE
  ciphertext = "your encoded codebook stuff goes here"
  return jsonify({"plaintext": text,
                  "ciphertext": ciphertext,
                  "operation": "encode"})

@app.route("/decode", methods=['GET'])
def decode():
  text = request.args.get('text')
  # DO YOUR DECODE WORK HERE
  plaintext = "your decoded codebook stuff goes here"
  return jsonify({"plaintext": plaintext,
                  "ciphertext": text,
                  "operation": "encode"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)