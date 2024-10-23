import re
sum =0
file = open(r'regex_sum_975255.txt',"r")
for line in file:
    num = re.findall("[0-9]+",line)
    if not num:
        continue
    else:
        for nums in num:
            sum +=int(nums)
print(sum)
