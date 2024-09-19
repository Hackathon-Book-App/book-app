import click

from app import App

class Book_properties:
    def __init__(self,gen,topic,style,language,pages):
        self.gen=gen
        self.topic=topic
        self.style=style
        self.language=language
        self.pages=pages
     
Book=Book_properties('','','','',any)

@click.group()
def cli():
    click.echo("Welcome to BookApp! Începe acum să explorezi lumea cărților într-un mod nou!")

@click.command()
def search_books():
    # Interogari initiale
    name = click.prompt("Cum te numești?")
    click.echo(f"Salut, {name}! Ce vrei să afli nou ?")
    click.echo('Apasa ENTER daca nu doresti sa adaugi o anumita proprietate.')
    
    # Criterii de căutare
    Book.gen = click.prompt('Introdu genul cărții ',default="",show_default=False) 
    Book.topic = click.prompt('Despre ce este cartea',default='',show_default=False)
    Book.style = click.prompt('Stilul în care este scrisă cartea',default='',show_default=False)
    Book.language = click.prompt('Limba în care este scrisă cartea',default='',show_default=False)
    Book.pages = click.prompt('Numărul aproximativ de pagini',type=int,default='400',show_default=False)

    click.echo(f"Căutare cărți cu genul: {Book.gen}, despre: {Book.topic}, stil: {Book.style}, în limba: {Book.language}, cu aproximativ {Book.pages} pagini.")

    # Executare app.py
    print(App(Book))
    
 
    # de implementat

    # Alegerea cărții
    #book_index = click.prompt('Alege cartea de la poziția', type=int)
    #click.echo(f"Cartea selectată este la poziția {book_index}")
    
    #Logica de generare a rezumatului (de implementat)
    #click.echo("Generăm un rezumat pentru cartea selectată...")


cli.add_command(search_books)

if __name__ == '__main__':
    cli()