from operator import indexOf

# Author: Thien Doan
# Assignment: #1

# string
gym_member = "Alex Alliton"
# float
preferred_weight_kg = 20.5
# int
highest_reps = 25
# bool
membership_active = True

# Dictionary {string: tuple(int)} (yoga, running, weightlifting)
workout_stats = {
    "Trung": (30, 45, 20),
    "Josh": (25, 40, 100),
    "Justin": (20, 35, 90)
}

# d
for name, workout_time in workout_stats.copy().items():
    total_workout_time = sum(workout_time)
    workout_stats[f"{name}_total_workout_time"] = total_workout_time
print(workout_stats)

# e
# int[][]
workout_list = []

for workout_time in workout_stats.values():
    if isinstance(workout_time, tuple):
        workout_list.append(list(workout_time))

# f
yoga_running_time = [row[0:2] for row in workout_list]
print("Yoga and Running time for all friends: ", yoga_running_time)

two_friend_time = workout_list[1:3]
weightlifting_time = [row[2] for row in two_friend_time]
print("Weightlifting: ", weightlifting_time)

# g
time = 120
for name, workout_time in workout_stats.copy().items():
    if isinstance(workout_time, int):
        if workout_time > time:
            print(f"Great job staying active, {name.split('_')[0]}!")

# h
friend_name = input("Enter your friend's name: ")

if friend_name in workout_stats:
    workouts = workout_stats[friend_name]
    total = workout_stats.get(f"{friend_name}_total_workout_time", sum(workouts))

    print(f"{friend_name}'s workout minutes:")
    print(f"Yoga: {workouts[0]}")
    print(f"Running: {workouts[1]}")
    print(f"Weightlifting: {workouts[2]}")
    print(f"Total workout time: {total}")
else:
    print(f"Friend {friend_name} not found in the records.")

# i
highest_friend = 0
lowest_friend = 9999999
max_friend = ""
min_friend = ""

for name, workout_time in workout_stats.copy().items():
    if isinstance(workout_time, int):
        if workout_time > highest_friend:
            highest_friend = workout_time
            max_friend = name
        if workout_time < lowest_friend:
            lowest_friend = workout_time
            min_friend = name

print(f"Highest Friend ({max_friend.split('_')[0]}): {highest_friend}")
print(f"Lowest Friend ({min_friend.split('_')[0]}): {lowest_friend}")

