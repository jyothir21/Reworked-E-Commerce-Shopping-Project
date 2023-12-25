import requests
import database

#* Connecting to the Fake Store API and loading the products data
product_data = requests.get('https://fakestoreapi.com/products')
# print("Connection Response:", product_data.status_code)

#* Getting the JSON format of the data
json_data = product_data.json()
# print("JSON Data:\n", json_data)

count = 0
product_names = []

for i in json_data:
    product_names.append(json_data[count]["title"])
    count += 1
    
print(product_names)



db = database.Database()
db.create_tables()
