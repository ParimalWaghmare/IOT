num = int(input("Enter a 4-digit number: "))


print("Face values:")
print(num // 1000, num % 1000 // 100, num % 100 // 10, num % 10)


# print("Place values:")
print(num // 1000 * 1000, num % 1000 // 100 * 100, num % 100 // 10 * 10, num % 10 * 1)


# print(n4 * 1000, n3 * 100 , n2 * 10, n1 )
print("Number in reverse order:")
print(num % 10 * 1000 + num % 100 // 10 * 100 + num % 1000 // 100 * 10 + num // 1000)
