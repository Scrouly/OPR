import pytest
import sys

from GamesWithMixedStrategies.Components.OptimalMixedStrategyForPlayers import optimal_mixed_strategy_for_players
from GamesWithMixedStrategies.Components.SaddlePoint import find_saddle_point
from GamesWithMixedStrategies.Components.ValueOfTheGame import value_of_the_game

sys.path.append("..Components")


@pytest.mark.parametrize(
    "matrix, result",
    [
        ([[2, 5, 6, 9], [8, 4, 12, 3], [6, 7, 3, 1], [12, 24, 2, 11]], False),
        ([[4, 16, 12], [2, 8, 14], [1, 3, 6]], True),
        ([[3, 8], [7, 4]], False),

    ]
)
def test_saddle_point(matrix, result):
    assert find_saddle_point(matrix) == result


@pytest.mark.parametrize(
    "matrix, result",
    [
        ([[5, 1], [3, 4]], 3.4),
        ([[2, -1], [-1, 0]], -0.25),
        ([[3, 8], [7, 4]], 5.5),

    ]
)
def test_value_of_the_game(matrix, result):
    assert value_of_the_game(matrix) == result


@pytest.mark.parametrize(
    "matrix, result",
    [
        ([[5, 1], [3, 4]], ([0.2, 0.8], [0.6, 0.4])),
        ([[2, -1], [-1, 0]], ([0.25, 0.75], [0.25, 0.75])),
        ([[3, 8], [7, 4]], ([0.375, 0.625], [0.5, 0.5])),

    ]
)
def test_optimal_mixed_strategy(matrix, result):
    assert optimal_mixed_strategy_for_players(matrix) == result
