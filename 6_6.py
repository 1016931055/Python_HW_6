list1 = []
dir = {}
with open('input.txt','r') as inp:
    for line in inp:
        if(line.split()[1] not in dir): #未记录的动物
            dir[line.split()[1]] = line.split()[2]
        else:  #检测到已有动物
            if(dir[line.split()[1]] != line.split()[2]):
                if(line.split()[1] not in list1):
                    list1.append(line.split()[1])
    list1.sort(key = len)
    if(len(list1) == 0):
        print(0)
    else:
        for i in list1:
            print(i)
    inp.close()