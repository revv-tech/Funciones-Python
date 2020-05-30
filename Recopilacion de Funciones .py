# RECOPILACION DE FUNCIONES

# Cuenta la cantidad de digitos de un numero
def largo(num):

    i = 0

    if num == 0:

        return 0

    while num != 0:

        num = num//10
        i += 1

    return i

# Suma todos los digitos de una lista en un solo numero
def suma_Lista(lista):

    total = 0

    if lista == []:

        return 0

    else:

        while lista != []:

            total += lista[0]
            lista = lista[1:]

        return total

# Recibe un numero y lo convierte a lista
def num_a_lista(num):

    lista = []
    digito = 0

    if num1 == 0:

        return [0]

    while num != 0:

        digito = num%10

        lista = [digito] + lista

        num = num//10

    return lista

# Realiza la sumatoria hasta el numero "num" que reciba
def sumatoria(num):

    if num == 0:

        return 0

    else:
        i = 0
        suma = 0

        while i <= num: # Mientras el i sea menor que el parametro final

            suma = suma + i # Se agrega el i a la suma total

            i  = i + 1 # i se acerca al parametro final

        return suma

# Calcula el largo de una lista
def largo_Lista(lista):

    if lista == []:

        return 0

    else:

        cont = 0
        while lista != []:
            

            cont += 1
            lista = lista[1:]

        return cont


# Realiza el factorial del numero "n" recibido
def factorial (n):

    contador = 0
    total = 1
    final = n

    if n == 0:

        return 1

    while n != 0:

        total = total * n
        n -=1

    return total


# Funcion que me indica si el n es un numero primo o no
def primo (n):

    if n == 0:

        return False

    elif n == 1:
        
        return False

    # No tomo en cuenta al 1 ni al n porque esos numeros siempre son divisores
    # sean primos o no
    for i in range(2, n-1):


        if n%i == 0:

            return False

    return True

# Funcion que muestra como se consiguen los digitos de un numeero
# de derecha a izquierda destruyendo el numero original
def rec_der_des(num):

    digito = 0

    while num != 0:

        digito = num%10

        print (digito)

        num = num//10

# Funcion que muestra como se consiguen los digitos de un numeero
# de derecha a izquierda sin destruir el numero original
def rec_der_no(num):

    digito = 0
    exp = 0   

    while exp < largo(num):

        digito = num//(10**exp)%10
        exp += 1

        print (digito)
        print (num)


# Funcion que muestra como se consiguen los digitos de un numeero
# de izquierda a derecha destruyendo el numero original
def rec_izq_des(num):

    digito = 0
    exp = largo(num)-1

    while num != 0:

        digito = num//(10**exp)
        

        print (digito)

        num = num%(10**exp)
        exp -= 1


# Funcion que muestra como se consiguen los digitos de un numeero
# de izquierda a derecha sin destruir el numero original
def rec_izq_no(num):

    digito = 0
    exp = largo(num)-1

    while exp >= 0:

        digito = num//(10**exp)%10

        print (digito)
        exp -= 1


# Suprime el elemento de una lista
def delete(lista, elemento):

    listaN = []

    for i in range(0, largo_Lista(lista)):

        if lista[i] == elemento:

            listaN += lista[:i]
            listaN += lista[i+1:]
            return listaN

    print ("No se encontró el elemento")


# Ordenamiento de burbuja
def bubbleSort(lista):

    for i in range(1, largo_Lista(lista)):

        for j in range(0, largo_Lista(lista)-1):

            if (lista[j]>lista[j+1]):

                k = lista[j+1]

                lista[j+1] = lista[j]

                lista[j] = k

    print (lista)


# Ordenamiento por inserción
def insert(lista):

    for i in range(1, largo_Lista(lista)):

        v = lista[i]

        j = i-1

        while j>=0 and lista[j]>v:

            lista[j+1] = lista[j]

            j = j-1


        lista[j+1] = v

    print(lista)

# Ordenamiento por seleccion
def selection (lista):

    for i in range(0, len(lista)-1):

        minimo = i

        for j in range(i+1, len(lista)):

            if lista[minimo] > lista[j]:

                minimo = j

        aux = lista[minimo]
        lista[minimo] = lista[i]
        lista[i] = aux

    print(lista)
