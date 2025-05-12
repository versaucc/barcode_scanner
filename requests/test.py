import requests
import pandas as pd
import os, sys

def get_nutrition_from_upc(upc_code):
    url = f"https://world.openfoodfacts.org/api/v0/product/{upc_code}.json"
    response = requests.get(url)
    data = response.json()
    if data["status"] == 1:
        product = data["product"]
        data_dict = {
            "product_name": product.get("product_name"),
            "brands": product.get("brands"),
            "nutrients": product.get("nutriments")
        }
        df = pd.DataFrame.from_dict(data, orient='index', columns=['Value'])
        df.reset_index(inplace=True)
        df.columns = ['Nutrient', 'Value']
        return df
    else:
        return {"error": "Product not found"}


"""" # Ex
df = get_nutrition_df("0049000052222")  
print(df.head())
"""

df = get_nutrition_from_upc("0000000001234")
print(df)
df.to_csv('tet.csv', index=False)
# os.mkdir('fitnessPal/tet.csv', exists='ok')
# df.to_csv('fitnessPal/tet.csv')