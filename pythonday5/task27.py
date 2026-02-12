n = int(input())

cubes_sum = 0

for i in range(1,n+1):
    cubes = i ** 3
    cubes_sum += cubes
print(cubes_sum)