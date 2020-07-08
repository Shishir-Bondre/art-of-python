def rotate_left(array: list, rotations: int) -> list:
    # This takes 0(n) -> time and 0(n) -> space
    array_length = len(array)
    new_array = [0]*array_length

    for i in range(array_length):
        position = i-rotations
        if position < 0:
            position = array_length - abs(position)
        new_array[position] = array[i]
    return new_array


if __name__ == "__main__":
    print(rotate_left(array=[1, 2, 3, 4, 5], rotations=2))
