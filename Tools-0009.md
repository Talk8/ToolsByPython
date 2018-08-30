
在制作工具时使用到了中文字符，结果出现了错误。网上搜索了各种方法仍然无效，
最后通过多次的debug和尝试才解决。为此写下来做为参考。

系统为```Ubuntu1404```,安装了```Python 2.7.6```和```Python 3.4.3```。具体的代码如下：

``` python

name = "签名文件.png"
print(name)

```

把该代码保存到```code.py```文件中，然后运行，**出错的信息**如下：

``` python

python code.py
  File "code.py", line 2
SyntaxError: Non-ASCII character '\xe7' in file code.py on line 23,
but no encoding declared; see http://www.python.org/peps/pep-0263.html for details

```

> 解决方法就是在文件开关加入以下声明：
> #coding=utf8

该声明告诉编译器源代码文件使用```utf-8```格式进行编码。

该方法的原理在于```python2```默认使用```ASCII```编码格式，而```ASCII```编码中不包括中文字符，
只有```Unicode```或者```utf-8```编码才支持中文等字符。通过这种声明，就是告诉编译器使用```utf-8```格式进行编码，
这样就能识别中文字符。

当然还有另外一种解决方法，那就是使用```python3```进行编译，因为```python3```默认使用```Unicode```编码格式.

> 具体的操作如下：

``` python

$python3 code.py
签名文件.png

```
其实问题比较简单，只要说清楚问题发生的背景和解决的原理就可以。
