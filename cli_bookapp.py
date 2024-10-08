import click

from BookObject import BookClass
from recommend_service import recommend_service
     
Book=BookClass()

@click.group()
def cli():
    click.echo("Welcome to BookApp! Start exploring the book world in a new way!")

@click.command()
def search_books():
    # Interogari initiale
    name = click.prompt("What is your name?")
    click.echo(f"Hi {name}! What type of new and exciting books do you want to find?")
    click.echo('\nPress ENTER if you don\'t want the specific property.')
    
    # Criterii de căutare
    # Book.topic = click.prompt('Topic, what the book shoud be about',default='[not specified]',show_default=False)
    # Book.style = click.prompt('Specific writing style',default='[not specified]',show_default=False)
    # Book.language = click.prompt('Book language',default='[not specified]',show_default=False)
    # Book.min_pages = click.prompt('Minimal page count',default='0',show_default=True)
    # Book.max_pages = click.prompt("Max book page count",default='10000', show_default=True)

    click.echo(f"Searching books about {Book.topic}, in {Book.language}, with min {Book.min_pages}, and max {Book.max_pages} pages, with {Book.style} writing style.")

    # Executare app.py
    results=recommend_service(Book)
    print(results["answer"])
    print(results["context"])

 
    # TODO de implementat

    # Alegerea cărții
    #book_index = click.prompt('Alege cartea de la poziția', type=int)
    #click.echo(f"Cartea selectată este la poziția {book_index}")
    
    #Logica de generare a rezumatului (de implementat)
    #click.echo("Generăm un rezumat pentru cartea selectată...")


cli.add_command(search_books)

if __name__ == '__main__':
    cli()