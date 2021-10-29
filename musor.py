import random 

row = 5
columns = 15 

for i in range(row):
    temp = []
    for j in range(columns):
        btn = j 
        temp.append(btn)

print(random.sample(temp,10))
