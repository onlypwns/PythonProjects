import pandas as pd
import numpy as np
import os

data = pd.read_csv("data"+os.sep+"stocks.csv")
df = pd.DataFrame(data)
df

df.corr()

df['Volume Difference'] = df['Volume']-df['Yesterday Volume']
df.corr()


#done with Jupyter notebook
