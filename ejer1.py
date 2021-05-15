import math
import numpy as np
import random
import sys

# path para estudiantes 'C:\\Users\\salma\\Desktop\\Codigo\\file1.txt'
# path para topics 'C:\\Users\\salma\\Desktop\\Codigo\\file2.txt'
def getStudents(pathEstudiantes):

    names = 0

    with open(pathEstudiantes,'r') as f:
        data = f.readlines()
        names = len(data)
    f.close()
    return names

def getTopics (pathTopics):

    cant_topicos = 0

    with open(pathTopics,'r') as f:
        data = f.readlines()
        cant_topicos = len(data)
        print(cant_topicos)
    f.close()
    return cant_topicos

    with open(pathTopics,'r') as f:
        data = f.readlines()
        names = len(data)
    f.close()
    return topics

def groupLayout(estudiantes, grupos):
    grupos_array = []
    if estudiantes % grupos == 0:
        valor = int(estudiantes / grupos)
        
        for i in range (0,grupos):
            grupos_array.append(valor)
       
    else:
        #print(estudiantes / grupos)
        min_grupo = int(estudiantes / grupos)
        
        #print(valor)
        
        remaining_students = estudiantes - (min_grupo * grupos)
        for i in range(grupos):
        #while estudiantes2 > -1:

            grupos_array.append(min_grupo)
            #print(estudiantes2)
        remaining_array = []

        while remaining_students > 0:
            random_value = random.randint(0, grupos - 1)
            try:
                remaining_array.index(random_value)
                print("valor en arreglo")
            
            except:
                grupos_array[random_value] += 1
                remaining_array.append(random_value)
                remaining_students -= 1
    
    return grupos_array

def randomizeData(estudiantes, pathEstudiantes):
    new_arr = []

    #randomiza los estudiantes y crea un array
    for i in range(estudiantes):
        newf=""
        check = False
        count = 0

        with open(pathEstudiantes,'r') as f:
            data = f.readlines()
            ran = random.randint(0, len(data) - 1)
        
            while True:
            
                if data[ran][0] != "*":
        
                    for line in data: 
                        if line == data[ran]:
                        
                            newf += "*" + line.strip() + "\n"
                            new_arr.append(line)
                            check = True
                        else:
                            newf += line.strip()+ "\n"
            
                if check == True:
                    break
        
                else:
                    ran = random.randint(0, len(data) - 1)
                    count = count + 1

        f.close()

        with open(pathEstudiantes,'w') as f:
            f.write(newf)
        f.close()

    newf2 =""

    with open(pathEstudiantes,'r') as f:
        data = f.readlines()
        for line in data:
            line = line.replace("*", "")
            newf2 +=  line.strip() + "\n"
    f.close()

    file1 = open(pathEstudiantes,"r+")
    file1.truncate(0)
    file1.close()

    with open(pathEstudiantes,'w') as f:
        f.write(newf2)
    f.close()

    return new_arr

def distribuirEstudiantes(estudiantes, cantidad_por_grupo):
    grupo_completo = [[] for i in range(len(cantidad_por_grupo))]
    
    for i, cantidad in enumerate(cantidad_por_grupo):
        for j in range(0, cantidad):
            grupo_completo[i].append(estudiantes.pop())

    return grupo_completo

    



def main():
    grupos = int(sys.argv[1])
    pathEstudiantes = sys.argv[2]
    pathTopics = sys.argv[3]

    estudiantes = getStudents(pathEstudiantes)
    topic = getTopics(pathTopics)

    cantidad_por_grupo = groupLayout(estudiantes, grupos)
    estudiantesReordenados = randomizeData(estudiantes, pathEstudiantes)
    estudiantes_asignados = distribuirEstudiantes(estudiantesReordenados, cantidad_por_grupo)
    print(cantidad_por_grupo)
    print(estudiantes_asignados)
    
    counter = 1
    for grupo in estudiantes_asignados:
        print("Grupo ", counter, ": ")
        for personas in grupo:
            print("\t", personas)
        print()
        counter += 1

    
main()

            


#grupos_array.pop()
