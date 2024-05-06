import requests
import json
import database
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler

# Connecting to the Fake Store API and loading the products data
product_data = requests.get('https://fakestoreapi.com/products')
print("Connection Response:", product_data.status_code)

# Getting the JSON format of the data
json_data = product_data.json()
#? print("JSON Data:\n", json.dump(json_data, indent=4))

# Create the parser and parse the arguments
parser = argparse.ArgumentParser(description="Open the database for the server")
parser.add_argument('--reset', type=bool, default=False,
                    help='A boolean to decide whether to reset the database')
args = parser.parse_args()

# Opening database for server with reset value from command line
db = database.Database(args.reset)

# Reset the database and upload the API information
if args.reset:
    db.create_tables()
    
    for data in json_data:    
        db["Products"] = (data)
    print("Database reset successfully...")

class Handler (BaseHTTPRequestHandler):
    def do_POST(self):
        print("Post method")
        
    def do_GET(self):
        print("Get method")