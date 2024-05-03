from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

#API Key: WRGH4XCNUZA425TB
def get_stock_price(symbol):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=WRGH4XCNUZA425TB'
    response = requests.get(url)
    data = response.json()
    return data['price']