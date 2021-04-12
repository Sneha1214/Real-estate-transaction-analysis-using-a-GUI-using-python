# plot 1st line graph
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
a=tk.Tk()
c1=tk.Canvas(a,width=350,height=200)
c1.pack()
entry=tk.Entry(a)
c1.create_window(150,100,window=entry)
def foo():
    global x1
    x1=str(entry.get())
    data=pd.read_csv("s.csv")
    df=pd.DataFrame(data)
    s=df["sale_date"]
    for i in range(len(s)):
        if x1==s[i]:
            b=df[i:i+1]
            print(b)
data=pd.read_csv("s.csv")
df=pd.DataFrame(data)            
btn=tk.Button(a,text="enter the sales date",command=foo,bg="green")
c1.create_window(150,140,window=btn)
root=tk.Tk()
df= pd.read_csv ('s.csv')
a=df[df['sale_date']=='Wed May 21 00:00:00 EDT 2008']['price']
figure1 = plt.Figure(figsize=(6,5), dpi=50)
ax1 = figure1.add_subplot(111)
line = FigureCanvasTkAgg(figure1, root)
line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
a.plot(kind='line', legend=True, ax=ax1, color='r',marker='o', fontsize=10)
ax1.set_title('Total number of Sales on May 21 2008')

# plot 2nd graph - Latitude and price and sales
b=df[df['city']=='SACRAMENTO']['latitude']
c=df[df['city']=='SACRAMENTO']['price']
figure3 = plt.Figure(figsize=(5,4), dpi=50)
ax3 = figure3.add_subplot(111)
ax3.scatter(b,c, color = 'g')
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend() 
ax3.set_title('Latitude versus Total Sales')

# plot 3rd graph - longitude
d=df[df['city']=='SACRAMENTO']['longitude']
e=df[df['city']=='SACRAMENTO']['price']
figure2 = plt.Figure(figsize=(4,3), dpi=50)
ax2 = figure2.add_subplot(111)
ax2.scatter(d,e, color = 'g')
scatter2 = FigureCanvasTkAgg(figure2, root) 
scatter2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax2.legend() 
ax2.set_title('longitude versus Total Sales')

 # plot graph
a=df[df['type']=='Residential']['city']
plt.title('TOTAL AREA WHICH IS RESIDENTIAL')
plt.hist(a)
import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv ('s.csv')
print(df)

# plot graph
a=df['city']
q=df['price']
plt.pie(q,labels=a)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv ('s.csv')

#plot graph
a=df['city']
b=df['beds']
# naming the x axis 
plt.xlabel('country') 
# naming the y axis 
plt.ylabel('total no of beds') 
plt.title('total number of beds for that country')
print(a)
print(b)
plt.bar(a,b)
a.mainloop()
