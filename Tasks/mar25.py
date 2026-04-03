###-------------------------------TASK 1--------------------------------
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##import tkinter as tk
##
##pages=[]
##visits=[]
##
##def add():
##    p=page.get()
##    v=visit.get()
##    
##    pages.append(p)
##    visits.append(int(v))
##
##
##def show():
##    df=pd.DataFrame({
##        "page":pages,
##        "visit":visits
##    })
##
##    total=np.sum(df["visit"])
##    result.config(text="Total visits: " + str(total))
##
##    plt.pie(df["visit"],labels=df["page"],autopct="%1.1f%%")
##    plt.title("Website Visit Distribution")
##    plt.show()
##
##root=tk.Tk()
##root.title("Website Visit Analyzer")
##root.geometry("500x600")
##
##tk.Label(root,text="Website Visit Analyzer",font=("Arial",16,"bold")).pack(pady=10)
##
##tk.Label(root,text="Page Name").pack()
##page=tk.Entry(root)
##page.pack()
##
##tk.Label(root,text="Visits").pack()
##visit=tk.Entry(root)
##visit.pack()
##
##tk.Button(root,text="Add",command=add).pack()
##tk.Button(root,text="Show Result",command=show).pack()
##
##result=tk.Label(root,text="")
##result.pack()
##
##root.mainloop()
##
##
##
##
###-------------------------------TASK 2--------------------------------
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##import tkinter as tk
##
##orders=[]
##times=[]
##
##def add():
##    o=order.get()
##    t=time.get()
##    
##    orders.append(o)
##    times.append(int(t))
##
##
##def show():
##    df=pd.DataFrame(
##        {
##        "order":orders,
##        "time":times
##    })
##
##    avg=np.mean(df["time"])
##    result.config(text="Average delivery time: " + str(avg))
##
##    plt.plot(df["order"],df["time"],marker='o')
##    plt.title("Delivery Time Tracker")
##    plt.xlabel("Order id")
##    plt.ylabel("Delivery time")
##    plt.show()
##
##root=tk.Tk()
##root.title("Delivery Time Tracker")
##root.geometry("500x600")
##
##tk.Label(root,text="DELIVERY TIME TRACKER",font=("Arial",16,"bold"),bg="yellow",fg="red").pack(pady=10)
##
##tk.Label(root,text="Order ID").pack()
##order=tk.Entry(root)
##order.pack()
##
##tk.Label(root,text="Delivery time").pack()
##time=tk.Entry(root)
##time.pack()
##
##tk.Button(root,text="Add",command=add).pack()
##tk.Button(root,text="Show result",command=show).pack()
##
##result=tk.Label(root,text="")
##result.pack()
##
##root.mainloop()
##
##
##
##
###-------------------------------TASK 3--------------------------------
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##import tkinter as tk
##
##names=[]
##salaries=[]
##
##def add():
##    n=name.get()
##    s=salary.get()
##    
##    names.append(n)
##    salaries.append(int(s))
##
##
##def show():
##    df=pd.DataFrame({
##        "name":names,
##        "salary":salaries
##    })
##
##    total=np.sum(df["salary"])
##    avg=np.mean(df["salary"])
##    result.config(text="Total: "+str(total)+" Avg: "+str(avg))
##
##    plt.bar(df["name"],df["salary"])
##    plt.title("Employee Salary Analyzer")
##    plt.xlabel("Employee")
##    plt.ylabel("Salary")
##    plt.show()
##
##root=tk.Tk()
##root.title("Employee Salary Analyzer")
##root.geometry("500x600")
##
##tk.Label(root,text="EMPLOYEE SALARY ANALYZER",font=("Arial",16,"bold"),bg="black",fg="white").pack(pady=10)
##
##tk.Label(root,text="Employee name").pack()
##name=tk.Entry(root)
##name.pack()
##
##tk.Label(root,text="salary").pack()
##salary=tk.Entry(root)
##salary.pack()
##
##tk.Button(root,text="Add",command=add).pack()
##tk.Button(root,text="Show Result",command=show).pack()
##
##result=tk.Label(root,text="")
##result.pack()
##
##root.mainloop()
##
##
##
###-------------------------------TASK 4--------------------------------
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##import tkinter as tk
##
##products=[]
##prices=[]
##
##def add():
##    p=product.get()
##    pr=price.get()
##    
##    products.append(p)
##    prices.append(int(pr))
##
##
##def show():
##    df=pd.DataFrame({
##        "product":products,
##        "price":prices
##    })
##
##    high=np.max(df["price"])
##    low=np.min(df["price"])
##    avg=np.mean(df["price"])
##    result.config(text="High: "+str(high)+"  Low: "+str(low)+"  Avg: "+str(avg))
##
##    plt.plot(df["product"],df["price"],marker='o')
##    plt.title("Product price comparison")
##    plt.xlabel("Product")
##    plt.ylabel("Price")
##    plt.show()
##
##root=tk.Tk()
##root.title("Product Price Comparison")
##root.geometry("500x600")
##
##tk.Label(root,text="Product Price Comparison",font=("Arial",16,"bold"),bg="black",fg="white").pack(pady=10,fill="x")
##
##tk.Label(root,text="Product name").pack()
##product=tk.Entry(root)
##product.pack()
##
##tk.Label(root,text="price").pack()
##price=tk.Entry(root)
##price.pack()
##
##tk.Button(root,text="Add",command=add).pack()
##tk.Button(root,text="Show Result",command=show).pack()
##
##result=tk.Label(root,text="")
##result.pack()
##
##root.mainloop()
##
##
##
##
###-------------------------------TASK 5--------------------------------
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##import tkinter as tk
##
##days=[]
##rain=[]
##
##def add():
##    d=day.get()
##    r=rainfall.get()
##    days.append(d)
##    rain.append(int(r))
##
##def show():
##    df=pd.DataFrame({
##        "day":days,
##        "rain":rain
##    })
##
##    total=np.sum(df["rain"])
##    avg=np.mean(df["rain"])
##    result.config(text="Total: "+str(total)+"  Avg: "+str(avg))
##
##    plt.plot(df["day"],df["rain"],marker='o')
##    plt.title("Rainfall data analyzer")
##    plt.xlabel("Day")
##    plt.ylabel("Rainfall")
##    plt.show()
##
##root=tk.Tk()
##root.title("Rainfall Data Analyzer")
##root.geometry("500x600")
##
##tk.Label(root,text="RAINFALL DATA ANALYZER",font=("Arial",16,"bold"),bg="navy",fg="white").pack(pady=10,fill="x")
##
##tk.Label(root,text="Day").pack()
##day=tk.Entry(root)
##day.pack()
##
##tk.Label(root,text="Rainfall").pack()
##rainfall=tk.Entry(root)
##rainfall.pack()
##
##tk.Button(root,text="Add",command=add).pack()
##tk.Button(root,text="Show Result",command=show).pack()
##
##result=tk.Label(root,text="")
##result.pack()
##
##root.mainloop()
##
##
##
###-------------------------------TASK 6--------------------------------
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##import tkinter as tk
##
##days=[]
##units=[]
##
##def add():
##    d=day.get()
##    u=unit.get()
##    
##    days.append(d)
##    units.append(int(u))
##
##
##def show():
##    df=pd.DataFrame({
##        "day":days,
##        "unit":units
##    })
##
##    total=np.sum(df["unit"])
##    avg=np.mean(df["unit"])
##    result.config(text="Total: "+str(total)+"  Avg: "+str(avg))
##
##    plt.plot(df["day"],df["unit"],marker='o')
##    plt.title("Electricity usage tracker")
##    plt.xlabel("Day")
##    plt.ylabel("Units")
##    plt.show()
##
##root=tk.Tk()
##root.title("Electricity")
##root.geometry("500x600")
##
##tk.Label(root,text="ELECTRICITY USAGE TRACKER",font=("Arial",20,"bold italic"),bg="yellow",fg="black").pack(pady=10)
##
##tk.Label(root,text="Day").pack()
##day=tk.Entry(root)
##day.pack()
##
##tk.Label(root,text="Units").pack()
##unit=tk.Entry(root)
##unit.pack()
##
##tk.Button(root,text="Add",command=add).pack()
##tk.Button(root,text="Show Result",command=show).pack()
##
##result=tk.Label(root,text="")
##result.pack()
##
##root.mainloop()



