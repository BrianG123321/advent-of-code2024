import re

with open("day3.txt", "r") as file:
    content = file.read()


def mult(content):
    idx = content.find('mul(')
    total = 0
    while idx != -1:
        idx = content.find('mul(')
        string = content[idx:idx+12]
        end = string.find(")")
        string = string[0:end+1]
        start_num1 = string.find("(")
        end_num1 = string.find(",")
        if end_num1 != -1:
            number = int(string[start_num1+1:end_num1])
        else:
            number = None

        start_num2 = string.find(',')
        end_num2 = string.find(')')
        if end_num2 != -1 and start_num2 != -1:
            num2 = int(string[start_num2+1:end_num2])
        else:
            num2 = None

        if(type(number) is int and type(num2) is int):
            total += number*num2
        content = content.replace(string, "")
        if string == '':
            start = content.find('mul(')
            string = content[start:start+4]
            content = content.replace(string, "")

    return total

def part1(data):
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, "".join(data))

        result = sum(int(x) * int(y) for x, y in matches)

        return result

def remove(data):
    start = data.find("don't()")
    while start != -1:
        start = data.find("don't()")
        end = data.find("do()")

        data = data[0:start-6] + data[end:]


test = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'


import re

with open('day3.txt') as f:
    lines = [line.rstrip() for line in f]


def find_multiply_pairs(find_line):
    # Takes a line of instructions, locates all mul(x,y), multiplies each x and y
    # then returns the sum
    p_sum = 0
    p_list = re.findall("mul\((\d+,\d+)\)", find_line)
    for pair in p_list:
        int_pair = [int(a) for a in pair.split(",")]
        p_sum += int_pair[0] * int_pair[1]
    return p_sum

# Part 1
mul_result = 0
mega_line = ""
for line in lines:
    mega_line += line  # Part 2 is a lot easier if the input is all on one line
mul_result = find_multiply_pairs(mega_line)
print(f"Part 1: {mul_result}")

# Part 2
mul_result = 0
# Split the line by "don't()". Then the beginning of each group (after the first group)
# will not be doing multiplications
inst_blocks = mega_line.split("don't()")

# Start by finding all the multiplications at the beginning, when do() is on
mul_result += find_multiply_pairs(inst_blocks[0])

for n in range(1, len(inst_blocks)):
    # Each of these inst_blocks starts with don't()
    # Find where do() gets turned back on
    i = inst_blocks[n].find('do()')

    # Create a substring where do() is on
    do_string = inst_blocks[n][i:]

    # Find all the multiplications
    mul_result += find_multiply_pairs(do_string)

print(f"Part 2: {mul_result}")