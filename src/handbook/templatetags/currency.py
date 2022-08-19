import requests
from django import template

register = template.Library()

@register.simple_tag
def currency():
    data = requests.get('https://www.nbrb.by/api/exrates/rates/431').json()
    #pprint(data['Cur_OfficialRate'])
    currency_today = data['Cur_OfficialRate']
    return currency_today