#-------------------------------TASK 7--------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

apps=[]
times=[]

def add():
    a=app.get()
    t=time.get()
    
    apps.append(a)
    times.append(int(t))


def show():
    df=pd.DataFrame({
        "app":apps,
        "time":times
    })

    total=np.sum(df["time"])
    max_app=df.loc[df["time"].idxmax(),"app"]
    result.config(text="Total: "+str(total)+"  Most used: "+str(max_app))

    plt.pie(df["time"],labels=df["app"],autopct="%1.1f%%")
    plt.title("Mobile Usage Analyzer")
    plt.show()

root=tk.Tk()
root.title("Mobile usage")
root.geometry("500x600")

tk.Label(root,text="MOBILE USAGE ANALYZER",font=("Arial",16,"bold"),bg="black",fg="yellow").pack(pady=10)

tk.Label(root,text="App name").pack()
app=tk.Entry(root)
app.pack()

tk.Label(root,text="Usage time").pack()
time=tk.Entry(root)
time.pack()

tk.Button(root,text="Add",command=add).pack()
tk.Button(root,text="Show result",command=show).pack()

result=tk.Label(root,text="")
result.pack()

root.mainloop()



#-------------------------------TASK 8--------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

products=[]
sales=[]

def add():
    p=product.get()
    s=sale.get()
    
    products.append(p)
    sales.append(int(s))


