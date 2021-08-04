# This example will use sandbox testing from IEX Cloud. I'm using the sandbox environment,
# so the API key and data returned do not share real data. But it will give us an example
# on how to use the platform
import requests, json, csv

TOKEN = 'Tpk_bf31b0e4c5dc458d9d92eca55e5fe1a0'
SYMBOL = 'INTC'

URL = "https://sandbox.iexapis.com/stable/stock/{}/chart/max?token={}".format(SYMBOL, TOKEN)

r = requests.get(URL)
#print(r.content) # Outputs json data
json_data = json.loads(r.content)
#print(json_data) #Outputs a python list
csv_file = open('IEXcloudStockOutput.csv','w')
csv_writer = csv.writer(csv_file, lineterminator="\n") # Only need index and lineterminator options if using Windows to prevent extra empty lines...
csv_writer.writerow(['date','open','high','low','close'])
for item in json_data:
    print(item)
    csv_writer.writerow([item['date'], item['open'], item['high'], item['low'], item['close']])

csv_file.close()