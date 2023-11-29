#De un numero dado muestra todos sus multiplos y suma sus multiplos impares
salida = False
sum_inp = 0
while not salida:
    try:
        n=int(input("Intoduce entero n : 0 < n < 50  "))
        if 0 < n < 50:
            for i  in range (50,201):
                if (i%n)==0:
                    print(i)
                    if not (i%2)==0:
                        sum_inp += i

            print(f"Suma de los multiplos impares: {sum_inp}")
            salida = True
        else:
            print(f"Error, n introducido en el rango incorrecto {sum_inp}")
    
    except:
        print("Error")

