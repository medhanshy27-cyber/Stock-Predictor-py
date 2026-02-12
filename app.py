from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

def calculate_rsi(prices, period=14):
    deltas = np.diff(prices)
    gain = np.maximum(deltas, 0)
    loss = -np.minimum(deltas, 0)

    avg_gain = np.mean(gain[:period])
    avg_loss = np.mean(loss[:period])

    if avg_loss == 0:
        return 100

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    prices = np.array(data["prices"])

    # Moving averages
    short_ma = []
    long_ma = []
    rsi_values = []

    for i in range(len(prices)):
        if i >= 4:
            short_ma.append(float(np.mean(prices[i-4:i+1])))
        else:
            short_ma.append(None)

        if i >= 19:
            long_ma.append(float(np.mean(prices[i-19:i+1])))
        else:
            long_ma.append(None)

        if i >= 14:
            rsi_values.append(float(calculate_rsi(prices[i-14:i+1])))
        else:
            rsi_values.append(None)

    final_short = short_ma[-1]
    final_long = long_ma[-1]
    final_rsi = rsi_values[-1]

    if final_short and final_long:
        if final_short > final_long and final_rsi < 30:
            result = "STRONG BUY"
        elif final_short > final_long:
            result = "BUY"
        elif final_short < final_long and final_rsi > 70:
            result = "STRONG SELL"
        elif final_short < final_long:
            result = "SELL"
        else:
            result = "HOLD"
    else:
        result = "Not enough data"

    return jsonify({
        "result": result,
        "prices": prices.tolist(),
        "short_ma": short_ma,
        "long_ma": long_ma,
        "rsi": rsi_values
    })



if __name__ == "__main__":
    app.run(debug=True)
