
在工作中有时候会给图上添加文字，常用的是PS工具，不过我想通过代码的方式来给图片添加文字。

需要使用的Python的图像库：PIL.更加详细的知识点如下：
- Imaga模块：用来创建，打开，保存图片文件
  - new(path):用来创建一个新的图片文件.该文件位于path所在的路径中。。打开后返回Image类型的图片。
  - open(path):用来打开已经存在的图片文件.该文件位于path所在的路径中。打开后返回Image类型的图片。
  - save(path):用来把创建或者打开的图片保到path所在的路径中。

- ImageDraw模块：用来在图片上绘制点，线，图形和文字。
  - Draw(Image)：用来返回一个ImageDraw类型的图片，它的参数为Image类型的图片。
  - text((x,y),str,...):用来在图片上添加文字，文字位置x,y所在坐标处，文字内容为str,其它参数可以控制文字字体和颜色。


>下面是完整的代码，请参考：

```python

from PIL import Image,ImageDraw

def addText(img,string):
    size = img.size
    width = size[0] - 20
    high = size[1] - 20
    lenth = len(string)*3
    draw = ImageDraw.Draw(img)
    draw.text((width-lenth,high),string,fill='black')
    oriImg.show()
    oriImg.save(path)


path = input("Please input the image file with path")

try:
    print("path: "+path)
    oriImg = Image.open(path)
    addText(oriImg,"good")
except IOError:
    print("can't' open the file,check the path again")
    newImg = Image.new('RGBA',(320,240),'white')
    newImg.save(path)


```

关于代码做以下说明：
 - 在代码中，会创建一个320*240和图片，背景为白色，里面什么也没有。
 - 把文字和图片边的宽度设置成了20，这个可以自己定义。另外，字符占用的长度乘以3是个经验值，也可以修改。
 - 在图片中添加的文字为'good'，这个可以自己定义。

下面是程序的运行结果：
PS:第一次运行时，如果没有图片，会有以下提示，同时会创建一个新的图片。

``` 

Please input the image file with pathH:\download\test.png(this is content of input )
path: H:\download\test.png
can't' open the file,check the path again

```
以后再次运行时，就使用系统默认的图片浏览器打开一个320*240和图片，图片右下角有黑色的文字：'good'。
我就不截图了，大家可以自己去运行。
