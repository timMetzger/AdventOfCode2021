# Timothy Metzger
# Advent of Code 2021
# Day 22

from itertools import chain

def main():
    with open('inputs/day22.txt') as f:
        procedure = []
        for line in f:
            line = line.strip().replace(" ",',').split(",")
            state = True if line[0] == 'on' else False
            x = list(map(int,line[1].replace("x=","").split("..")))
            y = list(map(int,line[2].replace("y=", "").split("..")))
            z = list(map(int,line[3].replace("z=", "").split("..")))
            procedure.append([state,x,y,z])

    # Part 1: The straight forward dumb approach
    # cubes = []
    # for x in range(100):
    #     y_axis = []
    #     for y in range(100):
    #         inner = []
    #         for z in range(100):
    #             inner.append(False)
    #         y_axis.append(inner)
    #     cubes.append(y_axis)
    #
    #
    # cubes_on = 0
    # # instruction [state,[x1,x2],[y1,y2],[z1,z2]]
    # for state, x, y, z in procedure:
    #     if x[1] <= 50 and x[0] >= -50:
    #         if y[1] <= 50 and y[0] >= -50:
    #             if z[1] <= 50 and z[0] >= -50:
    #                 for i in range(x[0],x[1]+1):
    #                     for j in range(y[0],y[1]+1):
    #                         for k in range(z[0],z[1]+1):
    #                             if state:
    #                                 if cubes[i][j][k] is not True:
    #                                     cubes[i][j][k] = True
    #                                     cubes_on += 1
    #                             else:
    #                                 if cubes[i][j][k] is not False:
    #                                     cubes[i][j][k] = False
    #                                     cubes_on -= 1
    #
    # print("Part 1: ",cubes_on)

    # Part 2: The better approach ... maybe
    x_on = [range(0,0)]
    y_on = [range(0,0)]
    z_on = [range(0,0)]
    for state, x, y, z in procedure:
        if state:
            turn_on(x,x_on)
            turn_on(y,y_on)
            turn_on(z,z_on)
        else:
            turn_off(x,x_on)
            turn_off(y,y_on)
            turn_off(z,z_on)

def turn_on(to_turn_on,current_on):
    # Find the highest high and highest low
    ll = float('inf')
    ll_index = None
    hh = -float('inf')
    hh_index = None


    for i, r in enumerate(current_on):
        if r[0] < ll:
            ll = r[0]
            ll_index = i

        if r[1] > hh:
            hh = r[1]
            hh_index = i

    high = to_turn_on[1]
    low = to_turn_on[0]

    if len(current_on) == 1:
        if low < ll:
            current_on[0] = low

        if high > hh:
            current_on[1] = high


    else:
        if low < ll:
            current_on[ll_index][0] = low

        if high > hh:
            current_on[hh_index][1] = high






def turn_off(to_turn_off,current_on):
    pass



if __name__ == "__main__":
    main()