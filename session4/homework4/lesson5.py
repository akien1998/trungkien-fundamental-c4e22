 
s = input("input string")

counts = {}
for c in s.lower():
    counts[c] = counts.get(c, 0) +1# trả về giá trị của một đói tuongj nếu đói tượng đáy là đau là 1, cn lần 2 là 2

for c, n in sorted(counts.items()):
    print(c, n)