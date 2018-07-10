s=input()
digit=0
letter=0
space=0
other=0
for i in s:
    if i.isnumeric():
        digit=digit+1
    elif i.isalpha():
        letter=letter+1
    elif i.isspace():
        space=space+1
    else:
        other=other+1
print(other)        
