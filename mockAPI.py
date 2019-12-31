from flask import Flask, Response, stream_with_context
import time
import uuid
import random

APP = Flask(__name__)


@APP.route("/getData/<int:rowcount>", methods=["GET"])
def get_large_request(rowcount):
    """retunrs N rows of data"""
    def f():
        """The generator of mock data"""
        for _i in range(rowcount):
            time.sleep(.01)
            txid = uuid.uuid1()
            # print(txid)
            uid = uuid.uuid4()
            amount = round(random.uniform(-1000, 1000), 2)
            yield F"('{txid}', '{uid}', {amount})\n"
    return Response(stream_with_context(f()))

if __name__ == "__main__":
    APP.run(debug=True)