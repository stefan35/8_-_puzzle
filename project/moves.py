#Funkcie na definovanie pohybu konkretnym smerom

def moveDown(array):
    tmp = array.index(0) + 3
    zero = array[array.index(0)]
    array[array.index(0)] = array[tmp]
    array[tmp] = zero


def moveLeft(array):
    tmp = array.index(0) - 1
    zero = array[array.index(0)]
    array[array.index(0)] = array[tmp]
    array[tmp] = zero


def moveUp(array):
    tmp = array.index(0) - 3
    zero = array[array.index(0)]
    array[array.index(0)] = array[tmp]
    array[tmp] = zero


def moveRight(array):
    tmp = array.index(0) + 1
    zero = array[array.index(0)]
    array[array.index(0)] = array[tmp]
    array[tmp] = zero