import pandas as pd

empdata = {"empid": [1001, 1002, 1003, 1004, 1005, 1006],
           "ename": ["Yuvraj", "Soni", "Shivam", "Nishu", "Kartik", "Rishabh"]}

df = pd.DataFrame(empdata)
print(df)

empdata2 = [(1001, "Yuvraj"), (1002, "Soni"), (1003, "Shivam"), (1004, "Nishu"), (1005, "Kartik"), (1006, "Rishabh")]

df2 = pd.DataFrame(empdata2, columns=["empid", "ename"])
print(df2)

df3 = pd.read_csv("Book1.csv")
print(df3)
print(df3.tail())
print(df3.shape)
print(df3[2:5])
print(df3[::-1])

print(df3.columns)