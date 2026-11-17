miles = []                 # one entry per index, in both lists
time = []
goal_pace = 8.5            # minutes per mile
logging = True

def slow_runs(time, miles, goal_pace):
    slow = []
    for index in range(len(miles)):      # loop
        pace = time[index] / miles[index]
        if pace > goal_pace:             # exactly at goal is NOT slow
            slow.append(index)
    return slow

while logging:
    distance = input("Whole miles, or type done: ")
    if distance == "done":
        logging = False
    elif distance.isdigit():             # What if: letters
        minutes = input("Whole minutes: ")
        if minutes.isdigit():            # What if: letters
            # What if: impossible numbers
            if int(distance) > 0 and int(minutes) > 0:
                miles.append(int(distance))
                time.append(int(minutes))
            else:
                print("Both numbers must be above 0.")
        else:
            print("Minutes must be a whole number.")
    else:
        print("Miles must be a whole number.")

if len(miles) == 0:                      # What if: empty list
    print("Nothing logged yet.")
else:
    print("Total miles:", sum(miles))
    print("Average pace:", sum(time) / sum(miles))
    for index in slow_runs(time, miles, goal_pace):
        print("Slower than goal:", miles[index], "mi in", time[index], "min")