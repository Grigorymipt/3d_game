str = input("Строка ")
def hash(str):
    arr = []
    for i in range(0, 400):
        if str[i] == '#':
            if (i+1)%20 >= 11 and (i+1)//20 <= 9:
                arr.append([(i+1)%20-10, (i+1)//20-10])
            if (i+1)%20 == 0 and (i+1)//20 <= 9 and (i+1)//20 >= 2:
                arr.append([10, (i+1)//20-10])
            if (i+1)%20 == 0 and (i+1)//20 == 1:
                arr.append([10, (i+1)//20-11])
            if (i+1)%20 == 0 and (i+1)//20 > 9:
                arr.append([10, (i+1)//20-9])
            if (i+1)%20 >= 11 and (i+1)//20 > 9:
                arr.append([(i+1)%20-10, (i+1)//20-9])
            if (i+1)%20 <= 10 and (i+1)//20 <= 9 and (i+1)%20 != 0:
                arr.append([(i+1)%20-11, (i+1)//20-10])
            if (i+1)%20 <= 10 and (i+1)//20 > 9 and (i+1)%20 != 0:
                arr.append([(i+1)%20-11, (i+1)//20-9])
    for obj in arr:
        print(obj, sep = '\n')
hash(str)
