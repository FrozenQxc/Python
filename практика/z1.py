a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

list = list(range(1,11))
a.sort()
print(a)
a.sort(reverse=True)
print(a)

print(list[::2])


print(list(filter(lambda elem: elem < 5, a)))

# for elem in (a):
#     if elem >5:
#         print(elem