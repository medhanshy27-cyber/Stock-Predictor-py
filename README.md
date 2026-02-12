Stock-Predictor-py
# 📊 Stock AI Predictor

An interactive stock trend analysis web application built using **Python (Flask), NumPy, and JavaScript (Chart.js)**.

This project analyzes stock price data using technical indicators such as:

- Moving Average (MA)
- Relative Strength Index (RSI)

It provides real-time predictions and interactive visual charts.

---

## 🚀 Features

✔ Interactive price input  
✔ Real-time trend prediction  
✔ 5-day Short Moving Average  
✔ 20-day Long Moving Average  
✔ RSI (14-period) indicator  
✔ Dynamic charts using Chart.js  
✔ Full Python backend (No C dependency)  

---

## 🧠 Prediction Logic

The system calculates:

- Short Moving Average (5-day)
- Long Moving Average (20-day)
- RSI (14-period)

### Decision Rules:

- **STRONG BUY** → Short MA > Long MA AND RSI < 30  
- **BUY** → Short MA > Long MA  
- **STRONG SELL** → Short MA < Long MA AND RSI > 70  
- **SELL** → Short MA < Long MA  
- **HOLD** → Neutral condition  

---

## 🛠 Tech Stack

- Python (Flask)
- NumPy
- JavaScript (Fetch API)
- Chart.js
- HTML & CSS

---

## 📂 Project Structure

