import pandas as pd

def create_examples() -> pd.DataFrame:
    """create a dataframe example

    Returns:
        pd.DataFrame: name and scores
    """
    tabela = pd.DataFrame({
    'nome': ['jp safada', 'julia charcoza', 'glauco macumbeiro'],
    'nota1': [10, 5, 10],
    'nota2': [6, 2, 9],
    })      

    return tabela