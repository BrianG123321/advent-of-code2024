import re

with open("day4.txt", "r") as file:
    content = file.read()

matrix = content.splitlines()

test = ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"]
def find_xmas(matrix):
    total = 0
    for line in matrix:
        found = re.findall(r"XMAS", line)
        found2 = re.findall(r"SAMX", line)
        total += len(found)
        total += len(found2)
    
    for line_N in range(len(matrix)):
        for idx in range(len(matrix[line_N])):
            if matrix[line_N][idx] == "X":
                idx_X = idx
            else:
                idx_X = None

            if idx_X is not None:
                if(line_N+1 < len(matrix) and matrix[line_N+1][idx_X] == "M"):
                    if(line_N+2 < len(matrix) and matrix[line_N+2][idx_X] == "A"):
                        if(line_N+3 < len(matrix) and matrix[line_N+3][idx_X] == "S"):
                            total+=1

                if(line_N-1 >=0 and matrix[line_N-1][idx_X] == "M"):
                    if(line_N-2 >=0 and matrix[line_N-2][idx_X] == "A"):
                        if(line_N-3 >=0 and matrix[line_N-3][idx_X] == "S"):
                            total+=1

                if(line_N+1 < len(matrix) and idx_X+1 < len(matrix[line_N]) and matrix[line_N+1][idx_X+1] == "M"):
                    if(line_N+2 < len(matrix) and idx_X+2 < len(matrix[line_N]) and matrix[line_N+2][idx_X+2] == "A" ):
                        if(line_N+3 < len(matrix) and idx_X+3 < len(matrix[line_N]) and matrix[line_N+3][idx_X+3] == "S"):
                            total+=1

                if(line_N-1 >= 0 and idx_X+1 < len(matrix[line_N]) and matrix[line_N-1][idx_X+1] == "M" ):
                    if(line_N-2 >= 0 and idx_X+2 < len(matrix[line_N]) and matrix[line_N-2][idx_X+2] == "A"):
                        if(line_N-3 >= 0 and idx_X+3 < len(matrix[line_N]) and matrix[line_N-3][idx_X+3] == "S"):
                            total+=1

                if(line_N+1 < len(matrix) and idx_X-1 >= 0 and matrix[line_N+1][idx_X-1] == "M"):
                    if(line_N+2 < len(matrix) and idx_X-2 >= 0 and matrix[line_N+2][idx_X-2] == "A" ):
                        if(line_N+3 < len(matrix) and idx_X-3 >= 0 and matrix[line_N+3][idx_X-3] == "S"):
                            total+=1

                if(line_N-1 >= 0 and idx_X-1 >= 0 and matrix[line_N-1][idx_X-1] == "M"):
                    if(line_N-2 >= 0 and idx_X-2 >= 0 and matrix[line_N-2][idx_X-2] == "A"):
                        if(line_N-3 >= 0 and idx_X-3 >= 0 and matrix[line_N-3][idx_X-3] == "S"):
                            total+=1
    
    return total
        
def find_cross_mas(matrix):
    total = 0
    for line_N in range(len(matrix)):
        for idx in range(len(matrix[line_N])):
            if matrix[line_N][idx] == "A":

                if(line_N-1 >= 0 and idx-1 >= 0 and matrix[line_N-1][idx-1] == "M"):
                    if(line_N+1 < len(matrix) and idx+1 < len(matrix[line_N]) and matrix[line_N+1][idx+1] == "S"):
                        if(line_N-1 >= 0 and idx+1 < len(matrix[line_N]) and matrix[line_N-1][idx+1] == "M"):
                            if(line_N+1 < len(matrix) and idx-1 >= 0 and matrix[line_N+1][idx-1] == "S"):
                                total+= 1

                if(line_N-1 >= 0 and idx-1 >= 0 and matrix[line_N-1][idx-1] == "S"):
                    if(line_N+1 < len(matrix) and idx+1 < len(matrix[line_N]) and matrix[line_N+1][idx+1] == "M"):
                        if(line_N-1 >= 0 and idx+1 < len(matrix[line_N]) and matrix[line_N-1][idx+1] == "S"):
                            if(line_N+1 < len(matrix) and idx-1 >= 0 and matrix[line_N+1][idx-1] == "M"):
                                total+= 1

                if(line_N-1 >= 0 and idx+1 < len(matrix[line_N]) and matrix[line_N-1][idx+1] == "M"):
                    if(line_N+1 < len(matrix) and idx-1 >= 0 and matrix[line_N+1][idx-1] == "S"):
                        if(line_N+1 < len(matrix) and idx+1 < len(matrix[line_N]) and matrix[line_N+1][idx+1] == "M"):
                            if(line_N-1 >= 0 and idx-1 >= 0 and matrix[line_N-1][idx-1] == "S"):
                                total+= 1

                if(line_N-1 >= 0 and idx+1 < len(matrix[line_N]) and matrix[line_N-1][idx+1] == "S"):
                    if(line_N+1 < len(matrix) and idx-1 >= 0 and matrix[line_N+1][idx-1] == "M"):
                        if(line_N+1 < len(matrix) and idx+1 < len(matrix[line_N]) and matrix[line_N+1][idx+1] == "S"):
                            if(line_N-1 >= 0 and idx-1 >= 0 and matrix[line_N-1][idx-1] == "M"):
                                total+= 1

    return total


print(find_cross_mas(matrix))

        
