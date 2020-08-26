import os
import typer
import datetime as dt

PATH = r'C:\Users\v_bat\Documents\VSCProjects\pruebas_typer\escaneados'

app = typer.Typer()

with os.scandir(PATH) as ficheros:
    ficheros = [fichero.name for fichero in ficheros if fichero.is_file and fichero.name.endswith('pdf')]

@app.command()
def renombrar(num: int):
    hoy = dt.datetime.now()
    fecha = hoy.strftime('%y%m%d%H%M')
    for i, f in enumerate(ficheros):
        archivo = f'{PATH}\\{f}'
        nuevo = f'{PATH}\\FP{fecha}_{num+i}.pdf'
        os.rename(archivo, nuevo)


if __name__ == "__main__":
    app()
