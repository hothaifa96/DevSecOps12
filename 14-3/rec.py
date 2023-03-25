def demo(counter):
    if counter == 10:
        return None
    print(counter)
    counter += 1
    demo(counter)


demo(0)
