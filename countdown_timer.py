import time
import re
def convert(t1):
    numbers = list(map(int, re.findall(r'\d+', t1)))  

    if len(numbers) == 2:  # If both hours and minutes are given
        hrs, min = numbers
    elif len(numbers) == 1:  # If only hours or minutes is given
        if "hour" in t1:
            hrs, mi = numbers[0], 0
        else:
            hrs, min = 0, numbers[0]
    else:
        return "Invalid input"
    sec = (hrs * 3600) + (min * 60)
    print(f"timer begins at {sec} seconds;")
    timer(sec)
    
def timer(sec):
    if sec==0:
        print("time ups!!!")
        return
    print(sec)
    time.sleep(1)
    timer(sec-1)
    

t1=(input('enter the time : '))
convert(t1)