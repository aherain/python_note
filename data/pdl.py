import pandas as pd
import sys
import re

from pandas import Series, DataFrame

# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
#         'year': [2000, 2001, 2002, 2001, 2002, 2003],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
#
# frame = pd.DataFrame(data)
#
# frame =pd.DataFrame(data, columns=['year', 'state'],  index=['one', 'two', 'three', 'one', 'two', 'three'])
#
# print(frame)
# print(frame.columns)
# print(frame['year'])
# pd.options.display.max_rows = 10
# df = pd.read_csv("csv", header=None, nrows=5)
#
# # df =pd.DataFrame(pd.read_table("csv", sep=','), columns=['a', 'b'])
# df.to_csv('out.csv')
# df.to_csv(sys.stdout, sep='|')

import sqlite3
import sqlalchemy as sqla
# query = """
# CREATE TABLE test
# (a VARCHAR(20), b VARCHAR(20),
#  c REAL,        d INTEGER
# );"""
con = sqlite3.connect('mydata.sqlite')
# con.execute(query)
# con.commit()

# data = [('Atlanta', 'Georgia', 1.25, 6),
#         ('Tallahassee', 'Florida', 2.6, 3),
#         ('Sacramento', 'California', 1.7, 5)]
#
# stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
# con.executemany(stmt, data)
# con.commit()
# cursor = con.execute('select * from test')
#
# rows = cursor.fetchall()
# print(rows[0][1])
#
#
# db = sqla.create_engine('sqlite:///mydata.sqlite')
# df = pd.read_sql('select * from test', db)

# df = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
#                               'Pastrami', 'corned beef', 'Bacon',
#                               'pastrami', 'honey ham', 'nova lox'],
#                      'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
#
# meat_to_animal = {
#     'bacon': 'pig',
#     'pulled pork': 'pig',
#     'pastrami': 'cow',
#     'corned beef': 'cow',
#     'honey ham': 'pig',
#     'nova lox': 'salmon'
# }
#
# lowercased = df['food'].str.lower()
#
# # df['animal'] = lowercased.map(meat_to_animal)
# df['food'].map(lambda x: meat_to_animal[x.lower()])
# print(df.replace(['bacon'], 'hahaha'))


#离散化与数据装箱

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]

cats = pd.cut(ages, bins)

print(cats)
print(pd.value_counts(cats))

# print(df)

text = "foo  bar\t baz \tqux"
a = text.split('\s+')

print(a)
print(re.split('\s+', text))

regex = re.compile('\s+')
print(regex.split(text))
