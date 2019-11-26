import pandas as pd

df = pd.read_csv('cars.csv')

df.to_csv('cars.csv')

cars = df[0:5],df[27:32]

print(cars)