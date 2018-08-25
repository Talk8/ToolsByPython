

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

