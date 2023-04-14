# https://bit.ly/3oZkT0p
# More Code https://github.com/dotLK
# https://twitter.com/MrSasindu

import random


art = {
  "up": "🔺",
  "down": "🔻"
}

one = random.randint(0,1);
two = random.randint(0,1);
thr = random.randint(0,1);
fre = random.randint(0,1);
fiv = random.randint(0,1);
six = random.randint(0,1);

list1 = [one,two,thr,fre,fiv,six]
num = []

for num in list1:
 
    # checking condition
    if num == 0:
        num = "1"
 
    else:
        num = "0"
    print(num,end=" ")


'''
roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
        
'''

