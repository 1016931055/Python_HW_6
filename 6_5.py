list = []
with open('input.txt','r') as inp:
    for line in inp:
        if(line.split()[1] not in list):
            list.append(line.split()[1])
    list.sort(key = len)
    for i in list:
        print(i)
    inp.close()
