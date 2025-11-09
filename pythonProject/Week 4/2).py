space = 0
lwrcase = 0
uprcase = 0
digits = 0
s = str(input())
for i in s :
    if i==' ':
        space += 1
    elif i >= 'a' and i <= 'z':
        lwrcase += 1
    elif i > 'A' and i <= 'Z':
        uprcase += 1
    elif i > '0' and i <= '9':
        digits += 1
print(uprcase)
print(lwrcase)
print(digits)
print(space)