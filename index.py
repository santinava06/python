import operaciones

def main():
    sum = operaciones.suma(4, 16)
    res= operaciones.resta(10, 5)
    mult = operaciones.multiplicacion(5, 5)
    div = operaciones.division(25, 5)
    print(sum)
    print(res)
    print(mult)
    print(div)

if __name__ == '__main__':
    main() 