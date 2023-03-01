# Someone has made a program to help direct people to the right floor in a department store.
# However, it has errors and needs fixing.

floors = {
    "lower": ["clothes", "food"],
    "upper": ["sports", "shoes"],
    "basement": ["gardening", "furniture"]
}

found = False
requested = "computers"
current = "lower"

if requested in floors[current]:
    print("Yes, on this floor.")
    found = True

else:

    for floor in ["lower", "upper", "basement"]:
        if requested in floors[floor]:
            print("On " + floor + " floor.")
            found = True

if found == False:
    print("Sorry, not sold in this store.")
