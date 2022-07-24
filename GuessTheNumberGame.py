import random
import time
# when use

print(
    """
    -----------------------------
    - welcome to the range game - 
    - enter two numbers and     -
    - then guess the random     -
    - number in the middle.     -
    - guess wrong five times    -
    - and fail ^_^              -
    - Good luck                 -
    -----------------------------
    """
)


rangenumber1 = int(input('enter first: '))
rangenumber2 = int(input('enter second: '))

Hidden_Number = random.randint(rangenumber1, rangenumber2)
number = int(input('enter the number if you dare: '))
count = 0

while number != Hidden_Number:
    if count != 5:
        count += 1
        print('ha, ha wrong again')
        number = int(input('enter the number if you dare: '))
    elif count == 5:
        print('better luck next time')
        time.sleep(0.5)


print('well done it was', Hidden_Number)
