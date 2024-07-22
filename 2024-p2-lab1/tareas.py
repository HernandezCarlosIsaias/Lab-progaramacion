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
        self.contador_total = 0 # Agregamos una variable self.contador_total que guarda el valor int 0
        self.contador_prioridad1 = 0 # Agregamos una variable self.contador_prioridad1 que guarda el valor int 0
        self.contador_prioridad2 = 0 # Agregamos una variable self.contador_prioridad2 que guarda el valor int 0
        self.contador_prioridad3 = 0 # Agregamos una variable self.contador_prioridad3 que guarda el valor int 0
        self.contador_tareas_pendientes = 0 # Agregamos una variable self.contador_tareas_pendientes que guarda el valor int 0

    def esta_vacia(self): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada esta_vacia pasandole como parametro self
        return self.cabeza is None # Retorna si self.cabeza es None, devolviendo True o False

    def agregar_tarea(self, descripcion, prioridad, categoria): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada agregar_tarea pasandole como parametro self, descripcion, prioridad y categoria
        if categoria != "": # Compara si el parametro categoria es distinto o no de string vacio. En el caso de que la condicion se cumpla ingresa al if
            tarea = Tarea(self.id_actual, descripcion, prioridad, categoria) # Guardamos en la variable tarea el objeto de la clase Tarea donde le pasamos los parametros self.id_actual, descripcion, prioridad y categoria
        else: #En el caso de que la condiion anterior no se cumpla, ingresa al else
            tarea = Tarea(self.id_actual, descripcion, prioridad) # Se crea una variable llamada tarea donde en este caso creamos el objeto de la clase Tarea pero excluyendo el parametro categoria
        nuevo_nodo = Nodo(tarea) # Guardamos en la variable nuevo_nodo el objeto de la clase Nodo pasandole como parámetro la variable tarea (es decir, el objeto creado de la clase Tarea)
        self.id_actual += 1 # Se incrementa el valor de self.id_actual que pertenece al constructor del objeto de la clase ListaEnlazada a +1

        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad: # Se crea una condicion donde primero accede al metodo esta_vacia, devolviendo un Bool; la otra condicion es si la prioridad de la tarea creada es mayor a la prioridad de la tarea que se encuentra en la cabeza del objeto de la clase ListaEnlazada
            # Si alguna de las dos condiciones explicadas anteriormente dan como valor booleano True, ingresa al condicional if
            nuevo_nodo.siguiente = self.cabeza # En la variable nuevo_nodo que dentro del mismo esta guardado el objeto de la clase Nodo guarda en el self.siguiente el valor de self.cabeza
            self.cabeza = nuevo_nodo # En self.cabeza se guarda el objeto que se encuentra dentro de la variable nuevo_nodo 
        else: # Si ambas condiciones del if dan False, accede al else
            actual = self.cabeza # Creamos una variable actual donde guardamos self.cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad: # Creamos un bucle cuando mientras el siguiente del valor de actual no sea None y que la prioridad de la tarea del siguiente de actual sea mayor o igual a la prioridad de la nueva tarea
                actual = actual.siguiente # Pisamos la variable actual donde ahora en vez de valer self.cabeza va a valer actual.siguiente (self.siguiente perteneciente a la clase Nodo)  
            nuevo_nodo.siguiente = actual.siguiente # En el siguiente del nuevo nodo que creamos guardamos el valor de la variable actual.siguiente
            actual.siguiente = nuevo_nodo # En actual.siguiente guardamos el valor del objeto nuevo_nodo
        
        self.contador_total += 1 # Se incrementa el valor guardado en self.contador_total a +1
        self.contador_tareas_pendientes += 1 # Se incrementa el valor guardado en self.contador_tareas_pendientes a +1
        
        if tarea.prioridad == 1: # Si la prioridad de la tarea es igual al valor 1 ingresa al if
            self.contador_prioridad1 += 1  # Se incrementa el valor de la variable self.contador_prioridad1 a +1
        elif tarea.prioridad == 2: # Si no se cumple el if anterior pero la prioridad de la tarea es igual al valor 2 ingresa al elif
            self.contador_prioridad2 += 1 # Se incrementa el valor de la variable self.contador_prioridad2 a +1
        else: # Si no se cumple tanto el if como el elif ingresa al else
            self.contador_prioridad3 += 1 # Se incrementa el valor de la variable self.contador_prioridad3 a +1
        print("Tarea agregada con éxito.") # Se muestra en pantalla el string "Tarea agregada con exito"

    def buscar_tarea_descripcion(self,text)->True: # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada buscar_tarea_descripcion pasandole como parametro self y text
        actual = self.cabeza # Creamos la variable actual donde guardamos self.cabeza perteneciente de la clase ListaEnlazada
        encontrada = False # Creamos una variable encontrada donde guardamos como valor el booleano False
        while actual is not None: # En el ciclo while compara si actual no es None , es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.descripcion.lower() == text.lower(): # Convierte el str del texto ingresado por el usuario y el str de la descripcion de la tarea en minusculas y lo compara. Si da True ingresa al if
                encontrada = True # Actualizamos el valor de la variable encontrada por el booleano True
            actual = actual.siguiente # Actualizamos el valor de la variable actual con el valor de actual.siguiente para que luego vuelva al ciclo while con el nuevo valor
        return encontrada # Cuando el ciclo while de false, se retorna el valor de la variable encontrada, de los cuales la misma puede ser True o False

    def completar_tarea(self, id): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada completar_tarea pasandole como parametro self e id 
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        while actual is not None: # En el ciclo while compara si actual no es None, es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.id == id: # Compara si el id de la tarea que se encuentra en self.cabeza es igual al id que le pasa el usuario
                actual.tarea.completada = True # Si se entra al condicional de la linea anterior se reemplaza el valor que se encuentra en la variable completada del objeto de la clase Tarea por True
                if actual.tarea.prioridad == 1: # Si la prioridad de la tarea guardada en la variable actual es igual a 1 ingresa al if
                    self.contador_prioridad1 -= 1 # Decrece el valor de la variable self.contador_prioridad1 a -1
                elif actual.tarea.prioridad == 2: # Si el if anterior no se cumple y el valor de la prioridad de la tarea es igual al 2 ingresa al elif
                    self.contador_prioridad2 -= 1 # Decrece el valor de la variable self.contador_prioridad2 a -1  
                else: # Si no se cumple tanto el if como el elif ingresa al else
                    self.contador_prioridad3 -= 1 # Decrece el valor de la variable self.contador_prioridad3 a -1
                self.contador_tareas_pendientes -= 1 # Decrece el valor de la variable self.contador_tareas_pendientes a -1
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
                else: # Si la condicion mas cercana da como booleano False, ingresa al else
                    previo.siguiente = actual.siguiente # Actualizamos el valor de previo.siguiente y guardamos el valor de actual.siguiente
                self.contador_total -= 1 # Decrece el valor de la variable self.contador_total a -1
                
                if actual.tarea.completada == False: # Si el valor de la variable completada de la tarea es igual a False, ingresa al if
                    if actual.tarea.prioridad == 1: # Si la prioridad de la tarea guardada en la variable actual es igual a 1 ingresa al if
                        self.contador_prioridad1 -= 1 # Decrece el valor de la variable self.contador_prioridad1 a -1
                    elif actual.tarea.prioridad == 2: # Si el if anterior no se cumple y el valor de la prioridad de la tarea es igual al 2 ingresa al elif
                        self.contador_prioridad2 -= 1 # Decrece el valor de la variable self.contador_prioridad2 a -1  
                    else: # Si no se cumple tanto el if como el elif ingresa al else
                        self.contador_prioridad3 -= 1 # Decrece el valor de la variable self.contador_prioridad3 a -1
                    self.contador_tareas_pendientes -= 1 # Decrece el valor de la variable self.contador_tareas_pendientes a -1
                
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
            if actual.tarea.descripcion.lower() == text.lower(): # Convertimos los str del texto ingresado por el usuario y la descripcion de la tarea en la variable actual en minusculas. Si son iguales entra en el if
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}") # Si se cumple la condicion de la linea anterior imprime todos los atributos de la clase tarea que se encuentran en el nodo
                control = True # Se actualiza el valor de la variable control por el booleano True     
            actual = actual.siguiente # Se reemplaza el valor de actual con el valor de actual.siguiente
        if control == False: # Se compara si el booleano de la variable control es False. Si dicha condicion da True, ingresa al if; si no, lo saltea
            print(f"No existen tareas con descripcion {text}") # Se imprime en la pantalla el str no hay tareas existentes con la descripcion escrita por el usuario
    
    # Funciones estadisticas:
    def contar_tareas_pendientes_lineal(self)->int: # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada contar_tareas_pendientes (siendo de notacion O(n)) pasandole como parametro self
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        contador_pendiente = 0 # Creamos la variable contador donde le asginamos dentro de la misma el valor entero 0
        while actual is not None: # En el ciclo while compara si actual no es none, es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.completada == False: # Compara si el valor de la variable del objeto Tarea guardada en el Nodo en self.cabeza es igual a False. Si dicha condicion dd True, ingresa. Si no, la saltea
                contador_pendiente += 1 # En el caso de que el if de la linea anterior cumpla la condicion, se le suma a la variable contador_pendiente +1          
            actual = actual.siguiente # Se reemplaza el valor de actual con el valor de actual.siguiente
        return contador_pendiente # Cuando el ciclo while de False, retorna el valor de la variable contador_pendiente
    
    def contar_tareas_pendientes(self)->int: # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada contar_tareas_pendientes (siendo de notacion O(cte)) pasandole como parametro self
        return self.contador_tareas_pendientes # Retorna el valor de la variable self.contador_tareas_pendientes

    def mostrar_estadisticas(self)->None: # Creamos el metodo mostrar_estadisticas dentro del objeto de la clase ListaEnlazada, pasandole como parametro self
        tareas_pendientes = self.contar_tareas_pendientes() # Guardamos en la variable tareas_pendientes el valor que devuelva el metodo contar_tareas_pendientes
        tareas_completadas = (100 * (self.contador_total - tareas_pendientes)) / self.contador_total # En la variable tareas_completadas guardamos el valor de la operacion 
        print(f"El porcentaje de las tareas completadas es: {tareas_completadas}%") # Se imprime en pantalla el str del porcentaje de las tareas completadas con su valor respectivo
        print(f"La cantidad de tareas pendientes es: \n- De prioridad 1: {self.contador_prioridad1} tarea/s.\n- De prioridad 2: {self.contador_prioridad2} tarea/s.\n- De prioridad 3: {self.contador_prioridad3} tarea/s.") # Se imprime en pantalla la cantidad de tareas pendientes con su respectiva prioridad
       
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

    def agregar_tarea_existente(self, tarea): # Se crea el metodo agregar_tarea_existente en el objeto de la clase ListaEnlazada donde recibe como parametros self y tarea
        nuevo_nodo = Nodo(tarea) # Se guarda en la variable nuevo_nodo el objeto de clase Nodo con el parametro tarea 
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad: # Accede al metodo self.esta_vacia devolviendo un booleano y compara si la prioridad de la tea es mayor a la prioridad de la tarea en self.cabeza
            # Si alguna de los booleanos da True, ingresa al if
            nuevo_nodo.siguiente = self.cabeza # En el siguiente de la variable nuevo_nodo se guarda el nodo de self.cabeza 
            self.cabeza = nuevo_nodo # En self.cabeza se guarda el objeto que se encuentra dentro de la variable nuevo_nodo
        else: # Si ambas condiciones del if dan False, ingresa al else
            actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad: # Mientras el siguiente no sea None y la prioridad de la tarea en actual.siguiente sea mayor o igual a la prioridad de la nueva tarea, ingresa al ciclo while 
                actual = actual.siguiente # Se pisa la variable actual teniendo como nuevo valor el siguiente (self.siguiente)
            # Cuando el ciclo while de False, sale del mismo y sigue con las lineas del codigo que se encuentran dentro del metodo
            nuevo_nodo.siguiente = actual.siguiente # El valor del siguiente del nuevo_nodo es el valor del siguiente de la variable actual
            actual.siguiente = nuevo_nodo # El valor del siguiente del actual es ahora el nuevo_nodo
        
        if tarea.id >= self.id_actual: # Compara si el id de la tarea es mayor o igual al valor de la variable del constructor de la clase ListaEnlazada. Si da true ingresa al if
            self.id_actual = tarea.id + 1 # Se cambia el valor de la variable self.id_actual utilizando el valor del id de la tarea + 1
        
        self.contador_total += 1 # Se incrementa el valor de la variable self.contador_total a +1
        
        if nuevo_nodo.tarea.completada == False: # Si el valor de la variable completada de la tarea es igual a False, ingresa al if 
            if nuevo_nodo.tarea.prioridad == 1: # Si la prioridad de la tarea es igual al valor ingresa al if
                self.contador_prioridad1 += 1 # Se incrementa el valor de la variable self.contador_prioridad1 a +1
            elif nuevo_nodo.tarea.prioridad == 2: # Si no ingresa al if pero el valor de la prioridad es igual a 2 ingresa al elif
                self.contador_prioridad2 += 1 # Se incrementa el valor de la variable self.contador_prioridad2 a +1  
            else: # Si no se cumple las condiciones tanto del if como del elif ingresa al else
                self.contador_prioridad3 += 1 # Se incrementa el valor de la variable self.contador_prioridad3 a +1
            self.contador_tareas_pendientes += 1 # Se incrementa el valor de la variable self.contador_tareas_pendientes a +1

