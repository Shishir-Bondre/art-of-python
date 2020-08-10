def swap(array, i, j):
    if i >= len(array)-1:
        print(array)
        return
    array[i], array[j] = array[j], array[i]
    swap(array, i+1, j+1)

def permutations(array):
    # for i in range(len(array)):
    swap(array, i=0, j=0)

if __name__ == "__main__":
    print(permutations(array=[1,2,3]))