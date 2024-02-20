# coding: utf-8

class Grid:
    def __init__(self, length, width) -> None:
        self.__content = [[0 for _ in range(length)] for _ in range(width)]

    def __str__(self) -> str:
        res:str = ""
        for line in self.__content:
            for column in line:
                res += column + " "
            res += "\n"