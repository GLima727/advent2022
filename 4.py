f = open("input4.txt", "r")
lines = f.read()



lines = lines.split("\n")
print(lines)                                                 
                                                            
count=0

for i in lines:
    i = i.split(",")
    first = i[0].split("-")
    second = i[1].split("-")

    if(int(first[0]) <= int(second[1]) and int(first[0]) >= int(second[0]) or int(first[1]) <= int(second[1]) and int(first[1]) >= int(second[0])):
        count+=1
    elif(int(second[0]) <= int(first[1]) and int(second[0]) >= int(first[0]) or int(second[1]) <= int(first[1]) and int(second[1]) >= int(first[0])):
        count +=1
print(count)
    