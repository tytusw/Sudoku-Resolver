#-------------------------------------------------------------------------------
# Name:        sudoku_resolver
# Purpose:
#
# Author:      wilczews
#
# Created:     05/06/2014
# Copyright:   (c) wilczews 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import copy
import sudoku
import sudoku_stats

def deterministic_resolve(var):

    resolve_state = True
    while resolve_state == True:
        resolve_state = False
        for x_num in range(9):
            for num in range(1,10):
                if sudoku.fill_nbr_case(var,x_num,num) == True:
                    resolve_state = True
                if sudoku.fill_nbr_horizontal(var,x_num,num) == True:
                    resolve_state = True
                if sudoku.fill_nbr_vertical(var,x_num,num) == True:
                    resolve_state = True


##var_init = [[0,4,0,5,3,0,0,7,0],[7,0,9,0,0,2,0,0,8],[0,0,0,0,0,6,0,4,0],[0,5,7,0,0,0,0,0,3],[9,0,0,0,4,0,0,0,2],[6,0,0,0,0,0,1,5,0],[0,9,0,1,0,0,0,0,0],[3,0,0,8,0,0,4,0,6],[0,2,0,0,5,3,0,9,0]]
##var_init = [[0,6,0,4,0,9,0,8,0],[0,2,0,0,5,0,0,1,0],[0,0,8,0,0,0,5,0,0],[0,4,1,0,6,0,7,3,0],[6,0,0,0,0,0,0,0,4],[0,8,3,0,9,0,1,2,0],[0,0,9,0,0,0,4,0,0],[0,3,0,0,7,0,0,6,0],[0,5,0,8,0,2,0,9,0]]
##var_init = [[0,3,0,0,1,0,0,4,0],[2,0,0,0,0,0,0,0,3],[5,6,0,3,0,9,0,2,8],[7,0,0,0,6,0,0,0,2],[0,0,0,8,0,2,0,0,0],[8,0,0,0,4,0,0,0,5],[6,7,0,1,0,3,0,5,4],[3,0,0,0,0,0,0,0,6],[0,4,0,0,2,0,0,7,0]]

#facile
##var_init = [[3,0,9,0,0,0,6,1,0],[0,0,0,6,0,0,0,7,3],[0,0,0,0,2,8,0,0,4],[0,0,4,0,6,2,5,0,0],[0,7,8,0,4,0,1,2,0],[0,0,2,8,5,0,4,0,0],[4,0,0,5,9,0,0,0,0],[8,9,0,0,0,6,0,0,0],[0,5,3,0,0,0,2,0,1]]
#moyen
##→var_init = [[0,3,0,0,0,0,7,6,2],[0,0,0,3,9,0,0,0,0],[0,8,0,0,0,4,5,0,0],[0,0,0,0,7,0,6,0,0],[1,2,0,0,5,0,0,7,8],[0,0,4,0,3,0,0,0,0],[0,0,6,2,0,0,0,8,0],[0,0,0,0,6,1,0,0,0],[2,4,7,0,0,0,0,5,0]]
#difficile
##var_init = [[6,0,0,5,0,0,0,0,0],[1,5,0,0,0,0,0,9,8],[3,7,0,9,0,0,0,0,0],[0,0,6,3,7,0,4,0,9],[0,0,0,0,0,0,0,0,0],[4,0,5,0,2,9,8,0,0],[0,0,0,0,0,6,0,8,5],[8,2,0,0,0,0,0,1,6],[0,0,0,0,0,1,0,0,4]]
##the hardest
var_init = [[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]]
var1 = copy.deepcopy(var_init)

sudoku.display(var_init)
deterministic_resolve(var1)
sudoku.display(var1)

res = sudoku_stats.is_filled(var1)
print("sudoku filled-in ? --> ",res)

cnt = 1

while res == False:
    print("Iteration " + str(cnt))
    cnt = cnt + 1
    print("Empty cells in lines")
    print(sudoku_stats.get_empty_cells_lines(var1))
    print("Empty cells in rows")
    print(sudoku_stats.get_empty_cells_rows(var1))
    print("Empty cells in cases")
    print(sudoku_stats.get_empty_cells_cases(var1))
    
    new_number = int(input("Give a number between 1-9"))
    new_number_line = int(input("Give the line number 0-8"))
    new_number_row = int(input("Give the row number 0-8"))
    
    var_temp = copy.deepcopy(var1)
    
    var_temp[new_number_line][new_number_row] = new_number
    
    sudoku.display(var_temp)
    
    deterministic_resolve(var_temp)
    
    
    res = sudoku_stats.is_filled(var_temp)
    print("sudoku filled-in ? --> ",res)
    
    sudoku.display(var_temp)
    
    if res == False :
        var1 = copy.deepcopy(var_temp)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
