# Créer generator
#!/usr/bin/env python3

# Generator - génère des calculs aléatoires simples

import random

def generer_expression():
    """Crée une opération simple avec deux nombres et un opérateur"""
    operateurs = ['+', '-', '*', '/']

    # Tirer deux nombres entre 1 et 100
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operateur = random.choice(operateurs)

    # Éviter la division par zéro
    if operateur == '/' and b == 0:
        b = 1

    return f"{a} {operateur} {b}"


def main():
    print("=== Générateur d'expressions ===")
    print("Combien d'expressions veux-tu générer ?")

    try:
        n = int(input("> "))

        if n <= 0:
            print("Le nombre doit être positif.")
            return

        print("\nExpressions générées :")
        for _ in range(n):
            print(generer_expression())

    except ValueError:
        print("Erreur : entre un nombre entier valide.")


if __name__ == "__main__":
    main()
