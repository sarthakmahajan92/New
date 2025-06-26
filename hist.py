import matplotlib.pyplot as plt

ages = [22, 25, 25, 27, 30, 30, 30, 35, 40]

plt.hist(ages, bins=5, color='skyblue', edgecolor='black')
plt.title("Histogram of Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
    