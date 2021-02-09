from main import goal_array

#Heuristika ktora pocita kolko policok nie je na svojom mieste
def position_number(array):
    wrong_position = 0
    for i in range(len(array)):
        if array[i] == 0:
            continue
        if array[i] != goal_array[i]:
            wrong_position = wrong_position + 1
    return wrong_position

#Heuristika ktora vypocita sucet vzdialenosti jednotlivych policok od cielovej pozicie
def distance_number(array):
        sum_distance = 0
        for i in range(1, len(array)):
            if goal_array.index(i) > array.index(i):
                difference = goal_array.index(i) - array.index(i)
            else:
                difference = array.index(i) - goal_array.index(i)
            column = difference % 3
            line = difference / 3
            sum_distance = sum_distance + column + int(round(line))
        return sum_distance