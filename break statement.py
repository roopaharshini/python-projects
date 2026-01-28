a = [1, 3, 5, 7, 9, 11]
val = 2

for i in a:
    if i == val:
        print(f"Found at {i}!")
        break
else:
    print(f"not found")
