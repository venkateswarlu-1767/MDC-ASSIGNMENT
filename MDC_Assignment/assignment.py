
numbers = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 3 != 0:
        numbers.append(str(i))

print(",".join(numbers))


characters = ["C", "O", "D", "I", "N", "G"]

result = "".join(characters).capitalize()

print(result)

n = int(input("Enter a number: "))

squares = {}

for i in range(1, n + 1):
    squares[i] = i * i

print(squares)
