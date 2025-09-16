import pdfplumber
import re

def nettoyer_texte(texte):
    """Nettoie le texte extrait du PDF (supprime numéros de page, espaces, etc.)."""
    texte = re.sub(r'\n\d+\n', '\n', texte)  # Supprime les numéros de page
    texte = re.sub(r'\s+', ' ', texte)       # Supprime les espaces multiples
    texte = re.sub(r'[^\w\s,.;!?\'"-]', '', texte)  # Supprime les caractères spéciaux
    texte = texte.replace("«", '"').replace("»", '"')  # Remplace les guillemets français
    return texte.strip()

def extraire_texte_pdf(chemin_pdf):
    """Extrait le texte du PDF en ignorant les images et nettoie le résultat."""
    texte_brut = ""
    with pdfplumber.open(chemin_pdf) as pdf:
        for page in pdf.pages:
            # Extraire uniquement le texte (ignore les images)
            texte_page = page.extract_text()
            if texte_page:
                texte_brut += texte_page + "\n"
    return nettoyer_texte(texte_brut)

# Utilisation
chemin_pdf = "data/La_Culture_Generale_Pour_Les_Nuls.pdf"  # Chemin relatif depuis la racine 
texte_nettoye = extraire_texte_pdf(chemin_pdf)

print(texte_nettoye[:500])  # Affiche les 500 premiers caractères

# Sauvegarder le texte nettoyé
with open("data/texte_nettoye.txt", "w", encoding="utf-8") as f:
    f.write(texte_nettoye)

print("Extraction et nettoyage terminés !")
