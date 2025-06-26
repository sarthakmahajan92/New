import pandas as pd



data = {
    'Name': ['Aditi', 'Rahul', 'Neha', 'Mohan', 'Riya'],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female'],
    'Age': [23, 30, 27, 35, 21],
    'Salary': [35000, 60000, 50000, 70000, 30000] 
}

df = pd.DataFrame(data)

print(df)

print("\n--- Descriptive Statistics ---")
print("Mean Age:", df['Age'].mean())
print("Mean Salary:", df['Salary'].mean())
print("Median Salary:", df['Salary'].median())
print("Mode Gender:", df['Gender'].mode()[0])
print("Salary Range:", df['Salary'].max() - df['Salary'].min())


print("\n--- Average Age and Salary by Gender ---")
print(df.groupby('Gender')[['Age', 'Salary']].mean())


