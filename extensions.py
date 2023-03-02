import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote:str, base:str, amount:str):
        if quote == base:
            raise ConvertionException('Невозможно конвертировать одинаковые валюты')

        try:
            quote_tick = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}\nСписок доступных валют: /values')

        try:
            base_tick = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}\nСписок доступных валют: /values')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException('Не удалось обработать кол-во')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        temp = json.loads(r.content)[keys[base]]

        return temp

