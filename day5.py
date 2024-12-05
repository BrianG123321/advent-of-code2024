with open("test5.txt", "r") as file:
    content = file.read()

array = content.splitlines()
for item in range(len(array)):
    if array[item] == '':
        sec1 = array[0:item]
        sec2 = array[item+1:len(array)]

sec2list = []
for line in sec2:
    new_line = line.split(",")
    sec2list.append(new_line)

print(sec1)
print(sec2list)

def pt1(rules, updates):
    total = 0

    dict_rules = dict()
    for rule in rules:
        num1 = rule[0:2]
        num2 = rule[3:5]
        if num1 not in dict_rules:
            dict_rules[num1] = set()
        dict_rules[num1].add(f"{num2}")

    print(dict_rules)

    for update in updates:
        ordered = True
        for num in range(len(update)-1):
            i = 0
            if num in dict_rules.keys():
                num_rules = dict_rules[num]
            else:
                num_rules = set()
                
            if len(num_rules) != 0:
                while i< num:
                    if(update[i] in num_rules):
                        ordered = False
                    i+=1

        if ordered:
            total += int(update[len(update)//2])
    
    return total

print(pt1(sec1, sec2list))


    
