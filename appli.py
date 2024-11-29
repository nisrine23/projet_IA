
# pour activer le venv: (.venv\Scripts\activate)
import streamlit as st

# Titre de l'application
st.set_page_config(page_title="Industrial Monitoring Dashboard", layout="wide")
st.title("Industrial Monitoring Dashboard")

# Barre latérale
st.sidebar.title("Navigation")
page = st.sidebar.radio("Menu", ["Home", "Identifiant", "Département", "Mécanique", "Électrique", "Procédés", "Assistant Virtuel"])

# Affichage en fonction de la sélection dans la barre latérale
if page == "Home":
    st.write("Bienvenue sur le tableau de bord industriel.")
elif page == "Identifiant":
    identifiant = st.text_input("Entrez votre identifiant")
    if identifiant:
        st.write(f"Identifiant : {identifiant}")
elif page == "Département":
    st.write("Choisissez un département")
    department = st.selectbox("Sélectionnez le département", ["Mécanique", "Électrique", "Procédés"])
    st.write(f"Département sélectionné : {department}")
elif page == "Mécanique":
    st.write("Bienvenue dans la section Mécanique.")
elif page == "Électrique":
    st.write("Bienvenue dans la section Électrique.")
elif page == "Procédés":
    st.write("Bienvenue dans la section Procédés.")
elif page == "Assistant Virtuel":
    st.write("Bienvenue dans l'assistant virtuel.")
    query = st.text_input("Posez votre question à l'assistant virtuel")
    if query:
        st.write(f"Assistant virtuel : Vous avez demandé '{query}'.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("**Industrial Monitoring Dashboard v1.0**")

### assistant virtuel 
import openai

# Configure ton API OpenAI
openai.api_key = "ta_clé_api_openai"

if page == "Assistant Virtuel":
    st.write("Bienvenue dans l'assistant virtuel.")
    query = st.text_input("Posez votre question à l'assistant virtuel")

    if query:
        # Appel à l'API OpenAI pour obtenir une réponse
        response = openai.Completion.create(
            engine="text-davinci-003",  # Utilise le modèle GPT-3 ou GPT-4 selon la configuration
            prompt=query,
            max_tokens=150
        )
        
        # Afficher la réponse
        answer = response.choices[0].text.strip()
        st.write(f"Assistant virtuel : {answer}")
