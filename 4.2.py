words = 'abcdefghijklmnopqrstuvwxyz'
input = ["masturbation", "pussy", "discipline", "beer", "familug"]
words_marks = {y: x  for x,y in enumerate(words, start = 1)}
mark_list = []

for i in input:
    mark = 0
    for j in i:
        if j in words_marks.keys():
            mark += words_marks[j]
    mark_list.append(mark)
            
print mark_list