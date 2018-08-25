
在```Linux```上工作的时候难免会和```Windows```做交互，在交互的时候有一点最麻烦，那就是文件路径。比如在```Linux上```想访问```FTP```服务器
上面的内容，而```FTP```服务器是```Windows```系统，拿到的文件路径不能直接使用，因为```Windows```系统上的文件路径以```'\'```为分隔符，
而Linux系统上的文件路径以```'/'```为分隔符。这时候需要对文件路径进行转换。为此，我写了一个**自动转换文件路径**的工具。

转换的思想如下：
 - 先把Windows系统文件路径中的```'\'```为分隔符去掉。（使用字符串操作函数```split()```就可以去掉分隔符）
 - 然后把Linux系统文件路径中的```'/'```为分隔符添加进去。（使用字符串操作函数```join()```就可以去掉分隔符）
 
 在这里我对```split()```和```join()```函数做一些说明：
 - split(sp)函数可以把字符串依据参数sp中的内容分隔成子字符串，并且把所有的子字符串放到列表中，最后返回该列表。
 - join(str)函数可以子字符串连接成一个新的字符串，而连接符就是调用函数的字符，最后返回该新字符串。
 - 这两个函数经常配对使用，可以看作是一对欢喜冤家。
 
 >下面是完整的程序代码，请参考：
 
``` python

winPath= ''
winPath = input('input the path of Windows: ')
print("Path of Windows: "+winPath)

#delete the '\' of path
if winPath !='':
    list= winPath.split('\\')
else:
    print("it is null")

#add the '/' into path
linuxPath= '/'.join(list)
print("Path of Linux  : "+linuxPath)

```

 >下面是程序的运行结果：

```python

input the path of Windows: C:\Program Files\Microsoft Office\Office ( this is content of input )
Path of Windows: C:\Program Files\Microsoft Office\Office
Path of Linux  : C:/Program Files/Microsoft Office/Office

```

----------------------------
 
