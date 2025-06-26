import pandas as pd

# Create the dataset
data = {
    'Name': ['Aditi', 'Rahul', 'Neha', 'Mohan', 'Riya'],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female'],
    'Age': [23, 30, 27, 35, 21]
}

df = pd.DataFrame(data)
print(df)


mean_age = df['Age'].mean()
median_age = df['Age'].median()
mode_gender = df['Gender'].mode()[0]
range_age = df['Age'].max() - df['Age'].min()



print("Mean Age:", mean_age)
print("Median Age:", median_age)
print("Mode Gender:", mode_gender)
print("Range of Age:", range_age)


