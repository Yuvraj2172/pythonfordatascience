import pandas as pd
import matplotlib as plt
empdata = {"empid": [1001, 1002, 1003, 1004, 1005, 1006],
           "ename": ["Yuvraj", "Soni", "Shivam", "Nishu", "Kartik", "Rishabh"]}

df = pd.DataFrame(empdata)
print(df)

empdata2 = [(1001, "Yuvraj"), (1002, "Soni"), (1003, "Shivam"), (1004, "Nishu"), (1005, "Kartik"), (1006, "Rishabh")]

df2 = pd.DataFrame(empdata2, columns=["empid", "ename"])
print(df2)

df3 = pd.read_csv("Book1.csv",parse_dates = ['doj'])
print(df3)
print(df3.tail())
print(df3.shape)
print(df3[2:5])
print(df3[::-1])

print(df3.columns)

print(df3.empid)

print([df3.empid, df3.ename])

print(sum(df3['empid']))

print(df3.describe())

print(df3[df3.ename == 'gaurav gupta'])

df3 = df3.set_index("empid")

df3 = df3.sort_values('doj', ascending= False)
df3 = df3.fillna(0)
print(df3)
#
# x = df3['empid']
# y = df3['ename']
# g = plt.bar(x,y, label= 'Employee data', color = 'red')
# g =plt.xlabel("empid")
# g= plt.ylabel("ename")
#
# plt.legend()
# plt.show()