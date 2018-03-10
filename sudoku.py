#! /usr/bin/python

def display(var):
    print ("-----------------------")
    for i in range(9):
        print ("|{:d}|{:d}|{:d}| |{:d}|{:d}|{:d}| |{:d}|{:d}|{:d}|".format(var[i][0],var[i][1],var[i][2],var[i][3],var[i][4],var[i][5],var[i][6],var[i][7],var[i][8]))
        #print ("|%d|%d|%d| |%d|%d|%d| |%d|%d|%d|")%(var[i][0],var[i][1],var[i][2],var[i][3],var[i][4],var[i][5],var[i][6],var[i][7],var[i][8])
        #print ("%s" % var[0][0])
        if (i+1)%3 == 0 and (i+1)!=9:
            print (" ")
    print ("-----------------------")

def check_nbr_vertical(var,row,nbr):
	"""
    check if nbr is already in this row
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
        row : is the row which will be checked (number range : [0 -> 8])
        nbr : is the numbre which have to check the whole row (number range : [1 -> 9])
    Returns : True or False
    """
	for line in range(9):
		if var[line][row] == nbr:
			return True
	return False

def check_nbr_horizontal(var,line,nbr):
	"""
    check if nbr is already in this line
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
        line : is the line which will be checked (number range : [0 -> 8])
        nbr : is the numbre which have to check the whole line (number range : [1 -> 9])
    Returns : True or False
    """
	for row in range(9):
		if var[line][row] == nbr:
			return True
	return False

def check_nbr_case(var,case,nbr):
    """
    Check if nbr is already in this case
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
        case : is the case which will be checked (number range : [0 -> 8])
        nbr : is the numbre which have to check the whole line (number range : [1 -> 9])
    Returns : True or False
    Note :
        Case numbering :
        |0|1|2|
        |3|4|5|
        |6|7|8|
    """
    #get the line and row offsets to be in the right case
    line_offset,row_offset = get_case_offsets(case)

    for line in range(3):
        for row in range(3):
            if var[line_offset + line][row_offset + row] == nbr:
                return True
    return False

def get_case_offsets(case):
    """
    To get the offsets of the given case number
    Params :
        case : is the case which will be checked (number range : [0 -> 8])
    Returns : line offset (values : 0,3 or 6), row offset (values : 0,3 or 6),
    Note :
        Case numbering :
        |0|1|2|
        |3|4|5|
        |6|7|8|
    """
    i_offset = 0
    j_offset = 0

    if case == 0 :
        i_offset = 0
        j_offset = 0
    elif case == 1 :
        i_offset = 0
        j_offset = 3
    elif case == 2 :
        i_offset = 0
        j_offset = 6
    elif case == 3 :
        i_offset = 3
        j_offset = 0
    elif case == 4 :
        i_offset = 3
        j_offset = 3
    elif case == 5 :
        i_offset = 3
        j_offset = 6
    elif case == 6 :
        i_offset = 6
        j_offset = 0
    elif case == 7 :
        i_offset = 6
        j_offset = 3
    elif case == 8 :
        i_offset = 6
        j_offset = 6
    return i_offset,j_offset

def get_case_number(line,row):
    """
    To get the case number of the given line and row offsets
    Params :
    line : is the line number (number range : [0 -> 8])
    row : is the row number (number range : [0 -> 8])
    Returns : case number
    Note :
    Case numbering :
    |0|1|2|
    |3|4|5|
    |6|7|8|
    """
    if line < 3 :
        if row < 3 :
            case_number = 0
        elif row < 6 :
            case_number = 1
        else :
            case_number = 2
    elif line < 6 :
        if row < 3 :
            case_number = 3
        elif row < 6 :
            case_number = 4
        else :
            case_number = 5
    else :
        if row < 3 :
            case_number = 6
        elif row < 6 :
            case_number = 7
        else :
            case_number = 8

    return case_number

def is_caseline_full(var,case,relatif_line):
    """
    Check if the line (dim=1x3) of the given case is already completly filled with numbers
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
        case : is the case which will be checked (number range : [0 -> 8])
        relatif_line : is the line of the case which will be checked !!!! (number range : [0 -> 2]) !!!!
    Returns : True or False , True = the case line is full , False = the case line is not completly full
    Note :
        Case numbering :
        |0|1|2|
        |3|4|5|
        |6|7|8|
    """
    #get the line and row offsets to be in the right case
    line_offset,row_offset = get_case_offsets(case)

    for row in range(3):
        if var[line_offset + relatif_line][row_offset + row] == 0 :
            return False

    return True

def is_caserow_full(var,case,relatif_row):
    """
    Check if the row ((dim=3x1) of the given case is already completly filled with numbers
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
        case : is the case which will be checked (number range : [0 -> 8])
        relatif_row : is the row of the case which will be checked !!!! (number range : [0 -> 2]) !!!!
    Returns : True or False , True = the case row is full , False = the case row is not completly full
    Note :
        Case numbering :
        |0|1|2|
        |3|4|5|
        |6|7|8|
    """
    #get the line and row offsets to be in the right case
    line_offset,row_offset = get_case_offsets(case)

    for line in range(3):
        if var[line_offset + line][row_offset + relatif_row] == 0 :
            return False

    return True

def compare(var1,var2):
    """
    Compare var1 to var2 and print line and row when difference
    Params :
        var1 : is the whole sudoku matrix (dim = 9 x 9)
        var2 : is the whole sudoku matrix (dim = 9 x 9)
    Returns : no returns
    Note :
        prints in consol the line and row number when different
        prints at the end the number changed values
    """
    diff_cnt = 0
    print("Comparison Start :")
    for line in range(9):
        for row in range(9):
            if var1[line][row] != var2[line][row]:
                print("line : ",line," , row : ",row," are differente => new value : ",var2[line][row])
                diff_cnt += 1
    print(diff_cnt," numbers are different")
    print("End of comparison")

