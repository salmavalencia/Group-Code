import sys

print(str(sys.argv)) 

grupos = sys.argv[1]
pathEstudiantes = sys.argv[2]

#'C:\\Users\\salma\\Desktop\\Codigo\\file1.txt'

with open(pathEstudiantes,'r') as f:
        data = f.readlines()
        names = len(data)
        print(names)
f.close()

print("grupos ", grupos)
print("path estudiante ", pathEstudiantes)