def show():
    df=pd.DataFrame({
        "product":products,
        "sale":sales
    })

    total=np.sum(df["sale"])
    best=df.loc[df["sale"].idxmax(),"product"]
    result.config(text="Total: "+str(total)+"  Best: "+str(best))

    plt.bar(df["product"],df["sale"])
    plt.title("Sales Performance Tracker")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.show()

root=tk.Tk()
root.title("Sales")
root.geometry("500x600")

tk.Label(root,text="SALES PERFORMANCE TRACKER",font=("Arial",16,"bold"),bg="white",fg="navy").pack(pady=10)

tk.Label(root,text="Product name").pack()
product=tk.Entry(root)
product.pack()

tk.Label(root,text="Sales amount").pack()
sale=tk.Entry(root)
sale.pack()

tk.Button(root,text="Add",command=add).pack()
tk.Button(root,text="result",command=show).pack()

result=tk.Label(root,text="")
result.pack()

root.mainloop()



#-------------------------------TASK 9--------------------------------
import pandas as pd
import tkinter as tk

def calculate():
    TP=int(tp.get())
    TN=int(tn.get())
    FP=int(fp.get())
    FN=int(fn.get())

    total=TP+TN+FP+FN

    acc=(TP+TN)/total
    pre=TP/(TP+FP)
    rec=TP/(TP+FN)
    f1=2*pre*rec/(pre+rec)

    result.config(text="Accuracy: "+str(acc)+"  Precision: "+str(pre)+"  Recall: "+str(rec)+"  F1: "+str(f1))

    m=[
        [TP, FN],
        [FP, TN]
    ]

    df=pd.DataFrame(m,
                    index=["Actual yes","Actual no"],
                    columns=["Pred yes","Pred no"])

    print("\nConfusion matrix:\n")
    print(df)


root=tk.Tk()
root.title("Disease prediction")
root.geometry("500x600")

tk.Label(root,
         text="DISEASE PREDICTION ANALYZER",
         font=("Arial",16,"bold italic"),
         bg="black",
         fg="white").pack(pady=10,fill="x")

tk.Label(root,text="True Positive").pack()
tp=tk.Entry(root)
tp.pack()

tk.Label(root,text="True Negative").pack()
tn=tk.Entry(root)
tn.pack()

tk.Label(root,text="False Positive").pack()
fp=tk.Entry(root)
fp.pack()

tk.Label(root,text="False Negative").pack()
fn=tk.Entry(root)
fn.pack()

tk.Button(root,text="Calculate",command=calculate).pack()

result=tk.Label(root,text="")
result.pack()

root.mainloop()
