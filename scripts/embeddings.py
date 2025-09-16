from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# 1. Charger le texte nettoyé
with open("data/texte_nettoye.txt", "r", encoding="utf-8") as f:
    texte = f.read()

# 2. Découper le texte en chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)
chunks = text_splitter.split_text(texte)
print(f"✅ Texte découpé en {len(chunks)} chunks.")

# 3. Générer les embeddings avec un modèle français
#    --> Désactive la conversion automatique avec `encode_kwargs`
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)
print("🔍 Génération des embeddings en cours...")

# 4. Créer et sauvegarder l'index FAISS
db = FAISS.from_texts(chunks, embeddings)
db.save_local("data/faiss_index")
print("🎉 Embeddings générés et sauvegardés dans data/faiss_index/")

# 5. Afficher un exemple de chunk
if chunks:
    print("\n--- Exemple de chunk ---")
    print(chunks[0][:200] + "...")

