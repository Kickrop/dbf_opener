import dbf
with dbf.Table('allforms.dbf') as table:
    dbf.export(table, 'output.csv')

