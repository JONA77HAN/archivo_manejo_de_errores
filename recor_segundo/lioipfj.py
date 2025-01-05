print('TOUCH CONTROL')
print('lioipfj.py')
print('segundo princial')
print('terminal')

import random

# Lista de Pokémon (Generaciones 1 a 9, algunos ejemplos representativos)
pokemon_list = [
    "Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Eevee", "Jigglypuff", "Meowth", 
    "Psyduck", "Machop", "Magnemite", "Gastly", "Onix", "Cubone", "Rhyhorn", "Magikarp",
    "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Mewtwo", "Chikorita", 
    "Cyndaquil", "Totodile", "Pichu", "Togepi", "Mareep", "Sudowoodo", "Wooper", 
    "Espeon", "Umbreon", "Murkrow", "Misdreavus", "Wobbuffet", "Sneasel", "Teddiursa", 
    "Houndour", "Phanpy", "Larvitar", "Lugia", "Ho-Oh", "Treecko", "Torchic", "Mudkip", 
    "Ralts", "Slakoth", "Nincada", "Whismur", "Makuhita", "Aron", "Roselia", "Trapinch", 
    "Swablu", "Zangoose", "Seviper", "Barboach", "Baltoy", "Lileep", "Anorith", 
    "Absol", "Snorunt", "Beldum", "Regirock", "Regice", "Registeel", "Latias", "Latios", 
    "Kyogre", "Groudon", "Rayquaza", "Turtwig", "Chimchar", "Piplup", "Starly", "Shinx", 
    "Budew", "Cranidos", "Shieldon", "Burmy", "Combee", "Buizel", "Cherubi", "Shellos", 
    "Drifloon", "Buneary", "Glameow", "Chingling", "Stunky", "Bronzor", "Gible", "Riolu", 
    "Hippopotas", "Skorupi", "Croagunk", "Carnivine", "Finneon", "Mantyke", "Snover", 
    "Rotom", "Uxie", "Mesprit", "Azelf", "Dialga", "Palkia", "Heatran", "Regigigas", 
    "Giratina", "Cresselia", "Darkrai", "Shaymin", "Victini", "Snivy", "Tepig", 
    "Oshawott", "Blitzle", "Zorua", "Drilbur", "Audino", "Timburr", "Tympole", 
    "Venipede", "Cottonee", "Petilil", "Sandile", "Darumaka", "Scraggy", "Yamask", 
    "Archen", "Trubbish", "Zorua", "Solosis", "Ducklett", "Vanillite", "Deerling", 
    "Foongus", "Ferroseed", "Klink", "Tynamo", "Litwick", "Axew", "Cubchoo", "Shelmet", 
    "Mienfoo", "Golett", "Pawniard", "Rufflet", "Vullaby", "Deino", "Larvesta"
]

# Selección de 145 Pokémon random sin repetición
random_pokemons = random.sample(pokemon_list, k=145)

random_pokemons
