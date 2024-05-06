archivo = open("data/atp_tennis.csv", "r")

lineas = archivo.readlines() 
lineas = [l.split("|") for l in lineas] #Lista 

for x in lineas:
    cadena = """<b>Torneo:</b> %s <br> <b>Ganador:<b> %s""" % (x[0],x[9])
    print(cadena)
    archivo_generado = open("data/%s.html" % (x[9]), "w")  #Nombre unico de archivo, deben salir 24362 archivos unicos hasta las 12
    archivo_generado.writelines("%s\n" % (cadena))
    archivo_generado.close()