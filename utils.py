import requests
from datetime import datetime
from urllib import parse


def get_currency_exchange_rate(date: str,
                               base_currency: str,
                               currency: str,
                               bank: str):

    url = 'https://api.privatbank.ua/p24api/exchange_rates?json&'
    
    queryString = {'date': date}
    query = parse.urlencode(queryString)

    response = requests.get(url + query)
    json = response.json()

    if response.status_code == 200:
        date = json.get('date')
        exchange_rate = json.get('exchangeRate')
        for i in range(len(exchange_rate)):
            if exchange_rate[i].get('baseCurrency') == base_currency and exchange_rate[i].get('currency') == currency:
                if bank == 'NB':
                    rate_NB = exchange_rate[i]['saleRateNB']
                    return f'Курс НБУ на {date} при конвертации {base_currency} в {currency} - {rate_NB}'
                elif bank == 'PB':
                    try:
                        sales_rate = exchange_rate[i]['saleRate']
                        purchase_rate = exchange_rate[i]['purchaseRate']
                        return f'Курс ПриватБанка на {date} при конвертации {base_currency} в {currency} для покупки {purchase_rate} и для продажи {sales_rate}'
                    except: 
                        return f'Курс ПриватБанка на {date} при конвертации {base_currency} в {currency} не найден'
        return f'Not found: exchange rate {base_currency} to {currency}'
    else:
        return f"Api error {response.status_code}: {json.get('errorDescription')}"



#print(get_currency_exchange_rate('01.12.2014', 'UAH', 'USD', 'NB'))