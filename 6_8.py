ani_dir = {}
with open('input.txt', 'r') as file:
    for line in file:
        if(line.split()[1] not in ani_dir.keys()):
            ani_dir[line.split()[1]] = []
            ani_dir[line.split()[1]].append(line.split()[0])
        else:
            ani_dir[line.split()[1]].append(line.split()[0])
            ani_dir[line.split()[1]].sort()

    #排序动物名
    sort_list = sorted(ani_dir.items(),key = lambda x:len(x[0]),reverse = False)
    print(sort_list)
    for line in sort_list:
        print(line[0],": ",sep = '',end = '')
        for num in range(0,len(line[1])):
            if num != len(line[1])-1:
                print(line[1][num], end = ', ')
            else:
                print(line[1][num], end = '')
        print()
    file.close()