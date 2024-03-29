import pandas as pd

def read_adresse_csv_file():
    try:
        df = pd.read_csv("src\data\communes-departement-region.csv", sep=',', low_memory=False)
        return df
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"error while reading the file: {e}")
        return None
    
    
def read_conso_csv_file():
    try:
        df = pd.read_csv("src\data\conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-commune.csv.gz", 
                         sep=';', 
                         compression='gzip',
                         dtype={'Libellé Commune': str, 'Code EPCI': str, 'Libellé EPCI': str, 'Code Commune': str, 'Code Département': str})
        return df
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"error while reading the file: {e}")
        return None
