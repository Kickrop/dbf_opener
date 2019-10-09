import pandas as pd
#from simpledbf import Dbf5
df = pd.read_csv('output.csv')

#df.drop(["b'col_32', 6",], axis=1)

#drop columns with zeros
df = df.drop(df.columns[df.apply(lambda col: col.sum() == 0)], axis=1)

no_place = df.groupby(
    ["(b'cur_year', 8)", "(b'razdel', 6)", "(b'num_of_row', 10)", "(b'num_of_sub', 10)"]).sum()

sub_fo_dict = pd.read_csv('sub_fo.csv', sep=';')

no_place = no_place.merge(sub_fo_dict, on="(b'num_of_sub', 10)")
#sum_fo = no_place.groupby('fo_code').sum()
no_place.to_csv("summa.csv")
#no_place.w("summa.csv")
#print(df.info())
#print(df["(b'num_of_sub', 10)"].sum())
#print(sum_fo.head())
#print(df.head())
