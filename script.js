let priceChart;
let rsiChart;

function analyzeStock() {
    const input = document.getElementById("priceInput").value;
    const prices = input.split(",").map(Number);

    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prices: prices })
    })
    .then(response => response.json())
    .then(data => {

        document.getElementById("resultBox").classList.remove("hidden");
        document.getElementById("prediction").innerText =
            "Prediction: " + data.result;

        drawPriceChart(data);
        drawRSIChart(data);
    });
}

function drawPriceChart(data) {
    const ctx = document.getElementById('chart').getContext('2d');

    if (priceChart) priceChart.destroy();

    priceChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.prices.map((_, i) => i + 1),
            datasets: [
                {
                    label: 'Stock Price',
                    data: data.prices,
                    borderColor: '#00ffbf',
                    fill: false
                },
                {
                    label: 'Short MA (5)',
                    data: data.short_ma,
                    borderColor: '#ffcc00',
                    fill: false
                },
                {
                    label: 'Long MA (20)',
                    data: data.long_ma,
                    borderColor: '#ff4444',
                    fill: false
                }
            ]
        }
    });
}

function drawRSIChart(data) {
    const ctx = document.getElementById('rsiChart').getContext('2d');

    if (rsiChart) rsiChart.destroy();

    rsiChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.prices.map((_, i) => i + 1),
            datasets: [
                {
                    label: 'RSI',
                    data: data.rsi,
                    borderColor: '#66ccff',
                    fill: false
                }
            ]
        },
        options: {
            scales: {
                y: {
                    min: 0,
                    max: 100
                }
            }
        }
    });
}
