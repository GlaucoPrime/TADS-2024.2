from functions.sql import connect_db

connect_db('tads2.db')

import sqlite3
import pandas as pd
from functions.example import create_examples

conn = sqlite3.connect('tads.db') #conversa com o banco de dados

df = create_examples()

df.to_sql('escola',
          conn, 
          if_exists='replace', 
          index = False)

#
query = """
   SELECT nome AS name, nota1 
   FROM escola
   WHERE nome = 'jp safada'
 """

pd.read_sql(
    query,
    conn
)