def printmatrix(mat):
    for i in mat:
        for j in i:
            print(j, end='  ')
        print()


mat = [0, 0, 1, 0, 0, 1], [1, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 0, 1, 1,
                                                                                                           0, 0]
printmatrix(mat)
