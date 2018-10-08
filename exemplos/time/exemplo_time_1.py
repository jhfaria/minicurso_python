import time

# dicionario com os dias da semana #
semana = {0: "2a feira",
		  1: "3a feira",
		  2: "4a feira",
		  3: "5a feira",
		  4: "6a feira",
		  5: "Sabado",
		  6: "Domingo",
}

# segundos desde 1970 #
seg_1970 = time.time()

print("Se passaram {:f} segundos desde (00:00:00 01/01/1970).".format(seg_1970))

# converte os segundos em uma struct com valores entendiveis #
ano, mes, dia, hora, minuto, segundos, dia_semana, dia_ano, horario_verao = time.localtime(seg_1970)

print(semana[dia_semana])
print("Dia:		{:s}/{:s}/{:s}".format(str(dia).zfill(2), str(mes).zfill(2), str(ano).zfill(2)))
print("Horario:	{:s}:{:s}:{:s}".format(str(hora).zfill(2), str(minuto).zfill(2), str(segundos).zfill(2)))
print("Hoje eh o {:d}o dia do ano!".format(dia_ano))