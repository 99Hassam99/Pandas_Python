"""
creating dataframes
dealing with rows and columns
Operations: min max std descibe
Conditional selection
set_index
"""
import pandas as pd
weather= {
    'day' : ['1/1/24','1/2/24','1/3/24','1/4/24','1/5/24'],
    'temperature' : [23,25,21,40,35],
    "windspeed" : [6,7,3,10,2],
    'event' : ['rain','sunny','snow','mild','storm']
}

df = pd.DataFrame(weather)
print(df.describe)

df = pd.read_csv("book.csv")
print(df)

# it's kind of tuple in which (5,4) means rows and columns
rows, columns = df.shape
print(df.shape)
print(rows)


# gives the first few lines, here it gives 4 but there is no much difference but it is very helpful while dealing with big data
print(df.head())

# we also can store 1 2 or 3 rows so for that
print(df.head(2))


print(df.tail()) # it will print the last rows
print(df.tail(2)) # like this

# we can also do indexing technique like we do in python so for that
print(df[1:4])

print(df[:]) # to print everything simply [:] index this

print(df.columns)

print(df.day()) # to print individual columns

# we can do it like that
print(df['event']) # same as printing individual columns


print(df[['event','day','temperature']])


print(df['temperature'].max())

print(df['temperature'].min())

print(df['temperature'].std())

print(df['temperature'].mean())

print(df.describe())  # it does statistics on these columns

print(df[df.temperature>=25])
print(df[df.temperature==df.temperature.max()])