import time

def main():
    import time

def calcular_tiempo_restante():
    hora_actual = time.localtime().tm_hour
    minutos_actual = time.localtime().tm_min
    hora_limite = 19

    if hora_actual >= hora_limite:
        print("¡Es hora de ir a casa!")
    else:
        minutos_restantes = (hora_limite - hora_actual - 1) * 60 + (60 - minutos_actual)
        horas_restantes = minutos_restantes // 60
        minutos_restantes %= 60

        print("Aún queda tiempo de trabajo. Tiempo restante: {} horas y {} minutos.".format(horas_restantes, minutos_restantes))

calcular_tiempo_restante()


if __name__ == '__main__':
    main() 