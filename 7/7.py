from functools import reduce  # forward compatibility for Python 3
import operator
with open("7.txt","r") as f:
    lines=f.read()

commands=lines.split('$ ')
commands=commands[1:]
filesystem={'/':{}}
currentFile=[]

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)

def setInDict(dataDict, mapList,key, value):
    getFromDict(dataDict, mapList)[key] = value



for command in commands:
    head,*tail=command.split('\n')[:-1]
    if head=='ls':
        for file in tail:
            a,name=file.split(' ')
            if a=='dir':
                setInDict(filesystem, currentFile,name, {})
            else:
                setInDict(filesystem, currentFile,name,int(a))
    else:
        cd,dir=head.split(' ')
        if dir=='/':
            currentFile=['/']
        elif dir=='..':
            currentFile.pop()
        else: currentFile.append(dir)
     
folderSize=[]     

def printFolderSize(filesS,prevName=''):
    lens=[]
    inHere=0
    for n,files in filesS.items():
        if type(files)==int:
            inHere+=files
        else:
            lens.append((n,printFolderSize(files,prevName+' '+n)))
    total=inHere+sum(map(lambda x:x[1],lens))
    if total>100000:
        for (n,t) in lens:
            if t<100000:
                folderSize.append((prevName+' '+n,t))
                
    return total     

printFolderSize(filesystem)
for i in folderSize:
    print(i)