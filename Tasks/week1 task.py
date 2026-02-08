matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]]

print(matrix)

c=2
for row in matrix:
    print(row[c])

print(matrix[1])

col=[0,1,2]

for i in matrix:
    i.insert(1,int(input("Enter a number: ")))
print(matrix)
