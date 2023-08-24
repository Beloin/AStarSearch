from src.astar import a_star
from src.mosaic import MosaicValuedStates

if __name__ == "__main__":
    # mosaic = MosaicValuedStates([2, 8, 3, 1, 6, 4, 7, 0, 5])
    # mosaic = MosaicValuedStates([7, 2, 4, 5, 0, 6, 8, 3, 1])
    # mosaic = MosaicValuedStates([1, 2, 3, 4, 5, 6, 7, 8, 0])

    #   | 1 | 2 | 3 |
    #   | 4 | 5 | 6 |
    #   | 0 | 7 | 8 |
    mosaic = MosaicValuedStates([1, 2, 3, 4, 5, 6, 0, 7, 8])
    # mosaic = MosaicValuedStates([1, 2, 3, 4, 5, 0, 6, 7, 8])
    star, code = a_star(mosaic, 0)
    print(star)

    if not code:
        translate = mosaic.translate(star)
        print(translate)
