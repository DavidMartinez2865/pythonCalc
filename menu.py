
x = 0
y = 0
res = 0
resOld = 0
salir = False
oper = 0
primer = True
string = ""
opt = ""

caracteres = 0
pasos = 0
acciones = {}



def verNum():
    while True:
        try:
            x = int(input("Escriba un número: "))
            return x
        except ValueError:
            print("Debe de escribir un número")

#def suma(res):
#    x = verNum()
#    string = f"({string} + {x})"             
#    print(string, "=")
#    res = res + x
#    print(res)
#    return string

        

#x = input("Escriba un número: ")
#        if x.isdigit():
#            return int(x)
#        else:
#            print("Debe de escribir un número")

while salir == False:

    caracteres = len(string.replace(" ", ""))
    
    if(pasos != 0):
        acciones[pasos] = string 
        print(acciones)

    print("Menu: 1.Suma 2.Resta 3.Multiplicar 4.Dividir 5.Volver atras 6.Salir")
    print("Pasos realizados: " , pasos , " Caracteres: " , caracteres)
    pasos += 1
    optOld = opt
    opt = input("Seleccione una opcion: ")
    

    match opt:
        case "1":
            if primer == True:
                x = verNum()
                y = verNum()
                res = x + y
                string = f"({x} + {y})"
                print(string , " = " , res)
                pregPrimer = input("¿Desea continuar? 1.Y 2.N  ")
                if pregPrimer == "1":
                    primer = False
                else:
                    break                
            else:
                x = verNum()
                resOld = x
                string = f"({string} + {x})"             
                print(string, "=")
                res = res + x
                print(res)
        case "2":      
            if primer == True:
                x = verNum()
                y = verNum()
                res = x - y
                string = f"({x} - {y})"
                print("Resultado: " , res)
                pregPrimer = input("¿Desea continuar? 1.Y 2.N  ")
                if pregPrimer == "1":
                    primer = False
                else:
                    break                
            else:
                x = verNum()
                resOld = x
                string = f"({string} - {x})"
                print(string, "=")
                res = res - x
                print(res)            
        case "3":  
            if primer == True:
                x = verNum()
                y = verNum()
                res = x * y
                string = f"({x} * {y})"
                print("Resultado: " , res)
                pregPrimer = input("¿Desea continuar? 1.Y 2.N  ")
                if pregPrimer == "1":
                    primer = False
                else:
                    break                
            else:
                x = verNum()
                resOld = x
                string = f"({string} * {x})"
                print(string, "=")
                res = res * x
                print(res)
        case "4":
            try:
                if primer == True:
                    x = verNum()
                    y = verNum()
                    res = x / y
                    string = f"({x} / {y})"
                    print("Resultado: " , res)
                    pregPrimer = input("¿Desea continuar? 1.Y 2.N  ")
                    if pregPrimer == "1":
                        primer = False
                    else:
                        break                
                else:
                    x = verNum()
                    resOld = x
                    res = res / x
                    string = f"({string} / {x})"
                    print(string, "=")
                    print(res)
            except ZeroDivisionError:
                print("No se puede dividir entre 0")
        case "5":
            if(primer == False):
                string = acciones[pasos - 2]
                del acciones[pasos - 1]
                pasos -= 1
                if(optOld == "1"):
                    res = res - resOld
                elif(optOld == "2"):
                    res = res + resOld
                elif(optOld == "3"):
                    res = res / resOld
                elif(optOld == "4"):
                    res = res * resOld
                print("Operación realizada con exito.")
                print(string)
                print(res)
            else:
                print("No hay pasos a los que volver.")
        case "6":
            print("Saliendo del programa...")
            salir = True
            break
        case _:
            print("Eso no es una opcion valida.")

