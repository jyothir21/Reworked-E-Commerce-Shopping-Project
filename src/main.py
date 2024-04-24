import requests
import json
import database

#* Connecting to the Fake Store API and loading the products data
product_data = requests.get('https://fakestoreapi.com/products')
print("Connection Response:", product_data.status_code)

#* Getting the JSON format of the data
json_data = product_data.json()
# print("JSON Data:\n", json.dump(json_data, indent=4))

for data in json_data:    
    print(data["title"])
    print(data["rating"]["rate"])

db = database.Database()
db.create_tables()
