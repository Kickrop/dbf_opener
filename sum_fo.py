import pandas as pd
#from simpledbf import Dbf5
df = pd.read_csv('junk.csv')

#df.drop(["b'col_32', 6",], axis=1)

#drop columns with zeros
df = df.drop(df.columns[df.apply(lambda col: col.sum() == 0)], axis=1)

no_place = df.groupby(
    ["(b'cur_year', 8)", "(b'razdel', 6)", "(b'num_of_row', 10)", "(b'num_of_sub', 10)"]).sum()


#no_place.to_csv("summa.csv")
#print(df.info())
#print(df["(b'num_of_sub', 10)"].sum())
#print(no_place.head())
#print(df.head())
