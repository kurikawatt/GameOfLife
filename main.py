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
    grid = Grid(20,20)
    while True:
        flush()
        print(grid)
        grid.step()
        time.sleep(1)
        