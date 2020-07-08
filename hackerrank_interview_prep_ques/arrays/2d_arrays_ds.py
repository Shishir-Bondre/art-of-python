def hour_glass_sum(array: list) -> int:
    values = [sum(array[0][0:3]) + array[1][1] + sum(array[2][0:3]),
              sum(array[0][1:4]) + array[1][2] + sum(array[2][1:4]),
              sum(array[0][2:5]) + array[1][3] + sum(array[2][2:5]),
              sum(array[0][3:6]) + array[1][4] + sum(array[2][3:6]),
              sum(array[1][0:3]) + array[2][1] + sum(array[3][0:3]),
              sum(array[1][1:4]) + array[2][2] + sum(array[3][1:4]),
              sum(array[1][2:5]) + array[2][3] + sum(array[3][2:5]),
              sum(array[1][3:6]) + array[2][4] + sum(array[3][3:6]),
              sum(array[2][0:3]) + array[3][1] + sum(array[4][0:3]),
              sum(array[2][1:4]) + array[3][2] + sum(array[4][1:4]),
              sum(array[2][2:5]) + array[3][3] + sum(array[4][2:5]),
              sum(array[2][3:6]) + array[3][4] + sum(array[4][3:6]),
              sum(array[3][0:3]) + array[4][1] + sum(array[5][0:3]),
              sum(array[3][1:4]) + array[4][2] + sum(array[5][1:4]),
              sum(array[3][2:5]) + array[4][3] + sum(array[5][2:5]),
              sum(array[3][3:6]) + array[4][4] + sum(array[5][3:6])]

    # print(max(values))
    return max(values)


if __name__ == "__main__":
    hour_glass_sum(array=[[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])
