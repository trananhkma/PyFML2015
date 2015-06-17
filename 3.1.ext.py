names = "cho meo ga chuot vit ngan"
# a,
max = 0
for i in names.replace(" ", ""):
    if names.count(i) > max:
        max = names.count(i)
        word = i

print word + ":", max



# b,
temp_list = []
for i in names.replace(" ", ""):
    if i not in temp_list:
        temp_list.append(i)
        print "{0}: {1},".format(i, names.count(i)) ,
    else:
        continue
