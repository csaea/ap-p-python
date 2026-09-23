# Predict the Output
import math

f = False
t = True
nums = [10, 20, 30, 40]

# 1. Predict the output.
print(7 // 2, 7 % 2, -7 // 2)

# 2. Predict the output. Why do the two values differ?
print(int(5.9), math.floor(5.9))

# 3. Predict the output.
print("5" * 3, "5" + "5")

# 4. Predict the output. Why do the two values look different?
print(2 ** 4, math.pow(2, 4))

# 5. Predict the output.
print(True + False + True + False + True)

# 6. Predict the output. Surprised? 
print(0.5 - 0.2 == 0.3)

# 7. Predict the output. Explain.
print("Zebra" == "Zebra")

# 8. Predict the output. Show the order Python evaluates it.
print(not False or True and False)

# 9. Predict the output.
nums = [11, 20, 30, 40, 50]
print(nums[-len(nums)])

# 10. Predict every line of output.
for i in range(10, 0, -3):
    print(i)

# 11. Predict every line of output. Does 11 print? Why?
x = 5
while x < 10:
    print(x)
    x += 2