def menu(): # Definimos en el main del programa el procedimiento menu donde no se le pasa ningun parametro
    print("\nMenú:") # Imprime en pantalla el str Menú
    print("1. Agregar tarea") # Imprime en pantalla el str 1. Agregar tarea
    print("2. Completar tarea") # Imprime en pantalla el str 2. Completar tarea
    print("3. Eliminar tarea") # Imprime en pantalla el str 3. Eliminar tarea
    print("4. Buscar tarea por descripcion") # Imprime en pantalla el str "4. Buscar tarea por descripcion"
    print("5. Mostrar todas las tareas") # Imprime en pantalla el str "5. Mostrar todas las tareas"
    print("6. Mostrar tareas pendientes") # Imprime en pantalla el str "6. Mostrar tareas pendientes"
    print("7. Mostrar tareas por descripcion") # Imprime en pantalla el str "7. Mostrar tareas por descripcion"
    print("8. Contar tareas pendientes") # Imprime en pantalla el str "8. Contar tareas pendientes"
    print("9. Estadisticas") # Imprime en pantalla el str "9. Estadisticas"
    print("10. Guardar tareas en archivo CSV") # Imprime en pantalla el str "10. Guardar tareas en archivo CSV"
    print("11. Cargar tareas desde archivo CSV") # Imprime en pantalla el str "11. Cargar tareas desde archivo CSV" 
    print("12. Salir") # Imprime en pantalla el str "12. Salir"

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
                descripcion = input("Ingrese la descripción de la tarea: ")
                if descripcion != "":
                    if lista_tareas.buscar_tarea_descripcion(descripcion) == False:
                        error= True
                        while error == True:
                            try:
                                prioridad = int(input("Ingrese la prioridad de la tarea (1 = baja, 2 = media, 3 = alta): "))
                                while prioridad <= 0 or prioridad >= 4:
                                    prioridad = int(input("Numero no valido. Ingrese la prioridad de la tarea (1 = baja, 2 = media, 3 = alta):  ")) 
                                categoria = input("Ingrese la categoría de la tarea: ") 
                                lista_tareas.agregar_tarea(descripcion, prioridad, categoria)
                                control = True 
                                error= False                
                            except ValueError:
                                print("Debes ingresar una prioridad")
                                error= True
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
            total = lista_tareas.contar_tareas_pendientes()
            print(f"Cantidad pendiente: {total} tarea/s.")
        
        elif opcion == "9":
            lista_tareas.mostrar_estadisticas()
        
        elif opcion == "10":
            lista_tareas.guardar_en_csv(archivo_csv)
        
        elif opcion == "11":
            lista_tareas.cargar_desde_csv(archivo_csv)
        
        elif opcion == "12":
            print("Saliendo del sistema de gestión de tareas.")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
