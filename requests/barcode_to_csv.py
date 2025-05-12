import pandas as pd
import requests
from pyzbar.pyzbar import decode
from PIL import Image
import json


def read_barcode_from_image(image_path):
    image = Image.open(image_path)
    barcodes = decode(image)
    if not barcodes:
        raise ValueError("No barcode found in image.")
    return barcodes[0].data.decode('utf-8')  # Return first detected barcode

import json
import requests

def fetch_openfoodfacts_json(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    data = response.json()

    if data.get("status") != 1:
        raise ValueError("Product not found in Open Food Facts.")

    return data  # Entire JSON object

def main():
    barcode = read_barcode_from_image("brisk_barcode.jpeg")  # or "barcode.jpeg"
    print(f"Scanned barcode: {barcode}")
    
    full_json = fetch_openfoodfacts_json(barcode)
    
    with open("barcode_test.json", "w", encoding="utf-8") as f:
        json.dump(full_json, f, indent=4, ensure_ascii=False)

    print("Full JSON saved to barcode_test.json")

if __name__ == "__main__":
    main()