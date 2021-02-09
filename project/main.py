from a_star import *

goal_array = [1, 2, 3, 4, 0, 5, 6, 7, 8]

#Vo funkcii main uzivatel zadava obtiaznost vstupu aj vyber heuristiky
def main():
    array = []
    print("Select difficulty of input array:")
    print("Press 1 for easy difficulty.")
    print("Press 2 for medium difficulty.")
    print("Press 3 for hard difficulty.")
    print("Press 4 for unsolvable.")
    selected = input()
    if selected == '1':
        array = [1, 5, 2, 0, 4, 3, 6, 7, 8]
    if selected == '2':
        array = [0, 5, 2, 1, 4, 3, 6, 7, 8]
    if selected == '3':
        array = [1, 3, 4, 6, 2, 0, 5, 7, 8]
    if selected == '4':
        array = [7, 6, 5, 4, 2, 3, 8, 0, 1]
    print("Select heuristic you want to use: ")
    print("Press 1 for use wrong number position")
    print("Press 2 for use count moves of number to correct position")
    print("Press 3 for compare time in both heuristic function")
    selected = input()
    if selected == '1':
        astar_wrong_position(array)
    if selected == '2':
        astar_count_moves(array)
    if selected == '3':
        print("Function which count numbers on wrong position")
        astar_wrong_position(array)
        print("Function which count moves to correct position")
        astar_count_moves(array)

if __name__ == "__main__":
    main()
