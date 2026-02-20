import pandas as pd

print("#1: Load csv file")
df = pd.read_csv("data.csv")
print(df)
print()

print("#2: Display summary statistics")
print(df.describe(include='all'))
print()

print("#3: Age column:")
print(df['age'])
print()

print("#4: Rename age as student_age")
df.rename(columns={'age':'student_age'},inplace=True)
print(df.columns)
print()

print("#5: Remove invalid data")
df['marks']=pd.to_numeric(df['marks'],errors='coerce')
print(df)
print()

print("#6: Fill NULL marks using mean")
mean = df['marks'].mean()
df['marks']=df['marks'].fillna(mean)
print(df)
print()

print("#7: Fill NULL age using median")
median=df['student_age'].median()
df['student_age']=df['student_age'].fillna(median)

print(df)
print()

print("#8: Remove duplicates")
df.drop_duplicates(inplace=True)
print(df)
print()

print("#9: Fetch top 5 students")
print(df.head(5))
print()

print("#10: Bottom 5 students:")
print(df.tail(5))
print()

print("#11: Random 3 students:")
print(df.sample(3))
print()

print("#12: Save cleaned CSV")
df.to_csv("cleaned.csv", index=False)
print("Cleaned csv saved successfully")
print()
