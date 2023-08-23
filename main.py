from src.astar import a_star
from src.mosaic import MosaicValuedStates

if __name__ == "__main__":
    mosaic = MosaicValuedStates([2, 8, 3, 1, 6, 4, 7, 0, 5])
    # mosaic = MosaicValuedStates([1, 2, 3, 4, 5, 6, 7, 8, 0])
    star, code = a_star(mosaic, 0)
    print(star)
