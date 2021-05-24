import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

#Zad1 #Zad2
'''x = np.arange(20, 41)

f = []
for i in range(20, 41):
    f.append(1/i)

plt.plot(x,f,'o:')
plt.title('Wykres funkcji f(x) dla x[20,40]')
plt.legend("f(x)")
plt.xlabel('x')
plt.ylabel('1/x')
plt.xlim(20,40)
plt.ylim(0.02, 0.05)
plt.show()'''

#Zad3
'''
x = np.arange(0, 45, 0.1)

y = np.sin(x)
y2 = np.cos(x)
plt.xlabel('x')


plt.plot(x, y, x, y2)
plt.title("Wykres funkcji sin(x) i cos(x)")
plt.legend(['sin(x)', 'cos(x)'])
plt.show()
'''
#Zad4
'''
x = np.arange(0, 45, 0.1)

y = np.sin(x)
y2 = np.sin(x)
plt.xlabel('x')
plt.ylabel('sin(x)')


plt.plot(x, y+2, x, -y2)
plt.title("Wykres funkcji sin(x) i cos(x)")
plt.legend(['sin(x)', 'cos(x)'],loc = 'center left')
plt.show()
'''
#Zad5
'''
data = pd.read_csv('iris.data', header= None)

sl = data._get_column_array(0)
sw = data._get_column_array(1)

# Nie wiem co to listing 6
print(sw)
'''
#Zad6
'''
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

# pierwszy wykres
p1 = pd.DataFrame(df,columns=['Liczba','Plec'])
p2 = p1.groupby('Plec').sum()
plt.figure(1,figsize=(12,6))
plt.subplot(224)
p2.plot.bar(ax=plt.gca())

# drugi wykres
tb = pd.pivot_table(df, values=['Liczba'], index=['Rok'], columns=['Plec'], aggfunc=sum)
plt.subplot(222)
plt.plot(tb)

# trzeci wykres
c1 = pd.DataFrame(df,columns=['Liczba','Rok'])
c2 = c1.groupby('Rok').sum()
plt.subplot(121)
c2.plot.bar(ax=plt.gca())

plt.show()



'''
#Zad7
'''
xlsx = pd.read_csv('zamowienia.csv', sep =';')
df = pd.DataFrame(xlsx)
print(df)
grupa = df.groupby(['Sprzedawca']).agg({'Utarg':['sum']})
wykres = grupa.plot.pie(subplots=True, autopct = '%.2f %%',fontsize= 10,legend = None, shadow = True, explode=(0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1))


plt.show()
'''

