import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame to include only rows with amount > 500
    rich_customers = store[store['amount'] > 500]
    
    # Get the number of unique customer IDs in the filtered DataFrame
    num_rich_customers = rich_customers['customer_id'].nunique()
    
    # Create a new DataFrame with the result
    result_df = pd.DataFrame({'rich_count': [num_rich_customers]})
    
    return result_df