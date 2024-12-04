with open("day2.txt", "r") as file:
    content = file.read()

array = content.splitlines()
matrix = []
for line in array:
    matrix.append(line.split())

print(matrix)


def get_num_safe(array):
    num_safe = 0
    for i in range(len(array)):
        safe = True
        increasing = int(array[i][1]) > int(array[i][0])
        for ele in range(len(array[i])-1):
            if int(array[i][ele]) == int(array[i][ele+1]):
                safe = False
            elif int(array[i][ele]) > int(array[i][ele+1]) and increasing is True:
                safe = False
            elif int(array[i][ele]) < int(array[i][ele+1]) and increasing is False:
                safe = False
            elif abs(int(array[i][ele]) - int(array[i][ele+1])) > 3:
                safe = False
        if safe:
            num_safe +=1
        else:
            print(array[i])

    return num_safe

array1 = [[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]]

print(get_num_safe(matrix))

def line_safe(list):
    safe = True
    increasing = int(list[1]) > int(list[0])
    for ele in range(len(list)-1):
        if int(list[ele]) == int(list[ele+1]):
            safe = False
        elif int(list[ele]) > int(list[ele+1]) and increasing is True:
            safe = False
        elif int(list[ele]) < int(list[ele+1]) and increasing is False:
            safe = False
        elif abs(int(list[ele]) - int(list[ele+1])) > 3:
            safe = False
    return safe

def flex_safe(matrix):
    num_safe = 0
    for line in matrix:
        already_done = False
        if line_safe(line) is False:
            for i in range(len(line)-1):
                line_temp = line.copy()
                line_temp.pop(i)
                if line_safe(line_temp) is True and already_done is False:
                    num_safe += 1
                    already_done = True
        else:
            num_safe += 1
    return num_safe

print(flex_safe(matrix))