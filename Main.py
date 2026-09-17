Name = input("What is your name?: ")
Age = int(input("How old are you?: "))
color = input("What is your favorite color?: ")

print("Hello", Name, "you are", Age, "and your favorite color is", color)

if Age >= 18:
    print("You are an adult!")
elif Age >= 13:
    print("You are a teenager!")
else:
    print("You are a child!")