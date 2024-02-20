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
    
    def is_in_grid(self, x, y):
        return (0 <= x and x < self.__width) and (0 <= y and y < self.__length)

    def step(self):        
        for x in range(self.__width):
            for y in range(self.__length):
                neighboors_count:int = 0
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if self.is_in_grid(x+dx, y+dy):
                            if self.__content[x+dx][y+dy]:
                                neighboors_count += 1
                # First and third rules
                if neighboors_count < 2 or neighboors_count > 3: 
                    print("hey!")
                    self.__content[x][y] = 0
                # Second and fourth rules
                else:
                    print("nop")
                    self.__content[x][y] = 1
