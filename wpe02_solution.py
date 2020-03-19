def myrange2(start, stop, step=None):
    result = []
    if not stop:
        stop = start
        start = 0
    if not step:
        step = 1
    counter = start
    while counter < stop:
       result.append(counter)
       counter += step
    return result


def myrange3(start, stop, step=None):
    if not stop:
        stop = start
        start = 0
    if not step:
        step = 1
    counter = start
    while counter < stop:
        yield(counter)
        counter += step


if __name__ == '__main__':
    print("Ranges the old fashioned way - in a list:")
    for num in myrange2(1,10,1.5):
        print(num)
    print("Snazzy dynamic ranges with generators!")
    for num in myrange3(1,10,2.5):
        print(num)
