def agenda_movil():
    mi_agenda = {}  # diccionario, no lista

    def insertar_contacto():
        name = input("Introduce el nombre del contacto: ")
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and len(phone) <= 11:
            mi_agenda[name] = phone
            print(f" Contacto {name} agregado.")
        else:
            print(" El teléfono debe tener solo dígitos y máximo 11 números.")

    def buscar_contacto():
        name = input("Introduce el nombre del contacto a buscar: ")
        if name in mi_agenda:
            print(f" El número de {name} es {mi_agenda[name]}.")
        else:
            print(f"El contacto {name} no existe.")

    def actualizar_contacto():
        name = input("Introduce el nombre del contacto a actualizar: ")
        if name in mi_agenda:
            phone = input("Introduce el nuevo teléfono: ")
            if phone.isdigit() and len(phone) <= 11:
                mi_agenda[name] = phone
                print(f" Contacto {name} actualizado.")
            else:
                print(" Número inválido.")
        else:
            print(f" El contacto {name} no existe.")

    def eliminar_contacto():
        name = input("Introduce el nombre del contacto a eliminar: ")
        if name in mi_agenda:
            del mi_agenda[name]
            print(f" Contacto {name} eliminado.")
        else:
            print(f" El contacto {name} no existe.")

    # Bucle principal
    while True:
        print("\n Menú de Opciones")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            buscar_contacto()
        elif opcion == "2":
            insertar_contacto()
        elif opcion == "3":
            actualizar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print(" ¡Hasta luego!")
            break
        else:
            print(" Opción no válida.")
