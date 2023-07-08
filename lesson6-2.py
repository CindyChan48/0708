import random

min=1
max=10
target =random.randint(min,max)
pinrt("猜猜看==========\n")

while Ture:
    keyin=int(input(f"猜數字{min}~{max}:"))
    count += 1
    if(keyin == target):
        print(f"猜對嘞,答案是:{target}")
        break
    else:
        print(f"你猜{count}次")
print("game over")