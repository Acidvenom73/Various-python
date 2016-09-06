text = "abcd"
total = 0
total1 = 0
for i in text:
    total = total + 1

for i in text:
    total1 = total1 + 1
    print text[total - total1]