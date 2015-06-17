def e_bill(count):
    # electricity bill per month
    bill = 0
    if 0 <= count <= 50:
        bill += count*1230
        return bill
    elif count <= 100:
        bill += 50*1230 + (count - 50)*1530
        return bill
    elif count > 100:
        bill += 50*1230 + 50*1530 + (count - 100)*1786
        return bill
    else:
        return bill

def e_bills(months):
    # electricity bill of multiple months
    bills = [e_bill(count) for count in months]
    return bills
    
print e_bills([1, 29, 1235, 69, 100])

# [1230, 35670, 2165110, 90570, 138000]