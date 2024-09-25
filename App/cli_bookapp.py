import click

from app import App

class Book_properties:
    def __init__(self=None,topic=None,style=None,language=None,min_pages=None, max_pages=None):
        self.topic=topic
        self.style=style
        self.language=language
        self.min_pages=min_pages
        self.max_pages=max_pages
     
Book=Book_properties()

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
    Book.topic = click.prompt('Topic, what the book shoud be about',default='[not specified]',show_default=False)
    Book.style = click.prompt('Specific writing style',default='[not specified]',show_default=False)
    Book.language = click.prompt('Book language',default='[not specified]',show_default=False)
    Book.min_pages = click.prompt('Minimal page count',type=int,default='0',show_default=True)
    Book.max_pages = click.prompt("Max book page count",default='10000', show_default=True)

    click.echo(f"Searching books about {Book.topic}, in {Book.language}, with min {Book.min_pages}, and max {Book.max_pages} pages, with {Book.style} writing style.")

    # Executare app.py
    results=App(Book)
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