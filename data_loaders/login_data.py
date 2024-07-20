import pandas as pd

file_path = '../data/login.xlsx'
def get_login_data_from_excel(file_path):

    df = pd.read_excel(file_path)
    return df.values.tolist()

login_data = get_login_data_from_excel(file_path)
