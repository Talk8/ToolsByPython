
我以前在C语言中介绍过**计算程序运行时间**的方法，该计算方法容易理解，具体步骤如下：
- 1.在程序开始运行前获取当前的时间，并且记录该时间
- 2.运行某个程序，以便统计该程序的运行时间
- 3.在程序运行结束后获取当前的时间，并且记录该时间
- 4.把步骤3和步骤1中记录的时间相减后就是程序的运行时间

我们知道```time```模块的```time()```函数具有获取当前时间的功能，使用该函数获取当前时间并且记录就可以。

> 下面是源代码，请参考：

``` python

import time

def func():
    product = 1
    for i in range(1, 3):
        product *= i
        time.sleep(1)
    return product

start = time.time()
res = func()
end = time.time()

print("start time: %d , end time: %d" %(start, end))
print("The result is %d " % res)
print("it  cost %s s for func running " %(end - start))
print("it  cost %s s for func running " %(round((end - start),3)))


```
在程序中我们使用round()函数对运行结果进行了处理，这样方便阅读。
> 下面是程序的运行结果：

``` python

start time: 1534667088 , end time: 1534667090
The result is 2 
it  cost 2.0001142024993896 s for func running 
it  cost 2.0 s for func running 

```
