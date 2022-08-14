import requests
from datetime import date, timedelta
import json
import logging

logging.basicConfig(filename="app.log", level=logging.DEBUG)
logger = logging.getLogger(__name__)

url = "https://openexchangerates.org"

logger.info("Sending HTTP GET")
resp = requests.get(url)

logger.info("Sending HTTP POST")
resp = requests.post(url, data='My Test Data')



def write(path, mode, string):
    file = open(path, mode)
    file.write(string)
    file.close

def main():
    start_date = date(2022, 7, 8)
    end_date = date(2022, 8, 8)
    delta = timedelta(days=1)
    logging.info('Started')

    while start_date <= end_date:
        a = start_date.strftime("%Y-%m-%d")
        start_date += delta
        res = requests.get(f"https://openexchangerates.org/api/historical/{a}.json?app_id=0bf14041e40b4abab54cd5e6132a0d90")
        if res.status_code != 200:
            raise Exception("ERROR: API rquest unsuccessful.")
        data = res.json()
    with open('history.txt', 'w') as convert_file:
        convert_file.write(json.dumps(data))
    logging.info('Finished')

if __name__ == "__main__":
	main()

def handbook():
    logging.info('Started')
    res = requests.get("https://openexchangerates.org/api/currencies.json?app_id=0bf14041e40b4abab54cd5e6132a0d90")
    if res.status_code != 200:
        raise Exception("ERROR: API rquest unsuccessful.")
    data2 = res.json()

    with open('currencies.txt', 'w') as convert_file:
        convert_file.write(json.dumps(data2))
    logging.info('Finished')
handbook()




