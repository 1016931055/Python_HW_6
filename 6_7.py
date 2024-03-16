dir = {}
with open('input.txt','r') as inp:
    for line in inp:
        if(line.split()[1] not in dir): #未记录的动物
            dir[line.split()[1]] = 1
        else:  #检测到已有动物
            dir[line.split()[1]] += 1
    sor_dir = sorted(dir.items(),key = lambda x:x[1],reverse=True)
    for i in sor_dir:
        print(i[0],"-",i[1])
    inp.close()