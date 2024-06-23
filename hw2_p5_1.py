n = int(input("Please input a number:"))
a, b = 0, 1
for i in range(n):
    a, b = b, a + b
print("The %d-th Fibonacci sequence number is %d" % (n, a))