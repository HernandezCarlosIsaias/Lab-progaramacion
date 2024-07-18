import csv
import os

class Tarea: # creamos la clase tarea
    def __init__(self, id, descripcion, prioridad, categoria="General"): # Constructor de la clase tarea
        self.id = id # guardamos los atributos en la variables de la clase
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False
        self.categoria = categoria

class Nodo: # creamos la clase nodo
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None

class ListaEnlazada: #creamos la clase lista enlasada
    def __init__(self):
        self.cabeza = None
        self.id_actual = 1

    def esta_vacia(self): #definimos el metodo esta vacia
        return self.cabeza is None # compara si self.cabeza es == a none si lo es devuelve true caso contrario devuelce false
                                   #si es true la lista eta vacia sino no lo esta

    def agregar_tarea(self, descripcion, prioridad, categoria): #Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada agregar_tarea pasandole como parametro self, descripcion, prioridad y categoria
        tarea = Tarea(self.id_actual, descripcion, prioridad, categoria) #Guardamos en la variable tarea el objeto de la clase Tarea donde le pasamos los parametros self.id_actual (que al principio tiene como valor 1), descripcion, prioridad y categoria
        nuevo_nodo = Nodo(tarea) #Guardamos en la variable nuevo_nodo el objeto de la clase Nodo pasandole como parámetro la variable tarea (es decir, el objeto creado de la clase Tarea)
        self.id_actual += 1 #Se incrementa el valor de self.id_actual que pertenece al constructor del objeto de la clase ListaEnlazada a +1
        
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad: #Se crea una condicion donde primero accede al metodo esta_vacia, devolviendo un True o False; la otra condicion es si la prioridad de la tarea creada es mayor a la prioridad de la tarea que se encuentra en la cabeza del objeto de la clase ListaEnlazada
            #Si alguna de las dos condiciones explicadas anteriormente dan como valor booleano True, ingresa al condicional if de la linea 31 y accede a las lineas 33 y 34
            nuevo_nodo.siguiente = self.cabeza #En la variable nuevo_nodo que dentro del mismo esta guardado el objeto de la clase Nodo guarda en el self.siguiente el valor de self.cabeza perteneciente al objeto de la clase ListaEnlazada
            self.cabeza = nuevo_nodo #En self.cabeza del objeto de la clase ListaEnlazada guarda el objeto de la clase Nodo que se encuentra dentro de la variable nuevo_nodo creado en la linea 28 
        else: #Si ambas condiciones del if dan False, accede al else
            actual = self.cabeza #Creamos una variable actual donde guardamos self.cabeza, siendo el valor del objeto de la clase ListaEnlazada
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad: #Creamos un bucle cuando mientras el siguiente del valor de actual (siendo self.cabeza que dentro del mismo tendremos un objeto de la clase Nodo) no sea None y que la prioridad de la tarea del siguiente de actual (self.cabeza) sea mayor o igual a la prioridad de la nueva tarea que queremos agregar
                #Entra en dicho bucle en el caso de que ambas condiciones mencionadas en la linea anterior den como valor booleano True, sino salta directamente a la linea 40
                actual = actual.siguiente #Pisamos la variable actual donde ahora en vez de valer self.cabeza va a valer actual.siguiente (este actual.siguiente es el objeto de la clase Nodo que se encuentra dentro de self.cabeza que pertenece al objeto de la clase ListaEnlazada)
            nuevo_nodo.siguiente = actual.siguiente #En el siguiente del nuevo nodo que creamos guardamos el valor de la variable actual.siguiente
            actual.siguiente = nuevo_nodo #En actual.siguiente guardamos el valor del objeto nuevo_nodo

        print("Tarea agregada con éxito.") #Se muestra en pantalla el string "Tarea agregada con exito"


    def buscar_tarea_descripcion(self,texto)->True:
        actual = self.cabeza # en la variable actual guardamos a sel.cabeza
        encontrada= False
        while actual is not None: # en ciclo while compara si actual no es none , es decir si la lista no esta vacia si es true entra en el bucle
            if actual.tarea.descripcion.lower() == texto.lower():
                encontrada= True # en el if compara si actual.tarea.id es igual a el id ingresado por el usuario en el caso de true entrada
                return encontrada
            actual = actual.siguiente 
        return encontrada
        

    def completar_tarea(self, id):
        actual = self.cabeza # en la variable actual guardamos a sel.cabeza
        while actual is not None: # en ciclo while compara si actual no es none , es decir si la lista no esta vacia si es true entra en el bucle
            if actual.tarea.id == id:
                actual.tarea.completada= True
                return
            actual = actual.siguiente 
        print(f"Tarea con ID {id} no encontrada.")
        

    def eliminar_tarea(self, id): # definimos el metodo para eliminar tareas
        actual = self.cabeza # en la variable actual guardamos a sel.cabeza
        previo = None # creamos una variable previo con el valor none
        while actual is not None: # en ciclo while compara si actual no es none , es decir si la lista no esta vacia si es true entra en el bucle
            if actual.tarea.id == id: # en el if compara si actual.tarea.id es igual a el id ingresado por el usuario en el caso de true entra
                if previo is None: # vuelve a hacer una comparacion si previo es none
                    self.cabeza = actual.siguiente # en self.cabeza se guarda el valor de actual.siguiente
                else: # si el if dio false entra en el else
                    previo.siguiente = actual.siguiente # en previo.siguiente guradamos actual.siguiente
                print(f"Tarea eliminada: {actual.tarea.descripcion}") # imprimimos que la tarea fue eliminada
                return # retorna ...
            previo = actual # actualizo el valor de previo con el valor de actual
            actual = actual.siguiente # actualizo el valor de actual con el valor de actual.siguiente
        print(f"Tarea con ID {id} no encontrada.") # en el caso de que el while de false imprime en pantalla que la tarea no fue encontrada

    def mostrar_tareas(self): # definimos el metodo para mostrar las tareas
        actual = self.cabeza # en la variable actual guardamos a sel.cabeza
        control = False
        while actual is not None: # en ciclo while compara si actual no es none , es decir si la lista no esta vacia si es true entra en el bucle
            estado = "Completada" if actual.tarea.completada else "Pendiente" #guarda "completado" en la variable estado si actual.tarea.completada es true en caso contrario guarda "Pendiente"
            print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}") # imprime todos los atributos de la clase tarea que se encuntran el nodo actual, incluyendo la variable estado
            control = True
            actual = actual.siguiente # actualizo el valor de actual con el valor de actual.siguiente
        
        if control == False:
            print("No hay tareas pendientes")
    def mostrar_tareas_pendientes(self):
        actual = self.cabeza # en la variable actual guardamos a self.cabeza
        control = False
        print("*** TAREAS PENDIENTES: ***")
        while actual is not None: # en ciclo while compara si actual no es none , es decir si la lista no esta vacia si es true entra en el bucle
            if actual.tarea.completada == False:
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}")          
                control = True
            actual = actual.siguiente 
        if control == False:
            print("No hay tareas pendientes")
        
    def mostrar_tareas_descripcion(self,texto)->None:
        actual = self.cabeza # en la variable actual guardamos a self.cabeza
        control= False
        while actual is not None: # en ciclo while compara si actual no es none , es decir si la lista no esta vacia si es true entra en el bucle
            if actual.tarea.descripcion.lower() == texto.lower():
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}")          
                control= True          
            actual = actual.siguiente 
        if control == False:
            print("No se encontro la tarea")

    # Funciones estadisticas:
    def contar_tareas_pendientes(self)->int:
        actual = self.cabeza # en la variable actual guardamos a self.cabeza
        coontador= 0
        while actual is not None: # en ciclo while compara si actual no es none , es decir si la lista no esta vacia si es true entra en el bucle
            if actual.tarea.completada == False:
                contador += 1       
            actual = actual.siguiente 
        return contador
    
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

    def agregar_tarea_existente(self, tarea): # definimos el metodo agregar tarea exitente, recibe por parametro un ojeto de la clase tarea
        nuevo_nodo = Nodo(tarea) #creamos un nuevo objeto de clase Nodo y recibe por parametro al objeto tarea que ingreso el usuario
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad: # si la lista enlazada esta vacia o si la priorida de la tarea es mayor a la prioridad de la tarea de self.cabeza, entra en el if
            nuevo_nodo.siguiente = self.cabeza # en el nuevo_nodo.siguiente guardamos a self.cabeza
            self.cabeza = nuevo_nodo #en self.cabeza guardamos nuvo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

        if tarea.id >= self.id_actual:
            self.id_actual = tarea.id + 1


