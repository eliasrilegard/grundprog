# Specifikation

## Inledning:
Jag vill programmera ett spel baserat på det klassiska "Minesweeper". Programmet kommer startas från ett terminalprogram, men själva spelet ska befinna sig i ett separat fönster. Programmet kommer därför ha ett GUI och användaren ska kunna klicka på en ruta för att öppna den istället för att använda koordinater som matas in till kommandolinjen.

En av de största utmaningarna inför detta projekt kommer vara strukturen för att lagra alla brickor (eng. "tiles") och minor, och hur programmet ska jobba med det.

## Användarscenarier:

### Spelgenomgång
Osquar (spelaren, användaren) presenteras först med ett blankt bräde, dvs alla rutor är gömda. Han får då möjligheten till att klicka på en ruta för att öppna den. Antingen är rutan en mina (tough luck!) och han förlorar direkt, eller en siffra. Siffran ska indikera hur många angränsande minor som finns till just den ruta. Om siffran är 0 visas ingenting, och en Flood Fill-algoritm körs som visar alla 8 angränsande rutor till rutan.

### Flood Filling
När Flood Fill-algoritmen aktiveras på en ruta ska hela området där alla tomma rutor (dvs antal angränsande minor är 0) också öppnas. Mer info kring hur denna algoritm fungerar principmässigt finns under https://en.wikipedia.org/wiki/Flood_fill.

### Poäng
När spelet avslutas ska en poäng för spelomgången beräknas, som tar hänsyn till bl.a. storleken på brädet, antalet minor och tiden. Spelaren ska tillfrågas om sitt namn, som lagras i en separat fil, dvs en highscore-lista, tillsammans med spelarens poäng. 

## Programskelett:
```python
class Tile:
  def show(self):
    """Rita själva rutan och eventuella flaggor, minor etc."""
    pass

class Board:
  def show(self):
    """Rita hela brädet"""
    pass

  def countNearby(self):
    """ Beräkna för alla rutor hur många minor som
    rutan angränsar till """
    pass

  def floodFill(self):
    """ Algoritm för Flood fill här """
    pass
```

## Programflöde och dataflöde:
Programmet börjar med att skapa en matris av en given storlek och fyller den med Tile-objekt. Varje ruta innehåller information om var den befinner sig i matrisen, sin position i fönstret, om den innehåller en mina, etc. Efter att matrisen skapats och initialiserats med rutor placeras placeras slumpmässigt ett antal minor från en given variabel ut. Därefter räknar varje ruta hur många angränsande minor som den gränsar till.

Efter att all förberedande information har skapats ska alla Tile-objekt (härifrån refererat till som rutor) visas. Osquar - användaren - får därefter möjligheten till att klicka på en ruta för att öppna den, eller att markera den som en flagga. Första rutan som öppnas ska aldrig vara en mina. Om rutan blir klickad på öppnas den. Om rutan gränsar mot en mina visas rutans siffra, och om rutan inte gränsar mot någon mina körs Flood fill-algoritmen med ursprung på den klickade rutan. Om rutan är en mina är spelet över och alla minor visas, oavsett om de är markerade eller inte. Minan som exploderat är extra markerad.
 
Spelet kan vinnas på två sätt: antingen genom att alla rutor som inte är minor är öppnade, eller att alla minor (och endast minor) är markerade. När spelet är över beräknas omgångens poäng, spelaren tillfrågas om sitt namn, vilket sparas i highscorelistan.