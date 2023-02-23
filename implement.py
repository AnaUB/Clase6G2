from sistemaVet import *

def main():
    servicio_hospitalario = sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota
                       \n6- Eliminar medicamento  
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))

        if menu == 1:
            if servicio_hospitalario.verNumeroMascotas() >= 14:
                print("No hay espacio disponible...")
                continue
            historia = int(input(" ingrese la historia clinica de la mascota: "))
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                if tipo == "canino":
                    if servicio_hospitalario.verNumeroCaninos() < 7:
                        peso=int(input("Ingrese el peso de la mascota: "))
                        dia = int(input("Ingrese el día de ingreso: "))
                        mes = int(input("Ingrese el mes de ingreso: "))
                        año = int(input("Ingrese el año de ingreso: "))
                        fecha = datetime.datetime(f"{año},{mes},{dia}")
                        cantidad = int(input("¿Cuántos medicamentos le suministra a la mascota?"))
                        med_ind = []
                        for i in range(0, cantidad):
                            medicamento.asignarNombre(input("Ingrese nombre del medicamento: "))
                            medicamento.asignarDosis(int(input("Ingrese dosis del medicamento: ")))
                            medicamento=Medicamento()
                            med_ind.append(medicamento)
                        mas = Mascota()
                        mas.asignarNombre(nombre)
                        mas.asignarHistoria(historia)
                        mas.asignarPeso(peso)
                        mas.asignarTipo(tipo)
                        mas.asignarFecha(fecha)
                        mas.asignarMedicamento(med_ind)
                        servicio_hospitalario.ingresarCanino(mas)
                    else:
                        print("No hay espacio disponible...")
                        break
                if tipo == "felino":
                    if servicio_hospitalario.verNumeroFelinos() < 7:
                        peso=int(input("Ingrese el peso de la mascota: "))
                        dia = int(input("Ingrese el día de ingreso: "))
                        mes = int(input("Ingrese el mes de ingreso: "))
                        año = int(input("Ingrese el año de ingreso: "))
                        fecha = datetime.datetime(f"{año},{mes},{dia}")
                        cantidad = int(input("¿Cuántos medicamentos le suministra a la mascota?"))
                        med_ind = []
                        for i in range(0, cantidad)):
                            medicamento.asignarNombre(input("Ingrese nombre del medicamento: "))
                            medicamento.asignarDosis(int(input("Ingrese dosis del medicamento: ")))
                            medicamento=Medicamento()
                            med_ind,append(medicamento)
                        mas = Mascota()
                        mas.asignarNombre(nombre)
                        mas.asignarHistoria(historia)
                        mas.asignarPeso(peso)
                        mas.asignarTipo(tipo)
                        mas.asignarFecha(fecha)
                        mas.asignarMedicamento(med_ind)
                        servicio_hospitalario.ingresarFelino(mas)
                    else:
                        print("No hay espacio disponible...")
                        break

            else:
                print("Ya existe una mascota con el numero de historia clínica ingresado.") 
            
        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            if fecha != None:  
                print("La fecha de ingreso de la mascota es: " + fecha.strftime("%x"))
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
          
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4:
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento=servicio_hospitalario.verMedicamento(q)
            if medicamento != None: 
                print(f"El medicamento suministrado es: {medicamento.verNombre()} con dosis {medicamento.verDosis()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu == 6: #Eliminar medicamento
            n = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion2 = servicio_hospitalario.eliminarMedicamneto(n)
            if resultado operacion2 == True:
                print("Medicamento eliminado del sistema con exito")
            else:
                print("No se ha podido eliminar el medicamento")

        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, inténtelo nuevamente...")

if __name__ == "__main__":
    main()