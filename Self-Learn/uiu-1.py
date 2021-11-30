

# *** Question 1 ***:
lablist = ['d', 'e', 'f', 'h']
# check
print(lablist)

# *** Question 2 ***:
lablist.append('p')
# check
print(lablist)

# *** Question 3 ***:
lablist.extend(['e', 'f', 'g'])
# check
print(lablist)

# *** Question 4 ***:
position = lablist.index('f')
# check
print(position)

# *** Question 5 ***:
list = ['a', 'b', 'p', 'e', 'f', 'g']
list.insert(3, 'q')
# check
print(list)

# *** Question 6 ***:
list.remove('e')
# check
print(list)

# *** Question 7 ***:
list.pop()
# check
print(list)

# *** Question 8 ***:
counter = list.count('p')
# check
print(counter)

# *** Question 9 ***:
list.sort()
# check
print(list)

# *** Question 10 ***:
list.reverse()
# check
print(list)

# *** Question 11 ***:
lablist += [1,2,4,6,7]
# check
print(lablist)

# *** Question 12 ***:
sliced = lablist[2:]
# check
print(sliced)

# *** Question 13 ***:
lablist = ['q', 'p', 'f', 'b', 'a']
sliced_3 = lablist[1:-2]
# check
print(sliced_3)

# *** Question 14 ***:
lablist = [434,456,645,634,632,562,423,533,414,567,788]
minimum = min(lablist)
# check
print(minimum)

# *** Question 15 ***:
lablist = [434, 456, 645, 634, 632, 562, 423, 533, 414, 567, 788]
# same question. if wants maximin: maximum = max(lablist)