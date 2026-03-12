numbers=list(map(int,input("Enter numbers:").split()))
print(max(numbers))
numbers.remove(max(numbers))
print(numbers)
print(min(numbers))
numbers.remove(min(numbers))
print(numbers)
average=sum(numbers)/len(numbers)
print("Average:",average)

OUTPUT:
Enter numbers: 5 3 65 20 79 36 2
79
[5, 3, 65, 20, 36, 2]
2
[5, 3, 65, 20, 36]
average: 25.8
