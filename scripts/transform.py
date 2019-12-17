import os

import pandas as pd
import requests as rq

TREFLE_TOKEN = os.environ['TREFLE_TOKEN']

# First pass ensures finding the plant in the Trefle DB
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


def query_trefle(x):
    if x["latin"] is not None:
        url = API_URL.format(token=TREFLE_TOKEN, latin=x.latin)
        global_rq = rq.get(url).json()

        if len(global_rq) is not 0:
            plant = global_rq[0]
            # If there is a result for the entry
            plant_url = plant["link"] + '?token={token}'.format(
                token=TREFLE_TOKEN
                )
            specific_rq = rq.get(plant_url).json()

            print(specific_rq["main_species"]["products"])

for item in filtered_data.iterrows():
    # Item looped as tuple(id, DataFrame)
    query_trefle(item[1])