#Conjuntos
def conjunto(lista):
    largo=0
    pos=0
    while largo<len(lista):
        while pos<len(lista):
            if largo!=pos:
                if lista[pos]==lista[largo]:
                    return False
                else:
                    pos+=1
            else:
                pos+=1
        pos=0
        largo+=1
    return True

def union(lista1,lista2):
    if conjunto(lista1)==True and conjunto(lista2)==True:
        while lista2!=[]:
            if not(lista2[0] in lista1):
                lista1=lista1+[lista2[0]]
            lista2=lista2[1:]
                     
        return lista1
    else:
        return "Debe ingresar conjuntos"

def interseccion(lista1,lista2):
    if conjunto(lista1)==True and conjunto(lista2)==True:
        listaNueva=[]
        while lista2!=[]:
            if lista2[0] in lista1:
                if lista2[0] not in listaNueva:
                    listaNueva+=[lista2[0]]
            lista2=lista2[1:]
        return listaNueva
    else:
        return "Deben ser conjuntos"

#Matrices

#Verifica si es una matriz
def validacion(matriz):
    a=0
    b=0
    if matriz==[]:
        return False
    elif matriz[0] == [] and matriz[1] == []:
        return "La matriz no es valida"
    else:
        for i in range (len(matriz)):
            if matriz==[]:
                a=1
            elif matriz[0]==[]:
                a=1
            elif len(matriz[0])!=len(matriz[1]):
                matriz=matriz+[matriz[0]]
                print(matriz)
                matriz=matriz[1:]
                print(matriz)
                a=1
            matriz=matriz+[matriz[0]]
            matriz=matriz[1:]
    if a==b:
        return True
    else:
        return False
#Suma Matrices
def sumaM( ma1,ma2):
    if validacion(ma1)!=validacion(ma2) :
        print ("matrices no validas")
    else:
        filas=len(ma1)
        columnas=len(ma1[0])
        for i in range (filas):
            for j in range (columnas):
                ma1[i][j] =ma1[i][j]+ ma2[i][j]
        print( ma1)

#Crea Matriz
def creamatriz(filas, columnas):
    matriz=[]
    for i in range(0, filas):
        matriz.append([])
    for i in range(0, filas):
        for j in range(0, columnas):
             matriz[i].append(j)
             matriz[i][j]=0
    return matriz
#Suma Matrices creando una nueva
def sumam(ma1, ma2):
    if validacion(ma1)!=validacion(ma2) :
        print ("matrices no validas")
    else:
        filas=len(ma1)
        columnas=len(ma1[0])
        man=creamatriz(filas, columnas)
        for i in range (filas):
            for j in range (columnas):
                man[i][j] =ma1[i][j]+ ma2[i][j]
        print(man)
#Invierte Matriz
def invierte(m1):
    if validacion(m1)==True:
        filas=len(m1[0])
        columnas=len(m1)
        m2=creamatriz(filas, columnas)
        for i in range(filas):
            for j in range(columnas):
                m2[i][j]=m1[j][i]
        return m2

