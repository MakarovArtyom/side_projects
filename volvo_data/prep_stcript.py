import pandas as pd
import numpy as np
from datetime import datetime
from pandas import Series

# will ignore the warnings
import datetime as dt
import sqlite3
from sqlalchemy import create_engine
import csv
import warnings
warnings.filterwarnings("ignore")
# reading csv file
df= pd.read_csv('sales.csv', sep=';', encoding='utf-8')
df.drop('Unnamed: 5', axis=1, inplace=True)
# convert to str and numeric
df['sales'] = df['sales'].astype('str')
df['sales']=pd.to_numeric(df['sales'])
# date convertion
df['date_year'] = [x.strftime('%Y')for x in df['date']]
df['date_month'] = [x.strftime('%m')for x in df['date']]
# reading into sql
engine = create_engine('sqlite:///sales.db', echo=False)
df.to_sql('sales_db', con=engine)
