x = input("Enter your format: ")
 
 
# x = 3[abc]2[ab]c

list_1= []
for lettr in str(x):
    if lettr == "[" or lettr == "]":
        list_1.append("")
        continue
    list_1.append(lettr)
    
    




print(list_1
