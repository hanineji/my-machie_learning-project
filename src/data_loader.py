import pandas as pd

def load_csv(path):
    """Carica un dataset CSV e restituisce un DataFrame pandas."""
    return pd.read_csv(path)
