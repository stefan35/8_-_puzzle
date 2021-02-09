from main import goal_array
from heuristic_function import *
from moves import *
from operator import itemgetter
import copy
import time

#Funkcia ktora mi zistuje ci som uz spravne riesenie nasiel
def solutionCheck(vector, e):
    if vector[0] == goal_array:
        return e
    else:
        return 0

#A* algoritmus ktory vyuziva heuristicku funkciu na pocitanie zlych pozicii v hlavolame
#Tato funkcia taktiez vypise aj cestu ako sa k rieseniu dostala, kolko tahov bolo potrebnych a za aky cas sa to vyriesilo
def astar_wrong_position(array):
    start_time = time.time()
    nodes = []
    visited = []
    path = []
    move = 0
    solution = False
    visited.append(copy.copy(array))
    while not solution:
        if array.index(0) != 2 and array.index(0) != 5 and array.index(0) != 8:
            tmp_array = copy.copy(array)
            moveRight(tmp_array)
            if tmp_array != visited:
                visited.append(copy.copy(tmp_array))
                nodes.append((copy.copy(tmp_array), move + 1, position_number(tmp_array), move + 1 + position_number(tmp_array), copy.copy(array)))
        if array.index(0) != 0 and array.index(0) != 3 and array.index(0) != 6:
            tmp_array = copy.copy(array)
            moveLeft(tmp_array)
            if tmp_array != visited:
                visited.append(copy.copy(tmp_array))
                nodes.append((copy.copy(tmp_array), move + 1, position_number(tmp_array), move + 1 + position_number(tmp_array), copy.copy(array)))
        if array.index(0) != 0 and array.index(0) != 1 and array.index(0) != 2:
            tmp_array = copy.copy(array)
            moveUp(tmp_array)
            if tmp_array != visited:
                visited.append(copy.copy(tmp_array))
                nodes.append((copy.copy(tmp_array), move + 1, position_number(tmp_array), move + 1 + position_number(tmp_array), copy.copy(array)))
        if array.index(0) != 6 and array.index(0) != 7 and array.index(0) != 8:
            tmp_array = copy.copy(array)
            moveDown(tmp_array)
            if tmp_array != visited:
                visited.append(copy.copy(tmp_array))
                nodes.append((copy.copy(tmp_array), move + 1, position_number(tmp_array), move + 1 + position_number(tmp_array), copy.copy(array)))
        for i in range(len(nodes)):
            correct_array = solutionCheck(nodes[i], i)
            if correct_array != 0:
              print("Solution found")
              result = nodes[i]
              print(result[0], "Goal array")
              print("Need", result[1], "moves to solve")
              end_time = time.time()
              print("Executing time: ", end_time - start_time)
              solution = True
        end_time = time.time()
        if end_time-start_time > 15:
            print("End, program si executing too long")
            print("Executing time: ", end_time - start_time)
            return
        nodes = sorted(nodes, key=itemgetter(3))
        tmp = nodes.pop(0)
        path.append(copy.copy(tmp))
        find_path = path[len(path) - 1]
        i = 0
        if solution == True:
            print("Move: ", path[len(path) - 1])
            while solution == True:
                if find_path[4] == path[i][0] and find_path[1] == path[i][1] + 1:
                    find_path = path[i]
                    print("Move: ", find_path)
                    if find_path[1] == 1:
                        return
                    i = 0
                    continue
                i = i + 1
        array = tmp[0]
        move = tmp[1]

#A* algoritmus ktory vyuziva heuristicku funkciu na vypocet sucetu vzdialenosti jednotlivych policok od cielovej pozicie
#Tato funkcia taktiez vypise aj cestu ako sa k rieseniu dostala, kolko tahov bolo potrebnych a za aky cas sa to vyriesilo
def astar_count_moves(array):
    start_time = time.time()
    nodes = []
    visited = []
    path = []
    move = 0
    solution = False
    visited.append(array)
    while not solution:
        if array.index(0) != 2 and array.index(0) != 5 and array.index(0) != 8:
            tmp_array = copy.copy(array)
            moveRight(tmp_array)
            if tmp_array != visited:
                visited.append(copy.copy(tmp_array))
                nodes.append((copy.copy(tmp_array), move + 1, distance_number(tmp_array), move + 1 + distance_number(tmp_array), copy.copy(array)))
        if array.index(0) != 0 and array.index(0) != 3 and array.index(0) != 6:
            tmp_array = copy.copy(array)
            moveLeft(tmp_array)
            if tmp_array != visited:
                visited.append(copy.copy(tmp_array))
                nodes.append((copy.copy(tmp_array), move + 1, distance_number(tmp_array), move + 1 + distance_number(tmp_array), copy.copy(array)))
        if array.index(0) != 0 and array.index(0) != 1 and array.index(0) != 2:
            tmp_array = copy.copy(array)
            moveUp(tmp_array)
            if tmp_array != visited:
                visited.append(copy.copy(tmp_array))
                nodes.append((copy.copy(tmp_array), move + 1, distance_number(tmp_array), move + 1 + distance_number(tmp_array), copy.copy(array)))
        if array.index(0) != 6 and array.index(0) != 7 and array.index(0) != 8:
            tmp_array = copy.copy(array)
            moveDown(tmp_array)
            if tmp_array != visited:
                visited.append(copy.copy(tmp_array))
                nodes.append((copy.copy(tmp_array), move + 1, distance_number(tmp_array), move + 1 + distance_number(tmp_array), copy.copy(array)))
        for i in range(len(nodes)):
            correct_array = solutionCheck(nodes[i], i)
            if correct_array != 0:
                print("Solution found")
                result = nodes[i]
                print(result[0], "Goal array")
                print("Need", result[1], "moves to solve")
                end_time = time.time()
                print("Executing time: ", end_time - start_time)
                solution = True
        end_time = time.time()
        if end_time - start_time > 15:
            print("End, program si executing too long")
            print("Executing time: ", end_time - start_time)
            return
        nodes = sorted(nodes, key=itemgetter(3))
        tmp = nodes.pop(0)
        path.append(copy.copy(tmp))
        find_path = path[len(path) - 1]
        i = 0
        if solution == True:
            print("Move: ", path[len(path) - 1])
            while solution == True:
                if find_path[4] == path[i][0]:
                    find_path = path[i]
                    print("Move: ", find_path)
                    if find_path[1] == 1:
                        return
                    i = 0
                    continue
                i = i + 1
        array = tmp[0]
        move = tmp[1]