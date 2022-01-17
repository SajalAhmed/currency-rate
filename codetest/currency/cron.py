import requests
from datetime import datetime
from codetest.currency.models import Convert, Currency 
def cron_job():
    URL = "https://freecurrencyapi.net/api/v2/historical"
    PARAMS = {}
    response = requests.get(url = URL, params = PARAMS)
    data = response.json()
    tdate = datetime.now().strftime("%Y-%m-%d")
    iterabledata =  data['data'][tdate]
    currency_data = []
    a = Convert(base_currency="USD", date=tdate)
    a.save()

    for it in iterabledata:
        c = Currency()
        c.name = it
        c.rate = iterabledata[it]
        c.convert = a
        currency_data.append(c)
    if len(currency_data) > 0:
        Currency.objects.bulk_create(currency_data)