import requests
from pprint import pprint

products = requests.get("https://fakestoreapi.com/products").json()

print(f"There are {len(products)} products in the 'YoungFolks' store.")

for p in products:
    print("Title:", p["title"])
    print("Category:", p["category"])
    print("Price:", p["price"], "\n")

#TODO: include the rate (not the count) of the product
#TODO: include the price
#TODO: include the picture of the product