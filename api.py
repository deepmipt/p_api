from flask import Flask, request, jsonify, redirect, url_for
from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy

import os


app = Flask(__name__)
Swagger(app)


@app.route('/')
def index():
    return redirect('/apidocs/')


@app.route('/answer', methods=['GET'])
def answer():
    """
    Faq Paraphraser
    ---
    parameters:
      - name: q
        in: query
        required: true
        type: string
    """
    q = request.args.get('q')
    with ClusterRpcProxy({'AMQP_URI': os.environ['AMQP_URI']}) as rpc:
        a = rpc.faq_paraphraser.predict(q)

    result = {
        'query': q,
        'question': a[0],
        'answer': a[1],
        'score': a[2]
    }
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
