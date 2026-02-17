import requests

def afficher_citation_aleatoire():
    url = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"
    
    try:
        # Appel à l'API
        reponse = requests.get(url)
        reponse.raise_for_status()
        
        # Extraction du message JSON
        donnees = reponse.json()
        citation = donnees['message']
        
        # Affichage stylisé
        print("\n" + "="*50)
        print(f'"{citation}"')
        print("="*50 + "\n")
        
    except Exception as e:
        print(f"Oups ! Impossible de joindre l'API : {e}")

if __name__ == "__main__":
    afficher_citation_aleatoire()