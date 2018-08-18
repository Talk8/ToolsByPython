#row=[i for i in range(1,10)]
#col=[i for i in range(1,10)]

format ='%d%s%d%s%2d' //format for showing
for i in range(1,10):
	for j in range(1,10):
		if(j<=i):
			print(format %(j,'*',i,'=',i*j),end='  ')  // print conten without newline
		else:
			print()
			break
print()
