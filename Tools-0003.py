
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
