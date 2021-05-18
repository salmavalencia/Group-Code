
import unittest
from final import distribuirEstudiantes, getFileData, groupLayout, randomizeData
 
import numpy as np
import math
import sys  

class Test_getFilePath(unittest.TestCase):
    def test_algo(test):
        
        pathEstudiantes ="file1.txt"
        estudiantes = getFileData(pathEstudiantes)
        test.assertAlmostEqual(getFileData(pathEstudiantes), estudiantes)
        
    def test_algo2(test):
        pathTopics = "file2.txt"
        topics = getFileData(pathTopics)
        test.assertAlmostEqual(getFileData(pathTopics), topics)  

class Test_groupLayout(unittest.TestCase):
    def test_groupDistribution(test):
        estudiantes = 9
        grupos = float(6)
        if(estudiantes % grupos == 0):
            test.defaultTestResult(True)
        else:
            estudiantes_por_grupo = int(estudiantes / grupos)
            remanente = float(estudiantes - (estudiantes_por_grupo * grupos))
            posibles_combinaciones = (math.factorial(grupos))/(math.factorial(grupos - remanente)*math.factorial(remanente))
            probabilidad_combinacion = 1/posibles_combinaciones
            array = []
            estudiantes = int(estudiantes)
            grupos = int(grupos)
            array = groupLayout(estudiantes,grupos)
            count = 0
            ejecuciones = 10000
            for i in range(ejecuciones):
            
                if(groupLayout(estudiantes,grupos) == array):
                    count = count + 1
            
            test.assertFalse(count >= (probabilidad_combinacion * ejecuciones) + 30)

    def test_topicDistribution(test):
        temas = 9
        grupos = float(6)
        if(temas % grupos == 0):
            test.defaultTestResult(True)
        else:
            temas_por_grupo = int(temas / grupos)
            remanente = float(temas - (temas_por_grupo * grupos))
            posibles_combinaciones = (math.factorial(grupos))/(math.factorial(grupos - remanente)*math.factorial(remanente))
            probabilidad_combinacion = 1/posibles_combinaciones
            array = []
            temas = int(temas)
            grupos = int(grupos)
            array = groupLayout(temas,grupos)
            count = 0
            ejecuciones = 10000
            for i in range(ejecuciones):
            
                if(groupLayout(temas,grupos) == array):
                    count = count + 1
            
            test.assertFalse(count >= (probabilidad_combinacion * ejecuciones) + 20)

    

            
                
        
        

class Test_randomnizeData(unittest.TestCase):
    def test_uno(test):
        pathEstudiantes ="file1.txt"
        estudiantes = getFileData(pathEstudiantes)
        posibles_combinaciones = math.factorial(estudiantes)
        probabilidad_combinacion = 1/posibles_combinaciones
        array = []
        array = randomizeData(estudiantes,pathEstudiantes)
        count = 0
        ejecuciones = 1000
        for i in range(ejecuciones):
            print(i)
            if(randomizeData(estudiantes,pathEstudiantes) == array):
                count = count + 1
        test.assertFalse(count >= (probabilidad_combinacion * ejecuciones))
            
if __name__ == '__main__':
    unittest.main()
             

   
