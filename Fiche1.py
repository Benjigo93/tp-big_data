# ---- EXERCICE 1 ---- #

# Question 1
products = {
    'Sabre laser': 229.0,
    'Mitendo DX': 127.30,
    'Coussin Linux': 74.50,
    'Slip Goldorak': 29.90,
    'Station Nextpresso': 184.60
}


# Question 2
def disponibilite(name, price):
    return name in products and products[name] == price


# Question 3
def prix_moyen(products):
    prices = []
    for product in products:
        prices.append(products[product])

    return sum(prices) / len(prices)


# Question 4
def fourchette_prix(mini, maxi, products):
    filteredProducts = set()
    for product in products:
        if maxi >= products[product] >= mini:
            filteredProducts.add(product)

    return filteredProducts


# Question 5
cart = {
    'Sabre laser': 3,
    'Coussin Linux': 2,
    'Slip Goldorak': 1,
}


# Question 6
def tous_disponibles(cart, products):
    check = True
    for product in cart:
        if product not in [*products]:
            check = False
            break

    return check


# Question 7
def prix_achats(cart, products):
    total = 0
    for product in cart:
        if product in [*products]:
            total += products[product] * cart[product]

    return total


# print(disponibilite('Sabre laser', 289.0))
# print(prix_moyen(products))
# print(fourchette_prix(50.0, 200.0, products))
# print(tous_disponibles(cart, products))
# print(prix_achats(cart, products))


# ---- EXERCICE 2 ---- #

Dessert = {
    'gateau chocolat': {'chocolat', 'oeuf', 'farine', 'sucre', 'beurre'},
    'gateau yaourt': {'yaourt', 'oeuf', 'farine', 'sucre'},
    'crepes': {'oeuf', 'farine', 'lait'},
    'quatre-quarts': {'oeuf', 'farine', 'beurre', 'sucre'},
    'kouign amann': {'farine', 'beurre', 'sucre'}
}


# Question 1
def nb_ingredients(book, recipe):
    return len(book[recipe]) if recipe in [*book] else 0


# Question 2
def recette_avec(book, item):
    filteredRecipes = set()
    for recipe in book:
        if item in book[recipe]:
            filteredRecipes.add(recipe)
    return filteredRecipes


# Question 3
def tous_ingredients(book):
    filteredIngredients = set()
    for recipe in book:
        for ingredient in book[recipe]:
            if ingredient not in filteredIngredients:
                filteredIngredients.add(ingredient)
    return filteredIngredients


# Question 4
def table_ingredients(book):
    table = {}
    ingredients = tous_ingredients(book)
    for ingredient in ingredients:
        table[ingredient] = recette_avec(book, ingredient)
    return table


# Question 5
def ingredient_principal(book):
    max = 0
    main_item = ''
    table = table_ingredients(book)
    for ingredient in table:
        if len(table[ingredient]) > max:
            max = len(table[ingredient])
            main_item = ingredient

    return main_item


# Question 6
def recettes_sans(book, item):
    filteredRecettes = {}
    for recipe in book:
        if item not in book[recipe]:
            filteredRecettes[recipe] = book[recipe]
    return filteredRecettes


# print(nb_ingredients(Dessert, 'gatesdu yaourt'))
# print(recette_avec(Dessert, 'lait'))
# print(tous_ingredients(Dessert))
# print(table_ingredients(Dessert))
# print(ingredient_principal(Dessert))
# print(recettes_sans(Dessert, 'beurre'))


# ---- EXERCICE 3 ---- #

def est_lettre(c):
    return ((c >= 'a') and (c <= 'z')) \
           or ((c >= 'A') and (c <= 'Z')) \
           or (c in {'é', 'è', 'à', 'ù', 'oe'})


# Question 1
def frequences_lettres(text):
    return {letter: text.count(letter) for letter in text if est_lettre(letter)}


# Question 2
def lettre_freq_max(letter_frequences):
    lettre, frequence = max(letter_frequences.items(), key=lambda tup: tup[1])
    return lettre


# Question 3
def chargement_texte(file):
    contenu = ""
    with open(file, "r") as f:
        contenu = f.read()
    return contenu


# Question 4
def lettres_freq_inf(letter_frequences, maximum):
    dict_letters = letter_frequences.copy()
    for letter, amount in letter_frequences.items():
        if amount > maximum:
            del dict_letters[letter]
    return list(dict_letters.keys())

# print(frequences_lettres('alea jacta est'))
# print(lettre_freq_max(frequences_lettres('alea jacta est')))
# print(lettres_freq_inf(frequences_lettres('alea jacta est'), 1))
