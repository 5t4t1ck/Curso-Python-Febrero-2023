import os

if os.path.exists("Archivos2/Archivos_Ejemplo"):
    os.rmdir("Archivos2/Archivos_Ejemplo")
    print("El directorio ha sido eliminado con éxito!!!")
else:
    print("El directorio no existe")