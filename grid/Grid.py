# coding: utf-8

import random as rdm

class Grid:
    def __init__(self, length, width) -> None:
        self.__length = length
        self.__width = width
        self.__content = [
            [rdm.randint(0,1) # to randomly choose which cells live at begining 
             for _ in range(length)] 
            for _ in range(width)
        ]

    def __str__(self) -> str:
        res:str = ""
        for line in self.__content:
            for column in line:
                res +=  f"{column} "
            res += "\n"
        return res