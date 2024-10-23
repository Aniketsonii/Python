strg = input()
n = len(strg)
ls =[]
for i in strg:
    if i not in ls:
        ls.append(i)
    else:
        break
print(*ls)