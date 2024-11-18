print("Enter a Number to get it's Table:")
#Taking input from User.
n = int(input())
print("the table of", n, "is:")
#Initializing loop.
#If 'n' is the last term in loop then range ends with n + 1.
for i in range(1, 11):
    print(n*i)
print("Exiting")