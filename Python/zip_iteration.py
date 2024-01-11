names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]
scores = [95, 87, 92]

for name, age, score in zip(names, ages, scores):
    print(f"{name} is {age} years old and scored {score} in the exam.")
