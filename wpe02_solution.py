def myrange3(start, stop, step=None):
    result = []
    if not step:
        step = 1
    counter = start
    while counter <= stop:
       result.append(counter)
       counter += step
    return result

if __name__ == '__main__':
    print(myrange3(1,10,2))
