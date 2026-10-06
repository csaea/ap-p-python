#----------
#DATA TYPES
#----------

#KEY CONCEPTS: data types, strings, integers, floats, booleans

# The following are common (but not all) data types for python. 
#These are the only ones you'll need to know for AP CSP exam

# 1. STRINGS:
print("Hello world")
print("Once upon a time and a very good time it was there was a moocow coming down along the road and this moocow that was down along the road met a nicens little boy named baby tuckoo")
print(" ")
print("Once upon a time \nand a very good time it was \nthere was a moocow")
print("Name: \tBilly \nAge: \t14 \nGrade: \t9")

# INTEGERS
print(42)
print(-23)
print(5 + 5 - 11)

#FLOAT 
print(4.0)
print(2.0 + 4.5)
print(2.0 + 4) #returns a float

#BOOLEANS 
print(True) # 1
print(False) # 0
print(1 == 1)
print(1 != 1)
print("Hello" == "hello")
print(5 + 5 == 11)

#How do I know what data type I'm working with? 
print("\nDATA TYPE LOOKUP:\n") 

print(type("To see this message, wrap me in a print statement"))
print(type(3))
print(type(3.14))
print(type(1 == 1))