#open a file with read 
#declare the brackets and store it in variable and set count to zero 
#iterate the file 
#for each line iterate the character and count with specifc string.
#if the total of left equals to total of right 
#print balance 
#else
#print not balance 

fileHandle = open('name.txt','r')
left_bra="<"
right_bra=">"
left_cur = "{"
right_cur = "}"
left_bracket ="("
right_bracket=")"
left_brac="["
right_brac="]"
count_1 , count_2, count_3,count_4,count_5,count_6,count_7,count_8 = 0,0,0,0,0,0,0,0 

for line in fileHandle:
    for i in line:
        # print(i)
        count_1 += i.count(left_bra)
        # print(count_1)
        count_2 += i.count(right_bra)
        count_3 += i.count(left_cur)
        count_4 += i.count(right_cur)
        count_5 += i.count(left_bracket)
        count_6 += i.count(right_bracket)
        count_7 += i.count(left_brac)
        count_8 += i.count(right_brac)
print(f'total number of "<":{count_1}\ntotal number of ">":{count_2}\ntotal number of "{{": {count_3}\ntotal number of "}}": {count_4}\ntotal number of "(": {count_5}\ntotal number of "": {count_6}\ntotal number of "[": {count_7}\ntotal number of "]": {count_8}\n')

if (count_1 + count_3 + count_5+ count_7 == count_2+count_4+count_6+count_8):
    print('They are balanced')
else:
    print('No. They are not balanced')

fileHandle.close()
print('Finished')