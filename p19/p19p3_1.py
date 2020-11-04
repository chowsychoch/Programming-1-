
#開file 
fileHandle = open('name.txt','r')



def checkedBalance(fileHandle):
    #用 [] 草住 
    stack = []
    #sample 嘅 brackets 
    Open_Brackets = ["{", "(","[","<"]
    Close_Brackets = ["}",")","]",">"]
    #loop over every line of file 
    for line in fileHandle:
        #loop over every char of line
        for character in line:
            print(character)
            #如果character 中左 open bracket[]入面嘅 
            if character in Open_Brackets:
                # print(character,"is inside")
                #將個 char 草入去 [] 度 
                stack.append(character)
                print(stack)
            #如果character 中左 closed bracket[]入面嘅 
            elif character in Close_Brackets:
                # 搵呢個字喺close bracket 對應嘅character index
                position = Close_Brackets.index(character)
                print('pos',position)
                #stack 有野 and open brack 嘅 index == stack 最後一個index true 就 pop False 就 imbalance  
                if len(stack) != 0 and Open_Brackets[position] == stack[len(stack)-1]:
                    print('stack is',stack[len(stack)-1])
                    print('OpenBrack[pos] is ',Open_Brackets[position])
                    stack.pop()
                else:
                    return print("Not a balance one")
            # print(stack)


    if len(stack) == 0:
        print('It is balanced brackets')
    else: 
        print('It is not a balance one')



checkedBalance(fileHandle)


fileHandle.close()

#['{']
# ['{', '[']
# ['{', '[', '(']
# ['{', '[', '(', '<']

# >
# pos 3
# stack is <
# OpenBrack[pos] is  <

#logic 先 append 所