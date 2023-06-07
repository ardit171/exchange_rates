import os

from flask import Flask, Response, jsonify

import exchange

app = Flask(__name__)

@app.route("/rates")
def rates():
    rates, last_updated = exchange.get_rates()
    data = {
        "rates": rates,
        "updated_at": last_updated
    }
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)