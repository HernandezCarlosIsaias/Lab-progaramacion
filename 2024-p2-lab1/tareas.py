import csv
import os

class Tarea: # Creamos el objeto de clase Tarea
    def __init__(self, id, descripcion, prioridad, categoria = "General"): # Creamos el constructor del objeto de clase Tarea con los parámetros self, id, descripcion, prioridad y categoria
        # En el caso de que el usuario no cargue un valor str en el parametro categoria la misma va a tener como valor "General"
        self.id = id # Guardamos el parametro id en la variable self.id
        self.descripcion = descripcion # Guardamos el parametro id en la variable self.id
        self.prioridad = prioridad # Guardamos el parametro prioridad en la variable self.prioridad
        self.completada = False # Creamos una variable llamada self.completada donde cada nuevo objeto de la clase Tarea siempre va a empezar a tener como valor en dicha variable el valor False
        self.categoria = categoria # Guardamos el parametro categoria en la variable self.categoria

class Nodo: # Creamos el objeto de clase Nodo
    def __init__(self, tarea): # Creamos el constructor del objeto de clase Nodo con los parámetros self y tarea
        self.tarea = tarea # Guardamos el parametro tarea en la variable self.tarea
        self.siguiente = None # Creamos una variable llamada self.siguiente donde cada nuevo objeto de la clase Nodo siempre va a empezar a tener como valor en dicha variable el valor None

