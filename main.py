import pandas as pd

clientes_ventas = pd.read_json(r"C:\Users\JOSE CARDENAS\OneDrive\Escritorio\Talsa\clientes_ventas.json")

with open(
    r"C:\Users\JOSE CARDENAS\OneDrive\Escritorio\Talsa\catalogo_equipos_raw.txt",
    "r",
    encoding="utf-8"
) as archivo:
    txt_archivo = archivo.read()

catalogo_equipos_raw = pd.DataFrame({
    "txt" : txt_archivo.splitlines()
})

# print("Caracteres del archivo:", len(txt_archivo))
# print("Filas del DataFrame:", len(catalogo_equipos_raw))
# print("Caracteres cargados:", catalogo_equipos_raw["txt"].str.len().sum())

# Comprobar que todas las líneas coinciden
if (txt_archivo.splitlines() == catalogo_equipos_raw["txt"].tolist()):
    print("Se conservaron todas las líneas")
else:
    print("Se perdieron líneas en la conversión a DataFrame")