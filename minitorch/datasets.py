import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N:int) -> list[tuple[float, float]]:
    """Creates a list of N (x,y) pairs, where x and y are uniform(0,1).

    Args:
        N (int): _

    Returns:
        list[tuple[float, float]]: list of (x,y) pairs

    """
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    """Class which holds 2d points with labels.
    
    Attributes:
        N (int): number of points
        X (List[Tuple[float, float]]): list of (x,y) coordinates for each point
        y (List[int]): list of integer labels for each point

    """

    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N: int) -> Graph:
    """Generates a graph of (x,y) pairs where label is +1 if x < 0.5, 0 otherwise.

    Args:
        N (int): number of points

    Returns:
        Graph: a graph with N points, where label for point i is +1 if X[i][0] < 0.5

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def diag(N: int) -> Graph:
    """Plots N points where y=1 iff sum of coordinates is < 0.5.

    Args:
        N (int): number of points

    Returns:
        Graph: a graph with N points, where X has (x1, x2) pairs and y has labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 + x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N: int) -> Graph:
    """Plots N points where y=1 iff x_1 < 0.2 or x_1 > 0.8
    

    Args:
        N (int): number of points

    Returns:
        Graph: a graph with N points, where X has (x1, x2) pairs and y has labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N: int) -> Graph:
    """Plots N points for xor function: y=1 iff (x_1<0.5 and x_2>0.5) OR (x_1 > 0.5 and x_2 < 0.5)

    Args:
        N (int): number of points

    Returns:
        Graph: a graph with N points, where X has (x1, x2) pairs and y has labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 and x_2 > 0.5 or x_1 > 0.5 and x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def circle(N: int) -> Graph:
    """Plots N points where decision boundary is a circle centered at (0.5, 0.5), radius sqrt(0.1); y=1 outside.

    Args:
        N (int): number of points

    Returns:
        Graph: a graph with N points, where X has (x1, x2) pairs and y has labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        x1, x2 = x_1 - 0.5, x_2 - 0.5
        y1 = 1 if x1 * x1 + x2 * x2 > 0.1 else 0
        y.append(y1)
    return Graph(N, X, y)


def spiral(N: int) -> Graph:
    """Plots N points where decision boundary is a circle centered at (0.5, 0.5), radius sqrt(0.1); y=1 outside.

    Args:
        N (int): number of points

    Returns:
        Graph: a graph with N points, where X has (x1, x2) pairs and y has labels.

    """
    def x(t: float) -> float:
        return t * math.cos(t) / 20.0

    def y(t: float) -> float:
        return t * math.sin(t) / 20.0

    X = [
        (x(10.0 * (float(i) / (N // 2))) + 0.5, y(10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    X = X + [
        (y(-10.0 * (float(i) / (N // 2))) + 0.5, x(-10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)


datasets = {
    "Simple": simple,
    "Diag": diag,
    "Split": split,
    "Xor": xor,
    "Circle": circle,
    "Spiral": spiral,
}
