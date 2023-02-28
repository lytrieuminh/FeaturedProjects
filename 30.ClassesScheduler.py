# Let's use our knowledge of functions and loops to match a list of classes to available time slots.

def schedule_classes(classes, times):
    schedule = []
# Scheduling each element of the classes list requires a loop.
# Start with a counter variable called "index", and set it to "0":
    index = 0
    while index < len(classes):
        scheduled_class = classes[index] + ": " + times[index]
        # Add the "scheduled class" to the "schedule" list:
        schedule.append(scheduled_class)
        # To schedule the next class with each iteration, increase "index" by one after the scheduling code:
        index += 1

    return schedule


classes = ["Algebra", "History", "Biology", "Swimming"]
times = ["9a.m.", "11a.m.", "1p.m.", "3p.m."]

# Call the function, passing "classes" and "times".
# Then save the result in "schedule":
schedule = schedule_classes(classes, times)

# Display "schedule" inside an f-string:
print(f"Monday's schedule: {schedule}")

# Awesome! You've coded a function that uses a loop to match each index of classes and times to create a new list of scheduled classes.
