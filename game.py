import numpy as np
number = np.random.randint(1, 101)
count = 0
while True:
    count+= 1
    predict_number = int(input('Guess a number from 1 to 100'))
    if predict_number > number:
        print('Number should be smoller!')
    elif predict_number < number:
        print('Number should be bigger!')
    else:
        print(f'You did it! Number is {number}, number of try is {count}')
        break
    
