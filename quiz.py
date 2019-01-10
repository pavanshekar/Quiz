import numpy as np
import pandas as pd
import random

filename = 'input.csv'
data = pd.DataFrame(data = pd.read_csv(filename))
options = np.array(data.iloc[:,1:-1])
answer = np.array(data.iloc[:,-1])
questions = np.array(data.iloc[:,0])
score = 0
numbers = []
while len(numbers)<3:
    index = random.randrange(0,5)
    if index not in numbers:
        numbers.append(index)

for i in numbers:
    print(questions[i])
    print('The options are')
    for op in options[i]:
    	print(op)
    ans = input("Answer ? ")
    if ans.lower() == answer[i].lower():
        score += 1
        print("Correct Answer\n")
    else:
        print("Wrong Answer\n")
print("Score = ",score)
