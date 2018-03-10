#-------------------------------------------------------------------------------
# Name:        sudoku_stats
# Purpose:
#
# Author:      wilczews
#
# Created:     19/05/2014
# Copyright:   (c) wilczews 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sudoku

def is_filled(var):
    """
    Check if the sudoku matrix is completly resolved
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
    Returns : True or False, True : sudoku completly filled, False : not completly filled
    """
    for line in range(9):
        for row in range(9):
            if var[line][row] == 0:
                return False

    return True

def get_empty_cells_line(var,line):
    """
    To get the number of empty cells in the given line
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
        line : the nmber of the line which will be checked (number range : [0 -> 8])
    Returns : Number of empty cells in the given line (type = integer)
    """
    empty_cell_cnt = 0

    for row in range (9):
        if var[line][row] == 0:
            empty_cell_cnt += 1

    return empty_cell_cnt
def get_empty_cells_lines(var):
    """
    To get the numbers of empty cells in all lines
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
    Returns : The list of numbers of empty cells in all lines (type = list)
    """
    empty_cells = []
    for line in range(9):
        empty_cells.append(get_empty_cells_line(var,line))

    return empty_cells

def get_empty_cells_row(var,row):
    """
    To get the number of empty cells in the given row
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
        row : the nmber of the row which will be checked (number range : [0 -> 8])
    Returns : Number of empty cells in the given row (type = integer)
    """
    empty_cell_cnt = 0

    for line in range (9):
        if var[line][row] == 0:
            empty_cell_cnt += 1

    return empty_cell_cnt

def get_empty_cells_rows(var):
    """
    To get the numbers of empty cells in all rows
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
    Returns : The list of numbers of empty cells in all rows (type = list)
    """
    empty_cells = []
    for row in range(9):
        empty_cells.append(get_empty_cells_row(var,row))

    return empty_cells

def get_empty_cells_case(var,case):
    """
    To get the number of empty cells in the given case
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
        case : the nmber of the case which will be checked (number range : [0 -> 8])
    Returns : Number of empty cells in the given case (type = integer)
    Note :
        Case numbering :
        |0|1|2|
        |3|4|5|
        |6|7|8|
    """

    #get the line and row offsets to be in the right case
    line_offset,row_offset = sudoku.get_case_offsets(case)

    empty_cell_cnt = 0

    for line in range (3):
        for row in range(3):
            if var[line+line_offset][row+row_offset] == 0:
                empty_cell_cnt += 1

    return empty_cell_cnt

def get_empty_cells_cases(var):
    """
    To get the numbers of empty cells in all cases
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
    Returns : The list of numbers of empty cells in all cells (type = list)
    Note :
        Case numbering :
        |0|1|2|
        |3|4|5|
        |6|7|8|
    """
    empty_cells = []
    for case in range(9):
        empty_cells.append(get_empty_cells_case(var,case))

    return empty_cells



























