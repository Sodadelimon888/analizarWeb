#Importando la libreria webtech
import webtech

#Metodo pata analizar las tecnologias
def analizar(url):
    wt = webtech.WebTech();
    resultado = wt.start_from_url(url, timeout=5);
    return resultado;

#Peticion basica pata insertar url.
print('Ingrese la URL de la pagina que quiere analizar');
url = input();
print(analizar(url));