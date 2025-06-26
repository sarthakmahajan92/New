import statistics

people = [
    {"name": "Sarthak", "gender": "F", "age": 22},
    {"name": "Ashwin", "gender": "M", "age": 25},
    {"name": "Charlie", "gender": "M", "age": 25},
    {"name": "Prem", "gender": "F", "age": 27},
    {"name": "Even", "gender": "F", "age": 30},
    {"name": "Fraud", "gender": "M", "age": 30},
    {"name": "Gracy", "gender": "F", "age": 30},
    {"name": "Henry", "gender": "M", "age": 35},
    {"name": "Head", "gender": "F", "age": 40},
]

ages = [person["age"] for person in people]

mean_age=statistics.mean(ages)
median_age=statistics.median(ages)
mode_age=statistics.mode(ages)
variance_age=statistics.variance(ages)
population_variance_age=statistics.pvariance(ages)



print("Mean age :",mean_age)
print("Median age :",median_age)
print("Mode age : ",mode_age)
print("Variance age :",variance_age)
print("Population age",population_variance_age)

