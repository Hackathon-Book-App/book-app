import click

@click.group()
def cli():
    click.echo("Welcome to BookApp! Începe acum să explorezi lumea cărților într-un mod nou!")

@click.command()
def search_books():
    # Interogari initiale
    name = click.prompt("Cum te numești?")
    click.echo(f"Salut, {name}!")
    click.echo("Ce vrei să afli nou ?")
    
    # Criterii de căutare
    gen = click.prompt('Introdu genul cărții')
    topic = click.prompt('Despre ce este cartea')
    style = click.prompt('Stilul în care este scrisă cartea')
    language = click.prompt('Limba în care este scrisă cartea')
    pages = click.prompt('Numărul aproximativ de pagini', type=int)
    
    # Logica de căutare (de implementat)
    click.echo(f"Căutare cărți cu genul: {gen}, despre: {topic}, stil: {style}, în limba: {language}, cu aproximativ {pages} pagini.")
    click.echo("1. Cartea X")
    click.echo("2. Cartea Y")
    
    # Alegerea cărții
    book_index = click.prompt('Alege cartea de la poziția', type=int)
    click.echo(f"Cartea selectată este la poziția {book_index}")
    
    # Logica de generare a rezumatului (de implementat)
    click.echo("Generăm un rezumat pentru cartea selectată...")

cli.add_command(search_books)

if __name__ == '__main__':
    cli()