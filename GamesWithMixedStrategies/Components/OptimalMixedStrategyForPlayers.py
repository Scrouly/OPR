def optimal_mixed_strategy_for_players(mat):
    if mat:
        x1 = round((mat[1][1] - mat[1][0]) /
                   ((mat[0][0] + mat[1][1]) - (mat[0][1] + mat[1][0])), 5)
        x2 = round((mat[0][0] - mat[0][1]) /
                   ((mat[0][0] + mat[1][1]) - (mat[0][1] + mat[1][0])), 5)
        y1 = round((mat[1][1] - mat[0][1]) /
                   ((mat[0][0] + mat[1][1]) - (mat[0][1] + mat[1][0])), 5)
        y2 = round((mat[0][0] - mat[1][0]) /
                   ((mat[0][0] + mat[1][1]) - (mat[0][1] + mat[1][0])), 5)
        sa = [x1, x2]
        sb = [y1, y2]

        return sa, sb
    else:
        return 0
