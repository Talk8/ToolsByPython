
创建无重复的文件名后，解决了重复命名的问题，不过文件名后面带一串数字还是让人觉得不舒服，怎么不舒服?就是没有哪种“所见即所得”的感觉。
为此我准备在文件名中加入日期。比如原来的文件名叫test，在test后加入当前的日期，在日期后面再加上时间戳，这样一看就能明白是“日期+时间”的组合。

加入时间戳已经介绍过了，现在介绍如何加入日期。```datetime```模块中的```datetime```类可以解决这个问题。它的```now()```函数返回当前的日期和时间，
不过是```datetime```类型。我们只需要日期就可以了，为此使用它的```date()```函数从```now()```函数的返回值中提取当前日期，然后再使用str转换为字符串类型。这样有点
绕的感觉，还有一种方法，就是使用```date```类的```now()```函数，它只返回当前日期，不过日期是```datetime.date```类型，需要转换为str类型。

得到日期后把它的文件名还有时间内戳组合在一起就可以。

另外时间戳中的数字感觉长的话可以使用取余的方法从中截取合适的长度，我在代码中截取的长度是四个数字。

下面是程序的源代码，请参考：

``` python


import time
import datetime

fileName = "test"
t = time.time()

#this the format for showing
format = "type is: %-30s , value is: %s "

#show the time
print(format %(str(type(t)),str(t)))

dateWithTime = datetime.datetime.now()
# check the type of dateWithTime
print(format %(str(type(dateWithTime)),str(dateWithTime)))

#get the date only
# date = datetime.datetime.date(dateWithTime)
# print(format %(str(type(date)),str(date)))

#another way of getting date
date = datetime.date.today()
print(format %(str(type(date)),str(date)))

#change the type of date
strDate = str(date)
print(format %(str(type(strDate)),str(strDate)))

#add the date and time in file name
fileName = fileName+'-'+strDate+'-'+str(round(t)%10000)
print(format %(str(type(fileName)),str(fileName)))

```

下面是程序的运行结果： 

``` python


type is: <class 'float'>                , value is: 1534649239.1772852 
type is: <class 'datetime.datetime'>    , value is: 2018-08-19 11:27:19.177285 
type is: <class 'datetime.date'>        , value is: 2018-08-19 
type is: <class 'str'>                  , value is: 2018-08-19 
type is: <class 'str'>                  , value is: test-2018-08-19-9239 


```