#RECURSIVIDAD======================================================================================================================================
def largo(n):
    if n<10:
        return 1
    else:
        return 1 + largo(n//10)

def esPrimo(n):
    return esPrimoAux(n,2)
def esPrimoAux(n,i):
    if i==n:
        return True
    else:
        if n%i==0:
            return False
        else:
            return esPrimoAux(n,i+1)
#CANTIDAD DE PARES EN UN NUMERO
def cantidadPares(n):
    if n<9:
        if n%2==0:
            return 1
        else:
            return 0
    elif (n%10)%2==0:
        return 1+cantidadPares(n//10)
    else:
        return cantidadPares(n//10)
#CREA UNA LISTA DE LOS ELEM HASTA LLEGAR AL ELEM SELECCIONADO
def particionLista(lista,elem):
    if lista[0]!=elem:
        return [lista[0]]+particionLista(lista[1:],elem)
    else:
        return [elem]
#CREA UNA LISTA DEL NUMERO
def nList(n):
    if n==0:
        return []
    else:
        return nList(n//10) + [n%10]
#CREA UNA LISTA DEL I HASTA N
def generadorLista(n,i):
    if i == n:
        return [n]
    else:
        return [i]+generadorLista(n,i+1)
#FACTORIAL RECURSIVO
def factorialR(n):
    if n==1:
        return 1
    else:
        return n*factorialR(n-1)
#STRINGS======================================================================================================================================

#IMPRIME LA PRIMERA EN MAYUSCULA
cadena= 'ana'
print(cadena.capitalize())

#IMPRIME TODAS EN MAYUSCULA
cadena1= 'casa'
print(cadena1.upper())

#IMPRIME TODAS EN MINUSCULA
cadena2='CaSitA'
print(cadena2.lower())

#VERIFICA STRING ES NUM (SIN ESPACIOS)
cadena3='20'
print(cadena3.isdigit())

#VERIFICA SI SON LETRAS (SIN ESPACIOS)
cadena4='Holamundo'
if cadena4.isalpha():
    print('Son alfabeticos')

#VERFICA SI ES UN ESPACIO
cadena5='    '
if cadena5.isspace():
    print('Espacio en blanco')

#VERIFICA SI SON NUMEROS Y LETRAS (ALFANUMERICOS)
cadena6= 'Cordoba613'
if cadena6.isalnum():
    print('Son alfanumericos')

#IMPRIME LA POSICION DE LA LETRA DESDE EL INICIO
cadena7='esto es una prueba y es solo es eso'
pos=cadena7.find('es')
print(pos)

#IMPRIME LA POSICION DE LA LETRA DESDE EL FINAL
cadena8 = 'esto es una prueba y solo es eso'
pos = cadena8.rfind('es')
print(pos)

#CUENTA LA CANTIDAD DE VECES QUE APARECE UNA PALABRA EN EL STRING
cadena9='Ana va a la playa por la mañana pero Ana no quiere ir en la tarde pobre Ana'
cont=cadena9.count('Ana')
print(cont)

#REEMPLAZAR LA PALABRA DESDE EL PRINCIPIO HASTA LA CANTIDAD DE LA ENTRADA (2)
cadena10=cadena9.replace('Ana','papaya',2)
print(cadena10)

#SEPARA LOS STRINGS SEPARADOS POR UN SEPARADOR / [maximo==rango]
#split('SEPARADOR',[maximo])
lista=cadena10.split(' ')
print(lista)

#INVIERTE LA CADENA
def inversa(cadena):
    invertida=''
    cont=len(cadena)
    indice=-1
    while cont>=1:
        invertida=invertida+cadena[indice]
        indice=indice+(-1)
        cont=cont-1
    return invertida
#VALIDA SI ES PALINDROMO O NO
def esPalindromo(cadena):
    cadena=cadena.lower()
    palabra_invertida=inversa(cadena)
    indice=0
    cont=0
    for i in range(len(cadena)):
        if palabra_invertida[indice]==cadena[indice]:
            indice= indice+1
            cont= cont+1
        else:
            print('No es palindromo')
            break
        if cont==len(cadena):
            print('Es palindromo')
#INTERCALAR DOS LISTAS
def intercalador(list1,list2):
    newList=[]
    cont=0
    while list1!=[] and list2!=[]:
        newList+=[list1[0]]+[list2[0]]
        list1=list1[1:]
        list2=list2[1:]
    if list1==[]:
        while list2!=[]:
            newList+=[list2[0]]
            list2=list2[1:]
    if list2==[]:
        while list1!=[]:
            newList+=[list1[0]]
            list1=list1[1:]
    return newList

#CONVERTIR LISTA EN NUMERO
def listToNum(new):
   for i in new: 
    print(i, end="")
    
#CLASES

libros = []

class Libro:
    ID=''
    titulo= ''
    autor = ''
    numeroEjmTotales= 0
    numeroEjmPrestados= 0
    anno= ''

    def imprimirLibros(self):
        print('Identificacion: ',self.ID)
        print('Titulo: ',self.titulo)
        print('Autor: ',self.autor)
        print('Anno: ',self.anno)
        print('Numero de Ejemplares Totales: ',self.numeroEjmTotales)
        print('Numero de Ejemplares Prestados: ',self.numeroEjmPrestados)
    def prestador(self,sub):
        self.numeroEjmTotales = self.numeroEjmTotales - sub
        self.numeroEjmPrestados = self.numeroEjmPrestados + sub
    def retorner(self,add):
        self.numeroEjmTotales = self.numeroEjmTotales + add
        self.numeroEjmPrestados = self.numeroEjmPrestados - add
    def autorPrint(self):
        print('El autor del libro es: ',self.autor)
    def annoPrint(self):
        print('El anno del libro es: ',self.anno)
    def cantidadLibros(self):
        print('El numero de ejemplares totales es: ',self.numeroEjmTotales)
    def listaDisponibles(self):
        if self.numeroEjmTotales>self.numeroEjmPrestados:
            print('El numero de ejemplares disponibles es: ',(self.numeroEjmTotales-self.numeroEjmPrestados))
        else:
            print('El numero de ejemplares disponibles es: ',(self.numeroEjmPrestados-self.numeroEjmTotales))

opcion = " "
while opcion.upper() != "S" :   #se sale hasta que "S"
    print("   1.  Ingresar libro")
    print("   2.  Imprimir libros")
    print("   3.  Prestar Libro")
    print("   4.  Devolver Libro")
    print("   5.  Autor ")
    print("   6.  Anno")
    print("   7.  Numeros de Ejemplares Totales")
    print("   8.  Disponibles")
    print("   S.  Salir")
    print("")
    opcion = input('Digite la opcion y presione enter: ')

    if opcion == '1':
        p = Libro()
        p.ID = input("Digite la identificacion del Libro: ")
        p.titulo = input("Digite el titulo: ")
        p.autor = input("Digite el nombre del autor: ")
        p.numeroEjmTotales = int(input("Digite la cantidad de ejemplares: "))
        p.numeroEjmPrestados = int(input("Digite la cantidad de ejemplares prestados: "))
        p.anno = int(input("Digite el anno de publicacion: "))
        libros.append(p)
        print()
        print()
        print('Libro Ingresado!')
        print()
        print()
    elif opcion == '2':
        print('Lista de Libros')
        print('===================')
        for i in range(len(libros)):
            libros[i].imprimirLibros()
            print()
        print('====================')
    elif opcion == '3':
        identificador = input("Digite la identificacion del Libro: ")
        encontro= -1
        for i in range(len(libros)):
            if libros[i].ID == identificador :
                encontro = i
        if encontro!=-1:
            presta = int(input('Cantidad de libros que desea retirar: '))
            if presta<libros[encontro].numeroEjmTotales:
                libros[encontro].prestador(presta)
                print()
                print('Procedimiento Exitoso',True)
                print()
            else:
                print()
                print('Procedimiento Fallido',False)
                print()
        else:
            print()
            print('Libro NO Registrado')
            print()
    elif opcion == '4':
        identificador = input("Digite la identificacion del Libro: ")
        encontro= -1
        for i in range(len(libros)):
            if libros[i].ID == identificador :
                encontro = i
        if encontro!=-1:
            presta = int(input('Cantidad de libros que desea devolver: '))
            if presta<libros[encontro].numeroEjmTotales:
                libros[encontro].retorner(presta)
                print()
                print('Procedimiento Exitoso',True)
                print()
            else:
                print()
                print('Procedimiento Fallido',False)
                print()
        else:
            print()
            print('Libro NO Registrado')
            print()
            
    elif opcion == '5':
        name = input("Digite el nombre del Libro: ")
        encontro= -1
        for i in range(len(libros)):
            if libros[i].titulo == name :
                encontro = i
        if encontro!=-1:
            print()
            libros[encontro].autorPrint()
            print()
        else:
            print()
            print('Libro NO Registrado')
            print()

    elif opcion == '6':
        name = input("Digite el nombre del Libro: ")
        encontro= -1
        for i in range(len(libros)):
            if libros[i].titulo == name :
                encontro = i
        if encontro!=-1:
            print()
            libros[encontro]. annoPrint()
            print()
        else:
            print()
            print('Libro NO Registrado')
            print()
    elif opcion == '7':
        name = input("Digite el nombre del Libro: ")
        encontro= -1
        for i in range(len(libros)):
            if libros[i].titulo == name :
                encontro = i
        if encontro!=-1:
            print()
            libros[encontro].cantidadLibros()
            print()
        else:
            print()
            print('Libro NO Registrado')
            print()
    elif opcion == '8':
        name = input("Digite el nombre del Libro: ")
        encontro= -1
        for i in range(len(libros)):
            if libros[i].titulo == name :
                encontro = i
        if encontro!=-1:
            print()
            libros[encontro].listaDisponibles()
            print()
        else:
            print()
            print('Libro NO Registrado')
            print()
