list = [0,0,0,0,0,0,0,0,0,0]
max_num = 0
max_app = 0
with open('input.txt', 'r') as inp:
    line = inp.read()
    for i in line:
        i = int(i)
        list[i] += 1
    for i in range(0,10):
        if(max_app < list[i]):
            max_num = i
            max_app = list[i]
    print(max_num)
    inp.close()


