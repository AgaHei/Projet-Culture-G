from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# 1. Charger l'index FAISS
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
db = FAISS.load_local(
    "data/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True # Permet la désérialisation (à utiliser avec précaution)
)

# 2. Configurer TinyLlama pour le CPU
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  # Modèle optimisé pour le CPU
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cpu",  # Force l'utilisation du CPU
    load_in_8bit=False,  # Désactive pour le CPU (8bit est pour GPU)
    torch_dtype="auto"
)

# 3. Pipeline optimisé pour le CPU
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=150,  # Réduit pour le CPU
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.1
)
llm = HuggingFacePipeline(pipeline=pipe)

# 4. Prompt optimisé
template = """
Tu es un **prof de culture G ultra-cool** qui explique les trucs **comme à des potes de 15 ans**.
**Règles absolues :**
1. Réponds en **3 phrases max** (court et percutant).
2. Utilise **des emojis** (🗼, 💥, 😂, etc.) pour illustrer.
3. Fais **des comparaisons modernes** (ex: "comme un story Instagram", "comme un TikTok viral").
4. Évite **les termes compliqués** (remplace par des mots simples).
5. Si tu ne sais pas, dis-le avec humour ("Là, je sèche… comme un dev sans café ! ☕").

**Contexte (extraits du livre) :**
{context}

**Question du user :**
{question}

**Réponse (style ado, max 3 phrases, avec emojis) :**
"""
prompt = PromptTemplate(input_variables=["context", "question"], template=template)

# 5. Chaîne RAG
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={"k": 3}),
    chain_type_kwargs={"prompt": prompt}
)

# Test
question = "Pourquoi la Tour Eiffel a été construite ?"
response = qa_chain.invoke({"query": question})
print("🤖 Réponse :", response["result"])




