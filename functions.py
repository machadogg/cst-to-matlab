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

    # integer to count the number of plots
    k = 0

    # Brings the plots together for the CSV
    for i in range(len(lis)):

        if 'SZmin(1),Zmax(1)/abs,dB' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s21-te'
                lis[i] = ''
            else:
                lis[i] = 'f,s21-te'
            k += 1

        if 'SZmax(1),Zmax(1)/abs,dB' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s11-te'
                lis[i] = ''
            else:
                lis[i] = 'f,s11-te'
            k += 1

        if 'SZmax(1),Zmin(1)/abs,dB' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s12-te'
                lis[i] = ''
            else:
                lis[i] = 'f,s12-te'
            k += 1

        if 'SZmin(1),Zmin(1)/abs,dB' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s22-te'
                lis[i] = ''
            else:
                lis[i] = 'f,s22-te'
            k += 1

        if 'SZmin(2),Zmax(2)/abs,dB' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s21-tm'
                lis[i] = ''
            else:
                lis[i] = 'f,s21-tm'
            k += 1

        if 'SZmax(2),Zmax(2)/abs,dB' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s11-tm'
                lis[i] = ''
            else:
                lis[i] = 'f,s11-tm'
            k += 1

        if 'SZmax(2),Zmin(2)/abs,dB' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s12-tm'
                lis[i] = ''
            else:
                lis[i] = 'f,s12-tm'
            k += 1

        if 'SZmin(2),Zmin(2)/abs,dB' in lis[i]:
            if i > 0:
                lis[0] = lis[0] + ',f,s22-tm'
                lis[i] = ''
            else:
                lis[i] = 'f,s22-tm'
            k += 1

        if i > 0:
            lis[i] = ','.join(lis[i].split())

    # lis = list(filter(None, lis))
    # for i in range(len(lis)):

    #     if lis[i] == '':
    #         del lis[i]

    del lis[len(lis) - 1]
    print(k)
    return lis


def adjusting(flis):

    list_empties = []

    for n in range(len(flis)):

        if n > 1:

            if flis[n] == '' or flis[n] == '\n':

                list_empties.append(str(n))

    print(list_empties)
