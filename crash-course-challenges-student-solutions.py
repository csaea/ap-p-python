# Python Real-World Coding Challenges - STARTER FILE

# ---------------- 1. Tip Calculator ----------------
bill = 75
tip=0.2*bill
print(f"Bill:{bill}\nTip:{tip}\nTotal:{bill+tip}")



# ---------------- 2. Pizza Order ----------------
import math

students = 23
slices_per_student = 2
slices_per_pizza = 8
student_slices = students * slices_per_student
total_pizzas = student_slices / slices_per_pizza
total_slices = slices_per_pizza * (math.ceil(total_pizzas))
extra_slices = total_slices - student_slices
print(f"Order {(math.ceil(total_pizzas))} pizzas")
print(f"Extra slices: {extra_slices}")
# <Your Code Here>


# ---------------- 3. Temperature Converter ----------------
fahrenheit = 32
celcius = (fahrenheit -32) * 5/9
# <Your Code Here>
print(celcius)

# ---------------- 4. Report Card ----------------
score = 100

if score >= 90:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
else:
    print("F")


# ---------------- 5. Login Screen ----------------
password = "csaea2026"
attempt = "gfdgsfy546546"

# <Your Code Here>
# if attempt=="CSAEA2026":
#     print("Access denied")
if attempt==password:
    print("Access granted")
else:
    print("Access denied")

# ---------------- 6. Even/Odd Parking ----------------
plate = 4828

if plate % 2 == 0:
    print("Park on the east side")
else:
    print("Park on the west side")


# ---------------- 7. Roller Coaster Gate ----------------
height = 33
age = 10
has_adult = False

if height < 48:
    print("You may not ride")
elif height >= 48 and age >= 10 or has_adult == True:
    print("You may ride!" )
else:
    print ("You may not ride")


# ---------------- 8. Name Tag Generator ----------------
first = "Ada"
last = "Lovelace"
school = "CSAEA"

print("Hello, my name is" + "" + first + "" + last + "" + "from" + school )
print(f"Hello, my name is {first} {last} from {school}")

# <Your Code Here>


# ---------------- 9. Shopping Cart ----------------
cart = [12, 5, 30, 8, 4]
total_price = 0 
for price in cart: 
    total_price += price 
item_count = len(cart)
print(f"total price is ${total_price}")
print(f"with {item_count} items in cart") 


# ---------------- 10. Grocery List Manager ----------------
groceries = ["milk", "eggs", "bread"]

# <Your Code Here>


# ---------------- 11. Rocket Launch ----------------
start = 10
import time
for z in range(start, 0, -1):
    print(z)
    time.sleep(1)
print("Liftoff!")

# ---------------- 12. Times Table Helper ----------------
number = 7

# <Your Code Here>


# ---------------- 13. Savings Goal ----------------
savings = 0
weekly_deposit = 15
goal = 100

# <Your Code Here>


# ---------------- 14. High Score ----------------
scores = [340, 1250, 980, 1510, 720]

# <Your Code Here>


# ---------------- 15. Class Pass Rate ----------------
grades = [88, 65, 72, 91, 54, 70]
passing = 70

# <Your Code Here>


# ---------------- 16. Garden Fence ----------------
import math

area = 49

# <Your Code Here>


# ---------------- 17. Parking Meter ----------------
import math

minutes_parked = 50
block_length = 15
cost_per_block = 1

# <Your Code Here>


# ---------------- 18. Playlist Swap ----------------
playlist = ["Intro", "Song A", "Song B", "Finale"]

# <Your Code Here>


# ---------------- 19. Leap Year Checker ----------------
year = 1900

# <Your Code Here>


# ---------------- 20. Speed Trap ----------------
speed_limit = 55
speed = 71

# <Your Code Here>
