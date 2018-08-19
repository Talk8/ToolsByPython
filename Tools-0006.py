
import time

def func():
    product = 1
    for i in range(1, 3):
        product *= i
        time.sleep(1)
    return product

start = time.time()
prod = func()
end = time.time()

print("start time: %d , end time: %d" %(start, end))
print("The result is %d " % prod)
print("it  cost %s s for func running " %(end - start))
print("it  cost %s s for func running " %(round((end - start),3)))