def fill_nbr_case(var,case,nbr):
    """
    Try to fill-in the sudoku matrix with the given number (nbr) in params but only in case mode
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
        case : is the case which will be filled-in (number range : [0 -> 8])
        nbr : is the numbre which the algo try to fill-in the cases (number range : [1 -> 9])
    Returns : True or False , True = a number has been placed , False = no number has been placed
    Note :
        Case numbering :
        |0|1|2|
        |3|4|5|
        |6|7|8|
    """
    #set the offsets for case scanning
    line_offset,row_offset = get_case_offsets(case)
    #si la valeur est deja dans cette case on resort de cette fonction
    if check_nbr_case(var,case,nbr) == True :
        #print(nbr," est deja dans cette case")
        return False

    for line in range(3):
        for row in range(3):
            line_cnt = 0
            row_cnt = 0
            #print("check ligne : ",i+line_offset," row : ",j+row_offset)
            #je verifie si la case est libre
            if var[line_offset + line][row_offset + row] == 0 :
                #verif vertical  de la case cible (si il y est deja sert   placer existe bien dans les autres lignes et colonnes
                        for k in range(3):
                            #check horizontal si nombre deja la ou si ligne de cette case est pleine
                            if k != line:
                                if check_nbr_horizontal(var,line_offset + k,nbr) == True or is_caseline_full(var,case,k) == True :
                                    line_cnt += 1
                            #check vertical si nombre deja la ou si ligne de cette case pleine
                            if k != row:
                                if check_nbr_vertical(var,row_offset + k,nbr) == True or is_caserow_full(var,case,k) == True:
                                    row_cnt += 1
                        #verifie si les deux autres cases (verticalement) ne sont pas plein
                        if line_cnt != 2 and row_cnt == 2 and var[line_offset + ((line + 1)%3)][row_offset + row] != 0 and var[line_offset + ((line + 2)%3)][row_offset + row] != 0:
                            line_cnt = 2
                        #verifie si les deux autres cases (horizontalement) ne sont pas plein
                        if line_cnt == 2 and row_cnt != 2 and var[line_offset + line][row_offset + ((row + 1)%3)] != 0 and var[line_offset + line][row_offset + ((row + 2)%3)] != 0:
                            row_cnt = 2

                        #verification si line_cnt = 2 et row_cnt = 2
                        if line_cnt == 2 and row_cnt == 2:
                            var[line_offset + line][row_offset + row] = nbr
                            return True

    # si on ne sais pas mettre la valeur on retourne false
    return False

def fill_nbr_horizontal(var,line_tf,nbr):
    """
    Try to fill-in the sudoku matrix with the given number (nbr) in params but only in horizontal mode
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
        line_tf : is the line which will be filled-in (number range : [0 -> 8])
        nbr : is the numbre which the algo try to fill-in the cases (number range : [1 -> 9])
    Returns : True or False , True = a number has been placed , False = no number has been placed
    """
    #check if the number isn't already in this line
    if check_nbr_horizontal(var,line_tf,nbr) == True:
        return False

    row = 0
    while row < 9:
        row_cnt = 0
        case_row = get_case_number(line_tf,row)
        if check_nbr_case(var,case_row,nbr) == True:
            row += 3
            continue
        #check if this place is empty and the number dosen't existe in this row
        if var[line_tf][row] == 0 and check_nbr_vertical(var,row,nbr) == False:
            #check vertical in the other rows if the number existe
            k = 0
            while k < 9:
                case_k = get_case_number(line_tf,k)
                if check_nbr_case(var,case_k,nbr) == True:
                    k += 3
                    if case_k != case_row :
                        row_cnt += 3
                    else:
                        row_cnt += 2
                    continue

                if k != row:
                    if check_nbr_vertical(var,k,nbr) == True or var[line_tf][k] != 0:
                        row_cnt += 1
                k +=1

            if row_cnt == 8:
                var[line_tf][row] = nbr
                return True
        row +=1

    return False


def fill_nbr_vertical(var,row_tf,nbr):
    """
    Try to fill-in the sudoku matrix with the given number (nbr) in params but only in horizontal mode
    Params :
        var : is the whole sudoku matrix (dim = 9 x 9)
        line_tf : is the line which will be filled-in (number range : [0 -> 8])
        nbr : is the numbre which the algo try to fill-in the cases (number range : [1 -> 9])
    Returns : True or False , True = a number has been placed , False = no number has been placed
    """
    #check if the number isn't already in this row
    if check_nbr_vertical(var,row_tf,nbr) == True:
        return False

    line = 0
    while line < 9:
        line_cnt = 0
        case_line = get_case_number(line,row_tf)
        if check_nbr_case(var,case_line,nbr) == True:
            line += 3
            continue
        #check if this place is empty and the number dosen't existe in this line
        if var[line][row_tf] == 0 and check_nbr_horizontal(var,line,nbr) == False:
            #check vertical in the other rows if the number existe
            k = 0
            while k < 9:
                case_k = get_case_number(k,row_tf)
                if check_nbr_case(var,case_k,nbr) == True:
                    k += 3
                    if case_k != case_line :
                        line_cnt += 3
                    else:
                        line_cnt += 2
                    continue
                if k != line:
                    if check_nbr_horizontal(var,k,nbr) == True or var[k][row_tf] != 0:
                        line_cnt += 1
                k +=1

            if line_cnt == 8:
                var[line][row_tf] = nbr
                return True
        line +=1

    return False


