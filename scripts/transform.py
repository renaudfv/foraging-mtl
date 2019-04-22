import os

import pandas as pd
import requests as rq

TREFLE_TOKEN = os.environ['TREFLE_TOKEN']

API_URL = 'https://trefle.io/api/plants/?token={token}&scientific_name={latin}'

# Load data as Pandas DataFrames, keeping only the needed columns
data = pd.read_csv(
    './data.csv',
    usecols=[
        "SIGLE", "Essence_latin", "Essence_fr", "ESSENCE_ANG",
        "Date_plantation", "Longitude", "Latitude"
    ]
)

# Rename columns for standadisation and lenght
data.columns = [
    "sigle", "latin", "fr", "en", "plantation_date", "lng", "lat"
]


# Remove every entry that had missing value in lng or lat
filtered_data = data.dropna(subset=['lng', 'lat'])

# def query_trefle(x):
#     print(.)
#     url = API_URL.format(token=TREFLE_TOKEN, latin=x.latin)
#     x.trefle = rq.get(url).json()

for item in filtered_data.iterrows():
    print(item)
