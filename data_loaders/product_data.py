import pandas as pd

file_path = '../data/products.xlsx'

def get_product_data_from_excel(file_path):

    df = pd.read_excel(file_path)
    return df['Product'].tolist()

product_data = get_product_data_from_excel(file_path=file_path)