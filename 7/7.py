with open("7.txt","r") as f:
    lines=f.read()

commands=lines.split('$ ')
commands=commands[1:]
filesystem={'/':{}}
pwd = []
def getFolder():
    curr=filesystem
    for i in pwd:
        curr=curr[i]
    return curr

for command in commands:
    currFS=getFolder()
    head,*tail=command.split('\n')[:-1]
    if head=='ls':
        for file in tail:
            a,name=file.split(' ')
            if a=='dir':
                currFS[name]={}
            else:
                currFS[name]=int(a)
    else:
        cd,dir=head.split(' ')
        if dir=='/':
            pwd=['/']
            
        elif dir=='..':
            pwd.pop()
        else: 
            pwd.append(dir)


addFoldersSize={}

def getFolderSize(name,system):
    if system=={}:
        addFoldersSize[name]=0
        return 0
    elif type(system)==int:
        addFoldersSize[name]=system
        return system
    total=0
    for k,v in system.items():
        este=getFolderSize(name+' '+k,v)
        total+=este
    addFoldersSize[name]=total
    return total
        



AllITems=[]
def recursiveCalculate(system):
    if system=={}:
        return 0
    thisFolder=0
    for i in system.values():
        if type(i)==int:
            thisFolder+=i
        else:
            thisFolder+=recursiveCalculate(i)
    AllITems.append(thisFolder)
    return thisFolder

getFolderSize('',filesystem)

needeed = 30000000
has= 70000000-addFoldersSize[' /']

print(min(filter(lambda x: has+x>needeed,addFoldersSize.values())))

 

        
         