class ListaEnlazada: # Creamos el objeto de clase ListaEnlaazada
    def __init__(self): # Creamos el constructor del objeto de clase ListaEnalazada con el parametro self
        self.cabeza = None # Creamos una variable llamada self.cabeza donde cada nuevo objeto de la clase ListaEnalazada siempre va a empezar a tener como valor en dicha variable el valor None
        self.id_actual = 1 # Creamos una variable llamada self.id_actual donde cada nuevo objeto de la clase ListaEnalazada siempre va a empezar a tener como valor en dicha variable el valor 1

    def esta_vacia(self): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada esta_vacia pasandole como parametro self
        return self.cabeza is None # Retorna si self.cabeza es None, devolviendo True o False

    def agregar_tarea(self, descripcion, prioridad, categoria): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada agregar_tarea pasandole como parametro self, descripcion, prioridad y categoria
        if categoria != "":
            tarea = Tarea(self.id_actual, descripcion, prioridad, categoria) # Guardamos en la variable tarea el objeto de la clase Tarea donde le pasamos los parametros self.id_actual (que al principio tiene como valor 1), descripcion, prioridad y categoria
        else:
            tarea = Tarea(self.id_actual, descripcion, prioridad)
        nuevo_nodo = Nodo(tarea) # Guardamos en la variable nuevo_nodo el objeto de la clase Nodo pasandole como parámetro la variable tarea (es decir, el objeto creado de la clase Tarea)
        self.id_actual += 1 # Se incrementa el valor de self.id_actual que pertenece al constructor del objeto de la clase ListaEnlazada a +1

        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad: # Se crea una condicion donde primero accede al metodo esta_vacia, devolviendo un True o False; la otra condicion es si la prioridad de la tarea creada es mayor a la prioridad de la tarea que se encuentra en la cabeza del objeto de la clase ListaEnlazada
            # Si alguna de las dos condiciones explicadas anteriormente dan como valor booleano True, ingresa al condicional if de la linea 31 y accede a las lineas 33 y 34
            nuevo_nodo.siguiente = self.cabeza # En la variable nuevo_nodo que dentro del mismo esta guardado el objeto de la clase Nodo guarda en el self.siguiente el valor de self.cabeza perteneciente al objeto de la clase ListaEnlazada
            self.cabeza = nuevo_nodo # En self.cabeza del objeto de la clase ListaEnlazada guarda el objeto de la clase Nodo que se encuentra dentro de la variable nuevo_nodo creado en la linea 28 
        else: # Si ambas condiciones del if dan False, accede al else
            actual = self.cabeza # Creamos una variable actual donde guardamos self.cabeza, siendo el valor del objeto de la clase ListaEnlazada
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad: # Creamos un bucle cuando mientras el siguiente del valor de actual (siendo self.cabeza que dentro del mismo tendremos un objeto de la clase Nodo) no sea None y que la prioridad de la tarea del siguiente de actual (self.cabeza) sea mayor o igual a la prioridad de la nueva tarea que queremos agregar
                # Entra en dicho bucle en el caso de que ambas condiciones mencionadas en la linea anterior den como valor booleano True, sino salta directamente a la linea 40
                actual = actual.siguiente # Pisamos la variable actual donde ahora en vez de valer self.cabeza va a valer actual.siguiente (este actual.siguiente es el objeto de la clase Nodo que se encuentra dentro de self.cabeza que pertenece al objeto de la clase ListaEnlazada)
            nuevo_nodo.siguiente = actual.siguiente # En el siguiente del nuevo nodo que creamos guardamos el valor de la variable actual.siguiente
            actual.siguiente = nuevo_nodo # En actual.siguiente guardamos el valor del objeto nuevo_nodo

        print("Tarea agregada con éxito.") # Se muestra en pantalla el string "Tarea agregada con exito"

    def buscar_tarea_descripcion(self,text)->True: # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada buscar_tarea_descripcion pasandole como parametro self y text
        actual = self.cabeza # Creamos la variable actual donde guardamos self.cabeza perteneciente de la clase ListaEnlazada
        encontrada = False # Creamos una variable encontrada donde guardamos como valor el booleano False
        while actual is not None: # En el ciclo while compara si actual no es None , es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.descripcion.lower() == text.lower(): # Convertimos el string de la descripcion de la tarea que se encuentra en self.cabeza en minúsculas y comparamos si es igual al texto que escribio el usuario (convirtiendo dicho string en minusculas). Si es True entra en el if
                encontrada = True # Actualizamos el valor de la variable encontrada por el booleano True
            actual = actual.siguiente # Si no entra al if actualizamos el valor de la variable actual con el valor de actual.siguiente para que luego vuelva al ciclo while con el nuevo valor
        return encontrada # Cuando el ciclo while de false, se retorna el valor de la variable encontrada, de los cuales la misma puede ser True o False

    def completar_tarea(self, id): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada completar_tarea pasandole como parametro self e id 
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        while actual is not None: # En el ciclo while compara si actual no es None, es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.id == id: # Compara si el id de la tarea que se encuentra en self.cabeza es igual al id que le pasa el usuario
                actual.tarea.completada = True # Si se entra al condicional de la linea anterior se reemplaza el valor que se encuentra en la variable completada del objeto de la clase Tarea por True
                return # Se utiliza el return para finalizar el método
            actual = actual.siguiente # Si el condicional de la linea 59 da como booleano False, cambia el valor de actual por el siguiente Nodo 
        print(f"Tarea con ID {id} no encontrada.") # En el caso de que el while de false, imprime en pantalla que la tarea con el id que le pasó el usuario no fue encontrada

    def eliminar_tarea(self, id): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada eliminar_tarea pasandole como parametro self e id
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        previo = None # Se crea la variable previo donde se guarda el valor None
        while actual is not None: # En el ciclo while compara si actual no es None, es decir, si self.cabeza no esta vacia. Si es true entra en el ciclo, si es False lo saltea
            if actual.tarea.id == id: # En el condicional if compara si el id de la tarea que se encuentra en self.cabeza es igual al id ingresado por el usuario. En el caso de que de True entra a este condicional
                if previo is None: # Se vuelve a crear un condicional donde compara si el valor de la variable previo es None. En el caso de que sea True entra en el condicional
                    self.cabeza = actual.siguiente # Ahora en self.cabeza guardamos el valor de actual.siguiente
                else: #! Si el if de la linea 70 es False, entra en el else
                    previo.siguiente = actual.siguiente # Actualizamos el valor de previo.siguiente y guardamos el valor de actual.siguiente
                print(f"Tarea eliminada: {actual.tarea.descripcion}") # Imprimimos que la tarea fue eliminada con su respectiva descripcion
                return # Se utiliza el return para finalizar el método
            previo = actual # Se actualiza el valor de la variable previo por el valor de actual (siendo el nodo que se encuentra en self.cabeza) 
            actual = actual.siguiente # Actualiza el valor de actual con el valor de actual.siguiente (siendo actual un objeto de la clase Nodo)
        print(f"Tarea con ID {id} no encontrada.") # En el caso de que el ciclo while de false, imprime en pantalla que la tarea con el id que le pasó el usuario no fue encontrada

    def mostrar_tareas(self): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada mostrar_tareas pasandole como parametro self
        print("\n*** TAREAS ***") # Se imprime en pantalla el string *** TAREAS ***
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        control = False # Se crea una variable llamada control donde guardamos el valor booleano False
        while actual is not None: # En el ciclo while compara si actual no es none, es decir, si la lista no esta vacia. Si es true entra en el bucle
            estado = "Completada" if actual.tarea.completada else "Pendiente" # Guarda el string "Completada" en la variable estado si el valor de la tarea completada en self.cabeza es True, en caso contrario guarda el str "Pendiente"
            print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}") # Si se cumple la condicion de la linea anterior imprime todos los atributos de la clase tarea que se encuentran en el nodo, incluyendo la variable estado
            actual = actual.siguiente # Se reemplaza el valor de actual con el valor de actual.siguiente
            control = True # Se actualiza el valor de la variable control por el booleano True
        if control == False: # Se compara si el booleano de la variable control es False. Si dicha condicion da True, ingresa al if; si no, lo saltea
            print("No hay tareas existentes.") # Se imprime en la pantalla el str no hay tareas pendientes en el caso de que se haya ingresado al condicional de la linea anterior

    def mostrar_tareas_pendientes(self): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada mostrar_tareas_pendientes pasandole como parametro self
        print("\n*** TAREAS PENDIENTES ***") # Se imprime en pantalla el string *** TAREAS PENDIENTES ***
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        control = False # Se crea una variable llamada control donde guardamos el valor booleano False
        while actual is not None: # En el ciclo while compara si actual no es none, es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.completada == False: # Compara si el valor de la variable del objeto Tarea guardada en el Nodo en self.cabeza es igual a False. Si dicha condicion dd True, ingresa. Si no, la saltea
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}") # Si se cumple la condicion de la linea anterior imprime todos los atributos de la clase tarea que se encuentran en el nodo
                control = True # Se actualiza el valor de la variable control por el booleano True    
            actual = actual.siguiente # Se reemplaza el valor de actual con el valor de actual.siguiente
        if control == False: # Se compara si el booleano de la variable control es False. Si dicha condicion da True, ingresa al if; si no, lo saltea
            print("No hay tareas pendientes.") # Se imprime en la pantalla el str no hay tareas pendientes en el caso de que se haya ingresado al condicional de la linea anterior
        
    def mostrar_tareas_descripcion(self,text)->None: # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada mostrar_tareas_descripcion pasandole como parametro self y text
        print("\n*** TAREAS ***") # Se imprime en pantalla el string *** TAREAS ***
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        control = False # Se crea una variable llamada control donde guardamos el valor booleano False
        while actual is not None: # En el ciclo while compara si actual no es none, es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.descripcion.lower() == text.lower(): # Convertimos el string de la descripcion de la tarea que se encuentra en self.cabeza en minúsculas y comparamos si es igual al texto que escribio el usuario (convirtiendo dicho string en minusculas). Si es True entra en el if
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}") # Si se cumple la condicion de la linea anterior imprime todos los atributos de la clase tarea que se encuentran en el nodo
                control = True # Se actualiza el valor de la variable control por el booleano True     
            actual = actual.siguiente # Se reemplaza el valor de actual con el valor de actual.siguiente
        if control == False: # Se compara si el booleano de la variable control es False. Si dicha condicion da True, ingresa al if; si no, lo saltea
            print(f"No existen tareas con descripcion {text}") # Se imprime en la pantalla el str no hay tareas existentes con la descripcion escrita por el usuario en el caso de que se haya ingresado al condicional de la linea anterior
    
    # Funciones estadisticas:
    def contar_tareas_pendientes(self)->int: # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada contar_tareas_pendientes pasandole como parametro self
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        contador = 0 # Creamos la variable contador donde le asginamos dentro de la misma el valor entero 0
        while actual is not None: # En el ciclo while compara si actual no es none, es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.completada == False: # Compara si el valor de la variable del objeto Tarea guardada en el Nodo en self.cabeza es igual a False. Si dicha condicion dd True, ingresa. Si no, la saltea
                contador += 1 # En el caso de que el if de la linea anterior cumpla la condicion, se le suma a la variable contador +1          
            actual = actual.siguiente # Se reemplaza el valor de actual con el valor de actual.siguiente
        return contador # Cuando el ciclo while de False, retorna el valor de la variable contador 
    
    def mostrar_estadisticas(self)->None:
        pass
        
    # Carga y guardado de archivos
    def guardar_en_csv(self, archivo):
        with open(archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            actual = self.cabeza
            while actual is not None:
                writer.writerow([actual.tarea.id, actual.tarea.descripcion, actual.tarea.prioridad, actual.tarea.categoria, actual.tarea.completada])
                actual = actual.siguiente
        print(f"Tareas guardadas en {archivo} con éxito.")

    def cargar_desde_csv(self, archivo):
        if not os.path.exists(archivo):
            print(f"Archivo {archivo} no encontrado.")
            return
        with open(archivo, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                id, descripcion, prioridad, categoria, completada = int(row[0]), row[1], int(row[2]), row[3], row[4] == 'True'
                tarea = Tarea(id, descripcion, prioridad, categoria)
                tarea.completada = completada
                self.agregar_tarea_existente(tarea)
            print(f"Tareas cargadas desde {archivo} con éxito.")

    def agregar_tarea_existente(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

        if tarea.id >= self.id_actual:
            self.id_actual = tarea.id + 1

def menu(): # Definimos en el main del programa el procedimiento menu donde no se le pasa ningun parametro
    print("\nMenú:") # Imprime en pantalla el str Menú
    print("1. Agregar tarea") # Imprime en pantalla el str 1. Agregar tarea
    print("2. Completar tarea") # Imprime en pantalla el str 2. Completar tarea
    print("3. Eliminar tarea") # Imprime en pantalla el str 3. Eliminar tarea
    print("4. Buscar tarea por descripcion") # Imprime en pantalla el str 7. Buscar tarea por descripcion
    print("5. Mostrar todas las tareas") # Imprime en pantalla el str 4. Mostrar todas las tareas
    print("6. Mostrar tareas pendientes") # Imprime en pantalla el str 5. Mostrar tareas pendientes
    print("7. Mostrar tareas por descripcion") # Imprime en pantalla el str 6. Mostrar tareas por descripcion
    print("8. Guardar tareas en archivo CSV") # Imprime en pantalla el str 8. Guardar tareas en archivo CSV
    print("9. Cargar tareas desde archivo CSV") # Imprime en pantalla el str 9. Cargar tareas desde archivo CSV
    print("10. Salir") # Imprime en pantalla el str 10. Salir

def main(): # Definimos en el main del programa el procedimiento main donde no se le pasa ningun parametro
    lista_tareas = ListaEnlazada() # Se guarda en la variable lista_tareas el objeto de la clase ListaEnlazada, donde no se le pasa ningun parametro
    archivo_csv = 'tareas.csv' # Se guarda en la variable archivo_csv el str tareas.csv

    # Cargar tareas desde CSV si el archivo existe
    lista_tareas.cargar_desde_csv(archivo_csv)

    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            control = False
            while control == False:
                try:
                    descripcion = input("Ingrese la descripción de la tarea: ")
                    if descripcion != "":
                        if lista_tareas.buscar_tarea_descripcion(descripcion) == False:
                            prioridad = int(input("Ingrese la prioridad de la tarea (1 = baja, 2 = media, 3 = alta): "))
                            if prioridad > 0 and prioridad < 4: 
                                categoria = input("Ingrese la categoría de la tarea: ") 
                                lista_tareas.agregar_tarea(descripcion, prioridad, categoria)
                                control = True
                            else: 
                                print("La prioriad debe ser 1, 2 o 3")                      
                        else:
                            des_existente = input(f"Tarea con descripcion {descripcion} ya existente. ¿Desea agregar una tarea? Responda con SI o NO: ")
                            while des_existente.lower() != "si" and des_existente.lower() != "no":
                                des_existente = input("Texto no valido. Debe escribir SI o NO: ")
                            if des_existente.lower() == "no":
                                break
                    else:
                        opcion_tarea = input("Debe escribir la descripcion de la tarea. ¿Desea agregar una tarea? Responda con SI o NO: ")
                        while opcion_tarea.lower() != "si" and opcion_tarea.lower() != "no":
                            opcion_tarea = input("Texto no valido. Debe escribir SI o NO: ")
                        if opcion_tarea.lower() == "no":
                            break
                except ValueError:
                    print("Debes ingresar una prioridad")
        elif opcion == "2":
            control= False
            while control == False:
                try:
                    id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
                    lista_tareas.completar_tarea(id_tarea)
                    control= True
                    print("Tarea completada")
                except ValueError:
                    print("No ingresaste un numero")
        elif opcion == "3":
            control= False
            while control == False:
                try:
                    id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
                    lista_tareas.eliminar_tarea(id_tarea)
                    control= True
                except ValueError:
                    print("No ingresaste un numero")
        elif opcion == "4":
            texto= input("Ingrese la descripcion de la tarea: ")
            lista_tareas.buscar_tarea_descripcion(texto)
        elif opcion == "5":
            lista_tareas.mostrar_tareas()
        elif opcion == "6":
            lista_tareas.mostrar_tareas_pendientes()
        elif opcion == "7":
            texto= input("Ingrese la descripcion de la tarea: ")
            lista_tareas.mostrar_tareas_descripcion(texto)
        elif opcion == "8":
            lista_tareas.guardar_en_csv(archivo_csv)
        elif opcion == "9":
            lista_tareas.cargar_desde_csv(archivo_csv)
        elif opcion == "10":
            print("Saliendo del sistema de gestión de tareas.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
