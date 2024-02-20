#!/bin/python
# coding: utf-8

import os
import time
from grid.Grid import Grid

def flush():
    """
    Clean the term
    """
    if os.name == "nt": # for Windows users
        os.system("cls")
    else: # Unix-like OS
        os.system("clear")

if __name__ == "__main__":
    grid = Grid(10,10)
    for _ in range(10):
        flush()
        print(grid)
        grid.step()
        time.sleep(0.5)
        