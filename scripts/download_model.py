from transformers import AutoModelForCausalLM, AutoTokenizer
import os

# Créer le dossier models/ s'il n'existe pas
os.makedirs("models/TinyLlama-1.1B-Chat-v1.0", exist_ok=True)

# Nom du modèle
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

print(f"🔍 Téléchargement du modèle {model_name}...")

# Télécharger et sauvegarder le tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.save_pretrained("models/TinyLlama-1.1B-Chat-v1.0")
print("✅ Tokenizer sauvegardé.")

# Télécharger et sauvegarder le modèle
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cpu",  # Télécharge sur CPU (pas besoin de GPU pour le téléchargement)
    low_cpu_mem_usage=True  # Réduit la mémoire utilisée pendant le téléchargement
)
model.save_pretrained("models/TinyLlama-1.1B-Chat-v1.0")
print("✅ Modèle sauvegardé dans models/TinyLlama-1.1B-Chat-v1.0/")

print("🎉 Téléchargement terminé ! Tu peux maintenant utiliser le modèle localement.")
