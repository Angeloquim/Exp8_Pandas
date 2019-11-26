import pandas as pd

df = pd.read_csv('cars.csv')

df.to_csv('cars.csv')

a = df.iloc[[0,1,2,3,4],[1,3,5,7,9,11]]

b = df[:1]

c = df.loc[[23],['Model','cyl']]

d = df.loc[[1,28,18],['Model','cyl','gear']]