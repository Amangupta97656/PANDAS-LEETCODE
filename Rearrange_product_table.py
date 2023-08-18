import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # set product_id as the index, preparing for stacking stores
    products.set_index('product_id', inplace=True)

    # stack stores
    products = products.stack(dropna=True).reset_index()

    # rename columns
    products.columns = ['product_id','store','price']
    return pd.DataFrame(products)