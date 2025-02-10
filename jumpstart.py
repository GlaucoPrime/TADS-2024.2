import pandas as pd
import polars as pl

#assim se cria uma tabela
tabela = pd.DataFrame({
    'nome': ['jp safada', 'julia charcoza', 'glauco macumbeiro'],
    'nota1': [10, 5, 10],
    'nota2': [6, 2, 9],
})

tabela[['nota2','nome', 'nota1']]
tabela.query('nome == "julia charcoza"')
tabela.query('nome in ("jp safada", "julia charcoza")')

tabela \
.assign(
    media = lambda x: ((x['nota1'] + x['nota2']) / 2)
)
