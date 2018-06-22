def calificacionexamen(nombre):
  print("")
  print("Hola "+nombre)
  print("Inserta la calificación de tus tareas")
  tarea1=float(input("Tarea 1:"))
  tarea2=float(input("Tarea 2:"))
  tarea3=float(input("Tarea 3:"))
  tarea4=float(input("Tarea 4:"))
  tarea5=float(input("Tarea 5:"))

  print("Inserta la calificación de tus exámenes")
  exa1=float(input("Examen 1:"))
  exa2=float(input("Examen 2:"))
  exa3=float(input("Examen 3:"))
  exa4=float(input("Examen 4:"))
  
  promedioexa = (exa1+exa2+exa3+exa4)/4
  promediotareas = (tarea1+tarea2+tarea3+tarea4+tarea5)/5
  
  print("")
  print("Tu promedio semifinal es: ",promedioexa)

  print("Tu promedio de tareas es: ",promediotareas)
  print("")
  if promediotareas>8.5:
     print("Tienes medio punto extra por tus buenas tareas")
     promedioexa=promedioexa+0.5
     print("Tu calificación final es:",promedioexa)
  elif promediotareas<=8.5 and promediotareas>7:
     print("El promedio de tus tareas no es apto para subir medio punto")
     print("Tu calificación final es:",promedioexa)
  else:
  	 print("Tus tareas fueron insuficientes para el curso, medio punto menos")
  	 promedioexa=promedioexa-0.5
  	 print("Tu calificación final es:",promedioexa)


calificacionexamen("Tista")
