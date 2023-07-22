import requests
import pandas as pd

API_KEY = '8bf92359-2c11-45d9-84bb-f32f0ba480e3'

url = 'https://api.random.org/json-rpc/2/invoke'

headers = {'Content-Type': 'application/json'}
data = {
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": API_KEY,
        "n": 70,
        "min": 1,
        "max": 538,
        "replacement": False
    },
    "id": 1
}

response = requests.post(url, headers=headers, json=data)

random_numbers = response.json()['result']['random']['data']

df = pd.read_excel('data.xlsx', sheet_name='dataset')
var_description = pd.read_excel('data.xlsx', sheet_name='var description')

sample_df = df[df['population number'].isin(random_numbers)]

# Resetting the index so it starts from 0.
sample_df = sample_df.reset_index(drop=True)

# Initialize ExcelWriter
writer = pd.ExcelWriter('Sample_Data_Set.xlsx', engine='xlsxwriter')

# Write dataframes to sheets
sample_df.to_excel(writer, sheet_name='Sample Data', index=False)
var_description.to_excel(writer, sheet_name='Variable Description', index=False)

# Save the result
writer.save()

