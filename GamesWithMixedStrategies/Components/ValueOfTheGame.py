def value_of_the_game(mat):
    if mat:
        v = (mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]) / \
            ((mat[0][0] + mat[1][1]) - (mat[1][0] + mat[0][1]))
        round_v = round(v, 5)
        return round_v
    else:
        return 0
