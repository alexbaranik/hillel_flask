from unittest import result
from flask import Flask, request
from utils import get_currency_exchange_rate
from db_practice import get_filtered_customers, get_count_of_firstname, get_all_profit

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p><b>Hello, World!</b></p>"


@app.route("/rates", methods=['GET'])
def get_rates():
    date = request.args.get('date', default='01.12.2014')
    base_currency = request.args.get('baseCurrency', default='UAH')
    currency = request.args.get('currency', default='USD')
    bank = request.args.get('bank', default='NB')
    result = get_currency_exchange_rate(date, base_currency, currency, bank)
    return result


@app.route("/customers", methods=['GET'])
def get_customers():
    city = request.args.get('city')
    state = request.args.get('state')
    result = get_filtered_customers(city, state)
    return result


@app.route("/firstname", methods=['GET'])
def get_count_firstname():
    return get_count_of_firstname()


@app.route("/profit", methods=['GET'])
def get_profit():
    profit = round(get_all_profit()[0][0], 2)
    result = f'Общая сумма заказов - {profit}'
    return result
