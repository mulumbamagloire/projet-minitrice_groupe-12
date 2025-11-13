# Créer minitrice
#!/usr/bin/env python3

# Minitrice - calculatrice simple
# Fait les 4 opérations de base : +, -, *, /

def evaluer_expression(expression):
    
    """Évalue une expression simple du type : nombre opérateur nombre"""
    
    # On sépare les éléments par des espaces
    elements = expression.split()

    # Vérifie qu’il y a bien 3 éléments : ex. "5 + 2"
    if len(elements) != 3:
        return "Erreur : format attendu -> nombre opérateur nombre"

    # On récupère les valeurs
    nombre1 = elements[0]
    operateur = elements[1]
    nombre2 = elements[2]

    # Vérifie que les deux nombres sont positifs
    if not nombre1.isdigit() or not nombre2.isdigit():
        return "Erreur : veuillez entrer des nombres positifs"

    nombre1 = float(nombre1)
    nombre2 = float(nombre2)

    # Calcule selon l’opérateur
    if operateur == '+':
        resultat = nombre1 + nombre2
    elif operateur == '-':
        resultat = nombre1 - nombre2
    elif operateur == '*':
        resultat = nombre1 * nombre2
    elif operateur == '/':
        if nombre2 == 0:
            return "Erreur : division par zéro"
        resultat = nombre1 / nombre2
    else:
        return "Erreur : opérateur inconnu"

    # Si le résultat est un entier, on l’affiche sans décimales
    if resultat == int(resultat):
        resultat = int(resultat)

    return resultat


def main():
    print("=== Minitrice ===")
    print("Entrez une opération (exemple : 4 * 2)")
    print("Tapez 'exit' pour quitter")

    while True:
        expression = input("> ")

        if expression.lower() == "exit":
            print("Fin du programme.")
            break

        resultat = evaluer_expression(expression)
        print(resultat)


if __name__ == "__main__":
    main()
