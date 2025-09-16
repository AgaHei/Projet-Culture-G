# 🎓 CulturaBot

**Un chatbot qui explique la culture générale aux ados, avec humour, emojis et un style 100% décontracté.** 😎
*Parce que la culture, c’est comme TikTok : ça doit être fun, rapide et addictif !*

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-ff4b4b)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.27-green)](https://python.langchain.com/)
[![FAISS](https://img.shields.io/badge/FAISS-1.7.4-orange)](https://github.com/facebookresearch/faiss)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-TinyLlama-yellow)](https://huggingface.co/TinyLlama)


---

## 📌 Table des matières
- [🛠 Installation](#-installation)
- [🚀 Utilisation](#-utilisation)
- [🌟 Exemples de questions/réponses](#-exemples-de-questionsréponses)
- [📂 Structure du projet](#-structure-du-projet)
- [📚 Données](#-données)
- [🤖 Modèle utilisé](#-modèle-utilisé)
- [🚀 Roadmap](#-suite-de-développement)
- [🙌 Contribuer]
- [🙏 Remerciements]

---

## 🛠 Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/AgaHei/Projet-Culture-G.git
cd projet-culture-g

### 2. Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

### 3. Installer les dépendances
pip install -r requirements.txt --no-cache-dir

### 4. Télécharger le modèle (optionnel)
Le modèle TinyLlama se télécharge automatiquement à la première utilisation.
(Si tu veux l’avoir en local pour éviter de re-télécharger :)

python scripts/download_model.py

## 🚀 Utilisation (à venir)
Lancer le chatbot localement
streamlit run scripts/app.py

## 🌟 Exemples de questions (réponses à calibrer encore):

"Pourquoi la Tour Eiffel a été construite ?"→ 
    "La Tour Eiffel a été construite pour l'exposition universelle de 1889, et fut construite à partir de 1882 pour remplacer une tour abandonnée. Elle était destinée à être la première tour de métal dans le monde, avec une hauteur de 324 mètres. La construction a coûté 12 millions de francs. 🗼✨"
"C’est quoi la photosynthèse ?"→ 
    "Photosynthèse est une réaction chimique, physico-chimique et biologique qui permet de produire de l'énergie et d'émerger du matériel à partir du carbonate de calcium (Ca2+) et du dioxyde de carbone (CO2), en produisant des molécules de glucose (Glc). Elle est réalisée par les plantes, les champignons, les algues et les bactéries.🌿💚"

## 📂 Structure du projet

projet-culture-g/
├── data/
│   ├── texte_nettoye.txt       # Texte extrait et nettoyé du livre
│   └── faiss_index/            # Index FAISS pour la recherche sémantique
│
├── models/                     # Dossier pour le modèle (à télécharger)
│   └── TinyLlama-1.1B-Chat-v1.0/  # Modèle local (optionnel)
│
├── notebooks/                  # Notebooks Jupyter pour les tests
│   ├── 01_extraction.ipynb      # Nettoyage du texte
│   ├── 02_embeddings.ipynb      # Génération des embeddings
│   └── 03_test_chatbot.ipynb    # Tests interactifs
│
├── scripts/                    # Scripts Python pour le déploiement
│   ├── extraction.py          # Extraction du texte
│   ├── embeddings.py           # Génération des embeddings
│   ├── rag_pipeline.py         # Pipeline RAG
│   └── app.py                  # Interface Streamlit (à venir)
│
├── requirements.txt            # Dépendances Python
└── README.md                   # Ce fichier

## 📚 Données

Source : Livre "La Culture Générale Pour Les Nuls" de Florence Braunstein (Docteur ès lettres) et Jean-François Pépin (Agrégé d’histoire).
Format : PDF nettoyé → data/texte_nettoye.txt (texte brut).
Index FAISS : Généré à partir de chunks de 1000 caractères (avec chevauchement de 200 caractères) pour une recherche optimale.

(Les données sont nettoyées pour supprimer les artefacts OCR et les mise en page inutiles.)

## 🤖 Modèle utilisé

Nom : TinyLlama/TinyLlama-1.1B-Chat-v1.0
Taille : ~1.1B paramètres (léger et optimisé pour le CPU).
Spécialité : Réponses courtes et adaptées aux ados. Ton humoristique et décontracté (emojis, comparaisons modernes).
Avantages :
- Fonctionne sur CPU (pas besoin de GPU).
- Rapide pour un modèle de cette taille.

## 🚀 Roadmap
- [ ] Intégrer TinyLlama pour des réponses fun.
- [ ] Optimiser les embeddings avec FAISS.
- [ ] Ajouter un système de quiz interactif.
- [ ] Déployer une version publique (Streamlit/Hugging Face).

## 🙌 Contribuer
Les contributions sont les bienvenues ! Ouvre une issue ou une pull request pour :
    - Améliorer les réponses du chatbot (structurer un pipeline RAG efficace pour un chatbot axé sur la culture générale, en combinant recherche sémantique et génération de réponses)
    - Ajouter des fonctionnalités (ex: quiz, thèmes spécifiques).

## 🙏 Remerciements
- Auteurs du livre "La Culture Générale Pour Les Nuls": Mme Florence Braunstein et M. Jean-François Pépin disponible sur: https://www.academia.edu/98866721/La_culture_generale_pour_les_nuls 
- [TinyLlama](https://huggingface.co/TinyLlama) pour le modèle.
- [LangChain](https://python.langchain.com/) pour les outils RAG.