# 1. decimal => hex
decimal_num = 1234567899999999999999999999999999
temp = decimal_num
hex_num = ''
hex_range = range(10,16)
hex_words = ['A', 'B', 'C', 'D', 'E', 'F']
hex_items = zip(hex_range, hex_words)
while temp > 0:
    remainder = temp % 16
    temp /= 16
    if remainder in hex_range:
        for i in hex_items:
            if i[0] == remainder:
                hex_num += i[1]
    else:
        hex_num += str(remainder)

print decimal_num, '<=>', hex_num[::-1]


# 2. List
list_a = range(30)
list_b = range(20, 40)

icommon = [str(i) for i in list_a if i in list_b]
print ' '.join(icommon)

i_in_a = [str(i) for i in list_a if i not in list_b]
print ' '.join(i_in_a)

i_in_b = [str(i) for i in list_b if i not in list_a]
print ' '.join(i_in_b)

all_items = icommon + i_in_a + i_in_b
print ' '.join(all_items)

ielse = i_in_a + i_in_b
print ' '.join(ielse)


