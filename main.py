from sympy import *
k, T, C, L = symbols('k C T L')

#1
C_ost = 100000
Am_lst = []
C_ost_lst = []
for i in range(5):
  Am = (C-L)/T
  C_ost -= Am.subs({C: 100000, T:5, L:0})
  Am_lst.append(round(Am.subs({C: 100000, T:5, L:0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst: ', Am_lst)
print('C_ost_lst: ', C_ost_lst)

#2
Aj = 0
C_ost = 100000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(5):
  Am = k * 1/T * (C - Aj)
  C_ost -= Am.subs({C: 100000, T:5, k:2})
  Am_lst_2.append(round(Am.subs({C: 100000, T:5, k:2}), 2))
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2: ', Am_lst_2)
print('C_ost_lst_2: ', C_ost_lst_2)

#табл вывод
import pandas as pd
Y = range(1, 6)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tframe = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
tframe2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
print(tframe)
print(tframe2)

#контейнер граф. вывода
from matplotlib  import pyplot as plt
plt.plot(tframe['Y'], tframe['C_ost_lst'], label = 'Am')
plt.plot(tframe2['Y'], tframe2['C_ost_lst_2'], label = 'Am_2')
plt.show()
vals = Am_lst
labels = list(range(1, 6))
explode = (0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, wedgeprops = {'lw':1, 'ls':'--','edgecolor':"k"}, rotatelabels=True)
ax.axis("equal")
plt.show()