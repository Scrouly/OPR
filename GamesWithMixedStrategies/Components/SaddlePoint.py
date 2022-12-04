def find_saddle_point(mat):
    if mat:
        n = len(mat)
        k = 0
        for i in range(n):
            min_row = mat[i][0]
            col_ind = 0
            for j in range(1, n):
                if min_row > mat[i][j]:
                    min_row = mat[i][j]
                    col_ind = j
            for k in range(n):
                if min_row < mat[k][col_ind]:
                    break
                k += 1
            if k == n:
                print("Value of Saddle Point ", min_row)
                return True
        print("No Saddle Point")
        return False
    else:
        return 0
