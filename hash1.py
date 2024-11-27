
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

size = int(input("Tamaño de la tabla hash: "))
hash_table = HashTable(size)

while True:
    option = input("¿Deseas insertar (1), buscar (2) o salir (3)? ")
    if option == "1":
        key = int(input("Ingresa la clave (número): "))
        value = input("Ingresa el valor: ")
        hash_table.insert(key, value)
        print("Valor insertado.")
    elif option == "2":
        key = int(input("Ingresa la clave a buscar: "))
        result = hash_table.search(key)
        print(f"Resultado: {result}" if result else "Clave no encontrada.")
    elif option == "3":
        break
    else:
        print("Opción no válida.")


