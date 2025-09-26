#CONCEPTS VARIABLES

# use descriptive variables names. variable names can be overwritten

password = "G00seberryPie5"
email = "mharrell@nhvweb.net"
print("Password: ", password)
print("Email: ", email)

temperature = 72.5
price = 3.99

enabled = False
is_complete = True

print(is_complete)

enabled = False
#print(is_complete)

# for math problems and loops, you will see single letters, but otherwise AVOID single letter variables!

x = 3.14
y = 7
print(x + y)

i = 0
j = i + 1
print(x, y)

# variables are flexible. you create or update another variable, like so:

count = 10
print(count)
count_down = count - 2
print(count_down)
count = count_down
print(count)

#CHALLENGES

# Challenge 1: Rename Variables  
# Change the variable names x, y, z below to more descriptive names. 

x = "Radia Perlman"
y = 34
z = "Networking Engineer"

# Challenge 2: Update Variables  
# Create a variable called 'count' with a value of 10.  
# Increase it by 5 and print the result.  

count = 10
adder = count + 5
print(adder)

# Challenge 3: Swap Variables  
# Given variables x = 4 and y = "hello".  
# Swap the values so that x = "hello" and y = 4. Use a temporary variable.  
# Hint: You will need to create one new variable. 

x = 4
y = "hello"
temp = x
x = y
y = temp

print("x = ", x)
print("y = ", y)

# Challenge 4: Boolean Practice  
# Create a variable named 'is_raining' set to False.  
# On the next line, change it to True. 
# Print "Is it raining?" followed by the boolean. 

is_raining = False
is_raining = True
print("Is it raining?", is_raining)
