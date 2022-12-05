import numpy as np




f = open("input5.txt", "r")
lines = f.read()

lines=lines.split("\n")
memory = []
squares = []
temp = []
final = []


for i in lines:
    if(i == ""):
        break
    memory = i

max = 0
for i in memory:
    if(i != " " and max < int(i)):
        max = int(i)

for i in lines:
    if(i == ""):
        break
    squares.append(i)


count = 0

for i in squares:
    
    while(count <= len(i)):
        temp.append(i[count+1])
        count+=4
    if(i[1] != "1"):
        final.append(temp)
    count=0
    temp = []  

matrix =  [ [] for i in range(max) ] 

index = 0
for i in final:
    for j in i:
        if(j != " "):
            matrix[index].append(j)
        index+=1
    index=0
for i in range(0,max):
    matrix[i].reverse()

signal = 0
commands = []
for i in lines:
    if(i == ""):
        signal = 1
    if(signal):
        commands.append(i)

commands.pop(0)
for i in commands:
    i=i.split(" ")
    print(i)
    num = int(i[1])
    source = int(i[3])
    destination = int(i[5])

    list = matrix[destination-1][-num:]
    if(type(list) == str):
        list = [list]
    print("list:",list)
    print(source)
    print(matrix[source-1])
    matrix[source-1] = matrix[source-1].pop(num)
    if(type(matrix[source-1]) == str):
        matrix[source-1] = [matrix[source-1]]
    matrix[destination-1] = matrix[destination-1] + list
    

print(matrix)