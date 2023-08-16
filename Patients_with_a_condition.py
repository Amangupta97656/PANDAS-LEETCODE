import pandas as pd

def find_diabetes(conditions):
    
    for condition in conditions.split(' '):
        if condition.startswith("DIAB1"):
            return True
    
    return False

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    
    result = patients[patients['conditions'].apply(find_diabetes)]
    
    return result