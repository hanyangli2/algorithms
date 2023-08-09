n = input()
n = int(n)
num_list = []

increasing = []
decreasing = []
same = []

for x in range(n):
    old, new = input().strip().split()
    old = int(old)
    new = int(new)
    temp_list = [old, new]
    if old < new:
        increasing.append(temp_list)
    elif new < old:
        decreasing.append(temp_list)
    else:
        same.append(temp_list)

print(increasing)
print(decreasing)
print(same)



