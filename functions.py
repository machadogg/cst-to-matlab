import inspect

# just for debuging purposes


def printdeb():

    line = inspect.currentframe().f_back.f_lineno
    print("Debug pass. Line ", line)

# deletes the dashes from CST


def del_dashes(lista):

    i = 0
    while i < len(lista):  # finds the dashes and delete them
        if '--' in lista[i]:
            del lista[i]
        i += 1
    return lista

# adjust the structure to prepare the final CSV file


def define_Sparam(lis):

    k = 0

    # Brings the plots together for the CSV
    # The CST file structure is
    # Frequency        S1,1
    # F1               v1
    # F2               v2
    # Frequency        S2,1
    # F1               v3
    # F2               v4
    # but we need it to be like this
    # Frequency,S11,Frequency,S21
    # F1,v1,F1,v3
    # F2,v2,F2,v4
    # this 'for' loop detects whether we are reading
    # the results from a floquet port (SZmin(1),Zmax(1)) - converts to s11-te or tm, depending on the index
    # or from a waveguide/discrete port (S1,1) - converts to s11, or s12, or s22 or s21
    for i in range(len(lis)):

        if 'SZmin(1),Zmax(1)' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s21-te'
                lis[i] = ''
            else:
                lis[i] = 'f,s21-te'
            k += 1

        if 'SZmax(1),Zmax(1)' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s11-te'
                lis[i] = ''
            else:
                lis[i] = 'f,s11-te'
            k += 1

        if 'SZmax(1),Zmin(1)' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s12-te'
                lis[i] = ''
            else:
                lis[i] = 'f,s12-te'
            k += 1

        if 'SZmin(1),Zmin(1)' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s22-te'
                lis[i] = ''
            else:
                lis[i] = 'f,s22-te'
            k += 1

        if 'SZmin(2),Zmax(2)' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s21-tm'
                lis[i] = ''
            else:
                lis[i] = 'f,s21-tm'
            k += 1

        if 'SZmax(2),Zmax(2)' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s11-tm'
                lis[i] = ''
            else:
                lis[i] = 'f,s11-tm'
            k += 1

        if 'SZmax(2),Zmin(2)' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s12-tm'
                lis[i] = ''
            else:
                lis[i] = 'f,s12-tm'
            k += 1

        if 'SZmin(2),Zmin(2)' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s22-tm'
                lis[i] = ''
            else:
                lis[i] = 'f,s22-tm'
            k += 1

        if 'S1,1' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s11'
                lis[i] = ''
            else:
                lis[i] = 'f,s11'
            k += 1
        if 'S2,1' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s21'
                lis[i] = ''
            else:
                lis[i] = 'f,s21'
            k += 1
        if 'S1,2' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s12'
                lis[i] = ''
            else:
                lis[i] = 'f,s12'
            k += 1
        if 'S2,2' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s22'
                lis[i] = ''
            else:
                lis[i] = 'f,s22'
            k += 1

        # Eliminate the white spaces and puts a comma for the CSV
        if i > 0:
            lis[i] = ','.join(lis[i].split())

    # lis = list(filter(None, lis))

    # Clears the double blank lines, leaving one. We will need it later!
    for j in range(k):
        if i > 1:

            for i in range(len(lis)):

                if lis[i] == '' and lis[i - 1] == '':
                    del lis[i]
                    break

    del lis[len(lis) - 1]

    lis = adjusting(lis, k - 1)
    print("k = ", k)
    return lis


def adjusting(flis, r):

    list_empties = []
    soma = []

    # Creates a list of the empty lines as they separate the plots

    for n in range(len(flis)):

        if n > 1:

            if flis[n] == '':

                list_empties.append(n)
    list_empties.append(len(flis))

    print(list_empties)

    # Creates a list with the number of data to be appended

    for n in range(len(list_empties)):
        if n > 0:
            soma.append(list_empties[n] - list_empties[n - 1])

    print(soma)

    for n in range(r):

        for j in range(1, soma[n]):
            flis[j] = flis[j] + ',' + flis[j + list_empties[n]]

    for n in range(list_empties[0], len(flis)):

        flis[n] = ''

    flis = list(filter(None, flis))

    return flis
