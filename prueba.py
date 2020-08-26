import typer
import random

__version__ = "0.0.1"

def get_name():
    return random.choice(['Anónimo','Desconocido','X'])

def trat_callback(value: str):
    posibles = ['Don','Doña','Sr','Sra']
    if value not in posibles:
        raise typer.BadParameter("Sólo se acepta Don/Doña/Sr/Sra")
    return value

def version_callback(value: bool):
    if value:
        typer.secho(f"Estupenda gran versión nº: {__version__}", fg=typer.colors.RED)
        raise typer.Exit()

def main(name: str = typer.Argument(get_name),
        trat: str = typer.Option(..., "--trat", "-t", prompt="Indica el tratamiento", callback=trat_callback),
        formal: bool = typer.Option(False, "--formal", "-f"),
        version: bool = typer.Option(None, "--version", callback=version_callback, is_eager=True)):
    """
    Saluda a NAME, opcionalmente con --trat.
    Si usas --formal, dará un saludo más formal.
    """
    if formal:
        typer.secho(f"Buenos días {trat} {name}!", fg=typer.colors.MAGENTA)
    else:
        typer.echo(f"Hola {name}!")

if __name__ == "__main__":
    typer.run(main)
