abhishek = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number '))
    abhishek.append(numbers)

print("Sum of Numbers is :", sum(abhishek))