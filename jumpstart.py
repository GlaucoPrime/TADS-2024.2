import pandas as pd

#assim se cria uma tabela
tabela = pd.DataFrame({
    'nome': ['jp', 'julia', 'glauco'],
    'nota1': [10, 5, 10],
    'nota2': [6, 2, 9],
})

tabela[['nota2','nome', 'nota1']]
tabela.query('nome == "julia"')
tabela.query('nome in ("jp", "julia")')

tabela \
.assign(
    media = lambda x: ((x['nota1'] + x['nota2']) / 2)
)
