
我们在工作中经常会打开各种公司内部网站，比如邮件网站，项目管理网站，bug系统网站等等一系列的网站。
常用的做法是把网站添加到收藏夹中（或者放到醒目的收藏菜单中），需要的时候再去收藏夹中找。如果收藏
的网站多了就会觉得收藏夹很乱，而且找起来比较麻烦。于是使用Python写个脚本，把工作中的网站写到列表
中，然后通过列表中元素的位置，也就是数字来索引这些网站。索引到网站后**使用浏览器打开这些网站**就可以。

> 下面是具体的代码，请参考：

``` Python
import webbrowser

workAddress=['www.baidu.com','www.sina.com','www.csdn.net']
length = len(workAddress)

print("input a number for selecting:")
for index in range(length):
    print(" %d : %s " %(index+1,workAddress[index]))

getInput=int(input())

if(0<getInput<length+1):
    webbrowser.open(workAddress[getInput-1])
else:
    print("wrong number, check again !")

```

在上面 的代码中，我们使用一些常用的网站做例子，大家可以依据自己的需要来替换掉这些网站 。

> 下面是程序运行时的情况，请参考：

``` Python
input a number for selecting:
 1 : www.baidu.com 
 2 : www.sina.com 
 3 : www.csdn.net 
3  // 输入数字3
//这时会启动系统中的浏览器打开与数字3对应的网站。
```
