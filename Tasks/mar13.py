#----------------------------TASK 1------------------------------
import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

names=[]
salaries=[]

def add_employee():
    Name=name.get()
    Salary=int(salary.get())

    names.append(Name)
    salaries.append(Salary)

    result.config(text="Employee details added")

def analyze():
    data={
        "Name":names,
        "Salary":salaries
        }

    df=pd.DataFrame(data)

    avg=np.mean(df["Salary"])
    high=np.max(df["Salary"])
    low=np.min(df["Salary"])

    result.config(text=f"Average Salary: {avg}\nHighest Salary: {high}\nLowest Salary: {low}")

    plt.bar(df["Name"],df["Salary"])
    plt.title("Employee Salary Analyser")
    plt.xlabel("Name")
    plt.ylabel("Salary")
    plt.show()
    
root=tk.Tk()
root.title("Salary Analyzer")
root.geometry("500x600")

heading=tk.Label(root,text="EMPLOYEE SALARY ANALYZER",font=("Helvetica",20,"bold italic"),fg="blue",bg="white")
heading.pack()

tk.Label(root,text="Employee Name:").pack(pady=5)
name=tk.Entry(root)
name.pack()

tk.Label(root,text="Employee Salary:").pack(pady=5)
salary=tk.Entry(root)
salary.pack()

tk.Button(root,text="Add employee",command=add_employee).pack(pady=5)
tk.Button(root,text="Analyse",command=analyze).pack(pady=5)

result=tk.Label(root,text="")
result.pack()

root.mainloop()


#----------------------------TASK 2------------------------------
import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

months=[]
units=[]

def add_data():
    Month=month.get()
    Units=int(unit.get())

    months.append(Month)
    units.append(Units)

    result.config(text="Data added")
def analyse():
    data={
        "Month":months,
        "Units":units
        }

    df=pd.DataFrame(data)

    total=np.sum(df["Units"])
    avg=np.mean(df["Units"])

    bill=total*3
    result.config(text=f"Total Units: {total}\nAverage: {avg}\nBill Amount: ₹{bill}")

    plt.plot(df["Month"],df["Units"],marker="o")
    plt.title("Electricity Usage Analyzer")
    plt.xlabel("Month")
    plt.ylabel("Units")
    plt.show()
    
    

root=tk.Tk()
root.title("Electricity bill")
root.geometry("500x600")

heading=tk.Label(root,text="ELECTRICITY BILL ANALYZER",font=("Helvetica",20,"bold italic"),fg="red",bg="yellow")
heading.pack()

tk.Label(root,text="Enter month").pack(pady=5)
month=tk.Entry(root)
month.pack()

tk.Label(root,text="Enter units").pack(pady=5)
unit=tk.Entry(root)
unit.pack()

tk.Button(root,text="Add data",command=add_data).pack()
tk.Button(root,text="Analyze data",command=analyse).pack()

result=tk.Label(root,text="")
result.pack(pady=5)
root.mainloop



#----------------------------TASK 3------------------------------
import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

days=[]
steps=[]
calories=[]

def add_data():
    Day=day.get()
    Step=int(step.get())
    Cal=int(calorie.get())

    days.append(Day)
    steps.append(Step)
    calories.append(Cal)

    result.config(text="Activity data added")

def analyse():
    data={
        "Day":days,
        "Steps":steps,
        "Calories":calories
        }

    df=pd.DataFrame(data)

    avg_steps=np.mean(df["Steps"])
    avg_calories=np.mean(df["Calories"])

    result.config(text=f"Average Steps: {avg_steps}\nAverage Calories: {avg_calories}")

    plt.plot(df["Day"],df["Steps"],marker="o",label="Steps")
    plt.plot(df["Day"],df["Calories"],marker="s",label="Calories")
    
    plt.title("Fitness Activity Tracker")
    plt.xlabel("Day")
    plt.ylabel("Activity")
    plt.legend()
    plt.show()


root=tk.Tk()
root.title("Fitness Tracker")
root.geometry("500x600")

heading=tk.Label(root,text="FITNESS ACTIVITY TRACKER",font=("Helvetica",20,"bold italic"),fg="blue",bg="white")
heading.pack()

tk.Label(root,text="Enter Day").pack(pady=5)
day=tk.Entry(root)
day.pack()

tk.Label(root,text="Enter Steps").pack(pady=5)
step=tk.Entry(root)
step.pack()

tk.Label(root,text="Enter Calories").pack(pady=5)
calorie=tk.Entry(root)
calorie.pack()

tk.Button(root,text="Add Data",command=add_data).pack()
tk.Button(root,text="Analyse",command=analyse).pack()

