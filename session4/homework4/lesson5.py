<<<<<<< HEAD
 
s = input("input string")

counts = {}
for c in s.lower():
    counts[c] = counts.get(c, 0) +1# trả về giá trị của một đói tuongj nếu đói tượng đáy là đau là 1, cn lần 2 là 2

for c, n in sorted(counts.items()):
=======
 
s = input("input string")

counts = {}
for c in s.lower():
    counts[c] = counts.get(c, 0) +1# trả về giá trị của một đói tuongj nếu đói tượng đáy là đau là 1, cn lần 2 là 2

for c, n in sorted(counts.items()):
>>>>>>> 8fced3cd054e5b32d5744932265673d7e28d6386
    print(c, n)