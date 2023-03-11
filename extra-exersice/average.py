class_room = 0
# outer loop
while class_room < 3:
    class_room += 1
    print('class', class_room)

    # inner loop
    i = 0
    sum = 0
    while i < 5:
        i += 1
        grade = int(input('please enter grade'))
        if grade < 0:
            break # goes to line 17
        if grade == 0:
            i -= 1
            continue # goes to line 11
        sum += grade
    avg = sum / 5
    print('for class', class_room, ' average is', avg)