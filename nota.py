
import typer
import os
import json

app = typer.Typer()

FILE = 'notas.txt'
ESTILO1 = typer.colors.MAGENTA
ESTILO2 = typer.colors.RED

@app.command()
def crear(
    nota: str,
    claves: str = typer.Option(..., prompt="Ahora introduce las palabras claves separadas por 1 espacio: ")
    ):
    entrada = {
        "nota": nota,
        "claves" : claves.split(" ")
        }
    with open (FILE, 'a') as f:
        f.write(json.dumps(entrada) + "\n")

@app.command()
def listar(clave: str = typer.Option("")):
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            alguna = False
            typer.echo()
            for num, line in enumerate(f):
                entrada = json.loads(line)
                if clave and clave in entrada["claves"]:
                    typer.secho(" - " + entrada["nota"], fg=ESTILO2)
                    typer.secho("Palabras claves: " + str(entrada["claves"]), fg=ESTILO2)
                    typer.echo()
                    alguna = True
                elif not clave:
                    typer.secho(str(num + 1) + " - " + entrada["nota"], fg=ESTILO2)
                    typer.secho("Palabras claves: " + str(entrada["claves"]), fg=ESTILO2)
                    typer.echo()
                    alguna = True
            if not alguna:
                typer.secho("No existe ninguna nota con esa palabra clave...", fg=ESTILO1)
    else:
        typer.secho("No existe ninguna nota que listar!", fg=ESTILO1)


@app.command()
def borrar_nota(num: int):
    index = num - 1

    with open(FILE, 'r') as f:
        notas = f.readlines()
        if len(notas) >= index:
            del notas[index]
        else:
            typer.secho("No existe esa nota...", fg=ESTILO1)
            raise typer.Exit()

    with open(FILE, 'w') as f:
        f.writelines(notas)

@app.command()
def borrar_todo(
    forzar: bool = typer.Option(..., prompt="Seguro que quieres borrar todas las notas??")
):
    if forzar:
        if os.path.exists(FILE):
            os.remove(FILE)
            typer.secho("Notas borradas!", fg=ESTILO1)
        else:
            typer.secho("No existe ninguna nota que borrar!", fg=ESTILO1)
    else:
        typer.secho("Operación cancelada...", fg=ESTILO1)

if __name__ == "__main__":
    app()
