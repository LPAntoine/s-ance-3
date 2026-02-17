class Boisson:
    def __init__(self, nom, prix, categorie):
        self.nom = nom
        self.prix = prix
        self.categorie = categorie

    def __str__(self):
        return f"{self.nom} ({self.categorie}) - {self.prix:.2f}€"

class Panier:
    def __init__(self):
        self.articles = []

    def ajouter(self, boisson):
        self.articles.append(boisson)
        print(f"✅ {boisson.nom} ajouté au panier.")

    def calculer_total(self):
        return sum(item.prix for item in self.articles)

    def afficher_commande(self):
        if not self.articles:
            print("Votre panier est vide.")
            return
        print("\n--- Votre Récapitulatif ---")
        for item in self.articles:
            print(f"- {item}")
        print(f"TOTAL À PAYER : {self.calculer_total():.2f}€")

# --- Configuration du Menu ---
menu = {
    1: Boisson("Expresso", 2.50, "Café"),
    2: Boisson("Limonade Maison", 4.00, "Soft"),
    3: Boisson("Thé Glacé Pêche", 3.50, "Soft"),
    4: Boisson("Cappuccino", 3.80, "Café"),
    5: Boisson("Vin Rouge (Verre)", 5.50, "Alcool")
}

def afficher_menu():
    print("\n==== 🍹 MENU BEVERARE ☕ ====")
    for touche, boisson in menu.items():
        print(f"[{touche}] {boisson}")
    print("[0] Terminer la commande")

# --- Boucle Principale ---
def main():
    mon_panier = Panier()
    
    while True:
        afficher_menu()
        choix = input("\nChoisissez le numéro de votre boisson : ")

        if choix == "0":
            break
        
        try:
            index = int(choix)
            if index in menu:
                mon_panier.ajouter(menu[index])
            else:
                print("⚠️ Choix invalide, réessayez.")
        except ValueError:
            print("⚠️ Veuillez entrer un nombre valide.")

    mon_panier.afficher_commande()
    print("\nMerci de votre visite ! À bientôt.")

if __name__ == "__main__":
    main()