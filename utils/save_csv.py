import pandas as pd

def save_csv(path, data):
    table = pd.DataFrame(data)
    table.to_csv(path, index=False)
    print('file saved at ' + path)