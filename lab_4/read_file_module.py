from lab_4.cube_module import Cube

def read_file(file_name:str):
    cube=[]
    f= open("lab_4/figure.txt")
    point=[]
    if f.readline()[:-1]=='cube':
        str=f.readline()
        for i in range(4):
            space=str.find(' ')
            cube.append(int(str[:space]))
            str=str[space+1:]
    else:
        for str in f:
            sym=0
            point=[]
            for i in range(3):
                space=str[sym:].find(' ')
                point.append(int(str[sym:][:space]))
                sym+=space+1
            cube.append(point)
    '''while sym<len(str):
        space=str[sym:].find(' ')
        print(space)
        point.append(int(str[sym:space]))
        sym=space+1
    cube.append(point)'''
    f.close()
    a=Cube(cube)
    return a