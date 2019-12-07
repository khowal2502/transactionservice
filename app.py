from flask import Flask
from flask import request
from flask import Response

from service.transaction_service import TransactionService

import json

app = Flask(__name__)
txn_service = TransactionService()


@app.route("/transaction/<txn_id>", methods=["PUT"])
def add_transaction(txn_id):
    data = request.json

    if not txn_service.valid_request(txn_id, data):
        return Response(json.dumps({"success": "false", "message": "Not Valid Request"}),
                        status=403, mimetype="application/json")

    cnt = txn_service.insert_txn(txn_id, data)
    if cnt:
        return Response(json.dumps({"success": "true"}), status=200, mimetype="application/json")
    else:
        return Response(json.dumps({"success": "false"}), status=500, mimetype="application/json")


@app.route("/transaction/<txn_id>", methods=["GET"])
def get_transaction(txn_id):
    if txn_id is None:
        return Response(json.dumps({"success": "false", "message": "Not Valid Request"}),
                        status=403, mimetype="application/json")

    resp = txn_service.get_txn(txn_id)

    return Response(json.dumps({
        "id": resp.transaction_id,
        "amount": resp.amount,
        "type": resp.txn_type,
        "parent_id": resp.parent_id
    }), status=200, mimetype="application/json")


@app.route("/types/<type>", methods=["GET"])
def get_transaction_by_type(type):
    if type is None:
        return Response(json.dumps({"success": "false", "message": "Not Valid Request"}),
                        status=403, mimetype="application/json")

    resp = txn_service.get_txn_ids_by_type(type)

    return Response(json.dumps({
        "ids": resp
    }), status=200, mimetype="application/json")


@app.route("/sum/<txn_id>", methods=["GET"])
def get_transaction_sum(txn_id):
    if txn_id is None:
        return Response(json.dumps({"success": "false", "message": "Not Valid Request"}),
                        status=403, mimetype="application/json")

    resp = txn_service.get_txn_sum(txn_id)

    return Response(json.dumps({
        "sum": resp
    }), status=200, mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True)
