# open a file with read 
#initiate count number 
#for every character in file iterate over it 
#iterate number in line
#if index of line equal to "e", count + 1 and do the same for other variables
#print result 
#close file and open file with write function 
#write function and close file 


fileHandle = open('index.html','r')
count_left ,count_right, count_newline = 0,0,0
count_e, count_string_l, count_string_r = 0,0,0
for line in fileHandle:
    for i in range (len(line)):
        # print(i)
        if line[i] == 'e':
            count_e += 1 
        elif line[i:i+4] == "<!--":
            count_string_l += 1 
        elif line[i:i+3] == "-->":
            count_string_r += 1
        elif line[i] == "<":
            count_left += 1 
        elif line[i] == ">":
            count_right +=1 
        elif line[i] == "\n":
            count_newline +=1
result = f"Number of e is {count_e}, Number of '<!--' is {count_string_l}, Number of '-->' is {count_string_r}, Number of '<' is {count_left}, Number of '>' is {count_right},Number of 'newline' is {count_newline}"

fileHandle.close()

fileHandles = open('results.txt','w')
fileHandles.write(result)
fileHandles.close()
print('Finished')