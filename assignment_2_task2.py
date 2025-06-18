'''
range_sum = 0
start = 1
end_range = 51
for i in range(start, end_range):
    range_sum = range_sum + i
print(f"The sum of numbers from {start} to {end_range - 1} is: {range_sum}")
'''

def add(x,y):
    return x + y
def square(x):
    return x ** 2

square_number = square(add(6,1))
print(square_number)