import pandas as pd

def create_rfm_features(df):

    rfm = pd.DataFrame()

    rfm['Recency'] = 100 - df['Spending Score (1-100)']

    rfm['Frequency'] = df['Spending Score (1-100)']

    rfm['Monetary'] = df['Annual Income (k$)']

    return rfm
