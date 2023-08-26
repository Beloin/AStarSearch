from src.astar import a_star
from src.mosaic import MosaicValuedStates
import random


def test_mosaic(mosaic):
    star, code = a_star(mosaic, 0)
    print(star)

    if not code:
        translate = mosaic.translate(star)
        print(translate)


def main_01():
    #   | 1 | 2 | 3 |
    #   | 4 | 5 | 6 |
    #   | 0 | 7 | 8 |
    mosaic = MosaicValuedStates([1, 2, 3, 4, 5, 6, 0, 7, 8])
    test_mosaic(mosaic)

    # TODO: TOO SLOW
    #   | 1 | 2 | 3 |
    #   | 7 | 5 | 6 |
    #   | 4 | 8 | 0 |
    # mosaic = MosaicValuedStates([1, 2, 3, 7, 5, 6, 4, 8, 0])
    # test_mosaic(mosaic)

    #   | 1 | 2 | 3 |
    #   | 4 | 8 | 5 |
    #   | 0 | 7 | 6 |
    mosaic = MosaicValuedStates([1, 2, 3, 4, 8, 5, 0, 7, 6])
    test_mosaic(mosaic)

    # OK:
    #   | 1 | 6 | 2 |
    #   | 7 | 0 | 5 |
    #   | 8 | 4 | 3 |
    #   SEE: https://deniz.co/8-puzzle-solver/
    mosaic = MosaicValuedStates([1, 6, 2, 7, 0, 5, 8, 4, 3])
    test_mosaic(mosaic)

    # OK:
    #   | 1 | 2 | 3 |
    #   | 0 | 4 | 6 |
    #   | 7 | 5 | 8 |
    mosaic = MosaicValuedStates([1, 2, 3, 0, 4, 6, 7, 5, 8])
    test_mosaic(mosaic)

    # OK:
    #   | 4 | 1 | 5 |
    #   | 7 | 3 | 2 |
    #   | 0 | 8 | 6 |
    #   States: [0, 2, 4, 5, 6, 11, 22, 43, 47, 51, 54]
    mosaic = MosaicValuedStates([4, 1, 5, 7, 3, 2, 0, 8, 6])
    test_mosaic(mosaic)


def main_02():
    mosaic = MosaicValuedStates()
    test_mosaic(mosaic)


if __name__ == "__main__":
    # main_01()
    main_02()
