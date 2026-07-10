
data_numbers:list = [1,2,3,4,5,6,7,8,9,10]

print(type(data_numbers))

total_numbers:int = 0

for data in data_numbers :
    total_numbers += data

print(total_numbers)
print(total_numbers/len(data_numbers))