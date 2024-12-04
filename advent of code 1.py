#sort 2 lists, put into set, subtract

with open("day1.txt", "r") as file:
    content = file.read()
    
list = content.split()
list1 = []
list2 = []

for idx in range(len(list)):
    if idx % 2 == 0:
        list1.append(list[idx])
    else:
        list2.append(list[idx])

list1.sort()
list2.sort()
def repeat(list):
    for idx in range(len(list)-2):
        if(list[idx] == list[idx+1]):
            return False
        else:
            return True
        
print(repeat(list1))
print(repeat(list2))


def get_total(list1, list2):
    total = 0

    for idx in range(len(list1)):
        add = abs(int(list1[idx]) - int(list2[idx]))
        total += add

    return total

list3 = [2, 3, 4, 5]
list4 = [3, 4, 5, 6]

print(get_total(list1, list2))

def get_sim(list1, list2):
    total = 0

    for ele in list1:
        for element in list2:
            if ele == element:
                total = total + int(element)

    return total

print(get_sim(list1, list2))
