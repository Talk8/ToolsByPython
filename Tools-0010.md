
在介绍完给图上添加文字后，我们再介绍给图片上添加图片，也就是图片的叠加。

需要使用的Python的图像库：PIL.更加详细的知识点如下：
- Imaga模块：用来创建，打开，保存图片文件
  - new(path):用来创建一个新的图片文件.该文件位于path所在的路径中。打开后返回Image类型的图片。
  - open(path):用来打开已经存在的图片文件.该文件位于path所在的路径中。打开后返回Image类型的图片。
  - save(path):用来把创建或者打开的图片保到path所在的路径中。
  - paste(img,(x,y)):用来把img引用的图片粘贴到另外一张图片上，粘贴的坐标为第二个参数。

这些函数中，只有最后一个函数是新介绍的，其它的函数，我们以前介绍过。


>下面是完整的代码，请参考：

``` python

from PIL import Image

def addImg(img):
    markImg = Image.new('RGBA',(120,120),'white')
    img.paste(markImg,(0,0))
    img.save(path)

path = input("Please input the image file with path: ")

try:
    print("path: "+path)
    oriImg = Image.open(path)
    addImg(oriImg)
    oriImg.show()
except IOError:
    print("can't open the file,check the path again")
    newImg = Image.new('RGBA',(320,240),'blue')
    newImg.save(path)

```

在代码中，我们先创建了一个 ```320*240```的蓝色图片，然后再创建一个```120*120```的白色图片。
通过paste函数把白色图片添加到了蓝色图片中，添加的位置位于蓝色图片左上角。

> 下面是程序的运行结果,请参考：

!(https://githubusercontent.com/Talk8/ToolsByPython/master/res/gt001.PNG?raw=true)



