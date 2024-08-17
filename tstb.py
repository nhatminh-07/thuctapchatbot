def sayhello(*names):
    for name in names:
        print("Hello,", name)

sayhello("A", "B", "C")
print()
sayhello(10, 20, 30, 40)