def menu():
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Eliminar tarea")
    print("4. Mostrar todas las tareas")
    print("5. Mostrar tareas pendientes")
    print("6. Mostrar tareas por descripcion")
    print("7. Guardar tareas en archivo CSV")
    print("8. Cargar tareas desde archivo CSV")
    print("9. Buscar tarea por descripcion")
    print("10. Salir")

def main():
    lista_tareas = ListaEnlazada()
    archivo_csv = 'tareas.csv'
    # Cargar tareas desde CSV si el archivo existe
    lista_tareas.cargar_desde_csv(archivo_csv)

    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            prioridad = int(input("Ingrese la prioridad de la tarea (1 = baja, 2 = media, 3 = alta): "))
            categoria = input("Ingrese la categoría de la tarea: ")
            lista_tareas.agregar_tarea(descripcion, prioridad, categoria)
        elif opcion == "2":
            id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
            lista_tareas.completar_tarea(id_tarea)
        elif opcion == "3":
            id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
            lista_tareas.eliminar_tarea(id_tarea)
        elif opcion == "4":
            lista_tareas.mostrar_tareas()
        elif opcion == "5":
            lista_tareas.mostrar_tareas_pendientes()
        elif opcion == "6":
            texto= input("Ingrese la descripcion de la tarea: ")
            lista_tareas.mostrar_tareas_descripcion(texto)
        elif opcion == "7":
            lista_tareas.guardar_en_csv(archivo_csv)
        elif opcion == "8":
            lista_tareas.cargar_desde_csv(archivo_csv)
        elif opcion == "9":
            texto= input("Ingrese la descripcion de la tarea: ")
            lista_tareas.buscar_tarea_descripcion(texto)
        elif opcion == "10":
            print("Saliendo del sistema de gestión de tareas.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
