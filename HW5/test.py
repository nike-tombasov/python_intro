def steps(step):
    print("current step", step)

    if step == 5:
        print("end")
        exit()
    step += 1
    return step

step = 1
while True:
    step = steps(step=step)