result=tk.Label(root,text="")
result.pack(pady=5)

root.mainloop()



#----------------------------TASK 4------------------------------
import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

names=[]
total_classes=[]
attended_classes=[]
percentage=[]

def add_data():
    Name=name.get()
    Total=int(total.get())
    Attended=int(attended.get())
    percent=(Attended/Total)*100

    names.append(Name)
    total_classes.append(Total)
    attended_classes.append(Attended)
    percentage.append(percent)

    result.config(text="data added")

def analyse():
    data={
        "Name":names,
        "Total":total_classes,
        "Attended":attended_classes,
        "Percentage":percentage
    }

    df=pd.DataFrame(data)
    avg=np.mean(df["Percentage"])

    result.config(text=f"Average attendance: {avg:.2f}%")

    plt.bar(df["Name"],df["Percentage"])
    plt.title("Student Attendance Analyzer")
    plt.xlabel("Student Name")
    plt.ylabel("Attendance %")
    plt.show()


root=tk.Tk()
root.title("Attendance Analyzer")
root.geometry("500x600")

heading=tk.Label(root,text="ATTENDANCE ANALYZER",font=("Helvetica",20,"bold italic"),fg="blue",bg="white")
heading.pack()

tk.Label(root,text="Student Name").pack(pady=5)
name=tk.Entry(root)
name.pack()

tk.Label(root,text="Total Classes").pack(pady=5)
total=tk.Entry(root)
total.pack()

tk.Label(root,text="Attended Classes").pack(pady=5)
attended=tk.Entry(root)
attended.pack()

tk.Button(root,text="Add Data",command=add_data).pack()
tk.Button(root,text="Analyse",command=analyse).pack()

result=tk.Label(root,text="")
result.pack(pady=5)

root.mainloop()



#----------------------------TASK 5------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

players=[]
scores=[]
def add_player():
    Player=name.get()
    Score=int(score.get())

    players.append(Player)
    scores.append(Score)

    result.config(text="player added")

def analyze():
    data={
        "Players":players,
        "Scores":scores
        }

    df=pd.DataFrame(data)

    total=np.sum(df["Scores"])
    avg=np.mean(df["Scores"])

    result.config(text=f"Total score: {total}\n Average score: {avg}")

    plt.bar(df["Players"],df["Scores"])
    plt.title("Cricket Score Analyzer")
    plt.xlabel("Player")
    plt.ylabel("Runs")
    plt.show()

root=tk.Tk()
root.title("Cricket Score Analyzer")
root.geometry("500x600")

heading=tk.Label(root,text="CRICKET SCORE ANALYZER",font=("Helvetica",20,"bold italic"),fg="purple",bg="white")
heading.pack()

tk.Label(root,text="Enter player name").pack(pady=5)
name=tk.Entry(root)
name.pack()

tk.Label(root,text="Enter score").pack(pady=5)
score=tk.Entry(root)
score.pack()

tk.Button(root,text="Add player data",command=add_player).pack(pady=5)
tk.Button(root,text="Analyze data",command=analyze).pack(pady=5)

result=tk.Label(root,text="")
result.pack()

root.mainloop()



#----------------------------TASK 6------------------------------
import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

days=[]
water=[]

def add_data():
    Day=day.get()
    Intake=int(intake.get())

    days.append(Day)
    water.append(Intake)

    result.config(text="Water intake data added")

def analyse():
    data={
        "Day":days,
        "Water Intake":water
        }

    df=pd.DataFrame(data)

    avg=np.mean(df["Water Intake"])

    result.config(text=f"Average Water Intake: {avg}")

    plt.plot(df["Day"],df["Water Intake"],marker="o")
    plt.title("Daily Water Intake Tracker")
    plt.xlabel("Day")
    plt.ylabel("Water Intake (ml)")
    plt.show()


root=tk.Tk()
root.title("Water Intake Tracker")
root.geometry("500x600")
root.config(bg="beige")

heading=tk.Label(root,text="DAILY WATER INTAKE TRACKER",font=("Helvetica",20,"bold italic"),fg="yellow",bg="black")
heading.pack()

tk.Label(root,text="Enter Day").pack(pady=5)
day=tk.Entry(root)
day.pack()

tk.Label(root,text="Enter Water Intake (ml)").pack(pady=5)
intake=tk.Entry(root)
intake.pack()

tk.Button(root,text="Add Data",command=add_data).pack()
tk.Button(root,text="Analyse",command=analyse).pack()

result=tk.Label(root,text="")
result.pack(pady=5)

root.mainloop()











