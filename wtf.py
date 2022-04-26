target = int(input())

# two paths are created whenever we hit a common factor
count = 0
for numFour in range(1,target // 4 + 1):
    if (target - (numFour*4)) % 5 == 0:
        count += 1

if target % 5 == 0:
    count += 1

print(count)