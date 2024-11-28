
import streamlit as st
import random
import plotly.express as px
import openai
import streamlit.components.v1 as components
import pandas as pd
import time
from datetime import datetime
import os
# Configuration de la page
st.set_page_config(page_title="Tableau de Bord Industriel", layout="wide", initial_sidebar_state="expanded")

# CSS pour la personnalisation
st.markdown("""
    <style>
        /* Pink-purple theme for background and text */
        .main {background-color: #f7f0fa; color: #4e003d;}
        h1, h2, h3, h4 {color: #d63384;}
        .sidebar .sidebar-content {background-color: #ffccff;}

        /* Styling for sidebar icons and elements */
        .stSidebar > div:first-child {background: #e0b3e6;}
        .sidebar-content > div:nth-child(2) > div > label {font-size: 20px; color: #4e003d;}
        .sidebar .sidebar-content .stRadio {background: #ffb3e6; padding: 10px; border-radius: 10px;}

        /* Customize titles and buttons */
        .stButton>button {background-color: #d63384; color: white; font-weight: bold; font-size: 16px; border: none;}
        .stButton>button:hover {background-color: #e066aa;}

        /* Additional layout adjustments */
        .css-1lcbmhc {border: 1px solid #d63384; padding: 15px; border-radius: 10px; margin-top: 20px;}
    </style>
    """, unsafe_allow_html=True)

# Titre de l'application
st.markdown("<h1 style='text-align: center;'>Tableau de Bord Industriel</h1>", unsafe_allow_html=True)

# Chemin vers le fichier de données
file_path = './data/donnees_pannes_performances.csv'

# Création automatique du dossier et du fichier si nécessaire
if not os.path.exists(file_path):
    st.warning(f"Le fichier {file_path} est introuvable. Création d'un fichier par défaut.")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Créer le dossier 'data' si non existant

    # Données par défaut
    default_data = {
        "Date": ["2024-11-20", "2024-11-21", "2024-11-22"],
        "Machine": ["Machine1", "Machine2", "Machine3"],
        "Temps de fonctionnement": [100, 200, 150],
        "Temps total de production": [120, 220, 180],
        "Nombre de pannes": [2, 3, 1],
        "Temps d'arrêt": [10, 20, 5],
        "Alertes critiques": [1, 2, 0]
    }
    pd.DataFrame(default_data).to_csv(file_path, index=False)
    st.info(f"Fichier créé avec des données par défaut : {file_path}")

# Barre latérale de navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Menu", ["🏠 Accueil", "🏢 Département", "📈 KPI",
                                 "👷‍ Formation du Personnel", "📚 Ressources", "🤖 Assistant Virtuel"])

# Page d'accueil
if page == "🏠 Accueil":
    st.markdown("## 👋 Bienvenue sur le Tableau de Bord Industriel")
    st.write("Surveillez et gérez vos sections industrielles ici.")

    # Saisie des informations par l'utilisateur
    efficacite = st.number_input("Entrez l'efficacité actuelle (%)", min_value=0, max_value=100, value=85)
    alertes = st.number_input("Entrez le nombre d'alertes actives", min_value=0, value=5)

    # Charger les données
    try:
        df = pd.read_csv(file_path)
        st.success("Fichier chargé avec succès.")
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")
        df = pd.DataFrame()  # Vide en cas d'erreur

    # Utiliser le file_uploader pour permettre à l'utilisateur de télécharger un fichier CSV
    uploaded_file = st.file_uploader("Charger un fichier de données de pannes et performances", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

    if not df.empty:
        # Calculer les KPI : OEE, MTBF, MTTR
        df['OEE'] = (df['Temps de fonctionnement'] / df['Temps total de production']) * 100  # Exemple simple pour OEE
        df['MTBF'] = df['Temps de fonctionnement'] / df['Nombre de pannes']
        df['MTTR'] = df['Temps d\'arrêt'] / df['Nombre de pannes']

        # Affichage des résultats dans Streamlit
        st.write("Données des performances et des pannes :")
        st.write(df)

        # Définir un seuil pour déclencher une alerte de panne
        seuil_OEE = 80
        seuil_MTTR = 8
        seuil_alertes = 5

        # Vérifier si les seuils sont dépassés et déterminer si une alerte est nécessaire
        df['Alerte'] = df.apply(
            lambda row: "Panne détectée" if row['OEE'] < seuil_OEE or row['MTTR'] > seuil_MTTR or row[
                'Alertes critiques'] > seuil_alertes else "Aucune panne", axis=1)

        # Afficher les alertes
        st.write("Alertes générées :")
        st.write(df[['Date', 'Machine', 'Alerte']])
        # Données simulées pour les pannes et réclamations
        pannes_data = pd.DataFrame({
            "Date": [datetime(2024, 11, 22), datetime(2024, 11, 21)],
            "Machine": ["Machine A", "Machine B"],
            "OEE": [65, 72],
            "MTTR": [45, 30],
            "Alerte": ["Panne détectée", "Maintenance préventive"],
        })

        reclamations_data = pd.DataFrame({
            "Date": ["2024-11-20", "2024-11-19"],
            "Machine": ["Machine C", "Machine D"],
            "Description": ["Capteur défectueux", "Surchauffe moteur"],
            "Statut": ["En cours", "Résolu"]
        })
        st.title("📊ATTENTION PANNES")
        st.markdown("Bienvenue ! Consultez les pannes critiques, signalez des problèmes ou suivez vos réclamations.")

        # Section 1 : Visualisation des pannes critiques
        st.markdown("### 🛠️ Pannes Critiques")
        pannes_critiques = pannes_data[pannes_data["Alerte"] == "Panne détectée"]

        if pannes_critiques.empty:
            st.success("✅ Aucune panne critique détectée.")
        else:
            st.warning("🚨 Pannes détectées ! Consultez les détails ci-dessous :")
            st.table(pannes_critiques[["Date", "Machine", "OEE", "MTTR", "Alerte"]])

        # Section 2 : Signalement d'une réclamation
        st.markdown("### 📝 Signalement d'un Problème")
        with st.form("form_reclamation"):
            nom_employe = st.text_input("Nom de l'employé")
            machine_id = st.text_input("ID de la machine")
            description = st.text_area("Décrivez le problème")
            urgence = st.selectbox("Niveau d'urgence", ["Faible", "Modérée", "Critique"])

            soumis = st.form_submit_button("Soumettre")
            if soumis:
                # Simuler l'ajout de réclamation dans le système
                st.success(f"Réclamation soumise avec succès par {nom_employe} pour la machine {machine_id} !")
                # Optionnel : Ajouter la réclamation aux données simulées
                nouvelle_reclamation = {
                    "Date": datetime.now().strftime("%Y-%m-%d"),
                    "Machine": machine_id,
                    "Description": description,
                    "Statut": "En cours"
                }
                reclamations_data = reclamations_data.append(nouvelle_reclamation, ignore_index=True)

        # Section 3 : Suivi des réclamations
        st.markdown("### 📋 Suivi des Réclamations")
        if reclamations_data.empty:
            st.info("Aucune réclamation soumise pour le moment.")
        else:
            st.table(reclamations_data)

        # Section 4 : Guides d’intervention
        st.markdown("### 📖 Guides d’Intervention")
        st.write("Consultez les guides de dépannage pour les pannes courantes :")
        if not pannes_critiques.empty:
            for _, row in pannes_critiques.iterrows():
                st.write(f"- [Guide pour {row['Machine']}](https://www.mcours.net/cours/pdf/mainten/reparerpann5.pdf)")
        else:
            st.info("Aucune panne détectée nécessitant un guide pour le moment.")

        # Section 5 : Contacts Assistance
        st.markdown("### 📞 Assistance Technique")
        st.write("Pour une assistance immédiate, contactez :")
        st.write("📧 Email : support@exemple.com")
        st.write("📞 Téléphone : +212 123 456 789")



# Page des départements avec descriptions et tâches
elif page == "🏢 Département":
    st.markdown("### 🏢 Sélectionnez un Département")
    department = st.selectbox(
        "Choisissez un département",
        [
            "🏭 Département de Production",
            "🔧 Département de Maintenance Industrielle",
            "🔬 Département de Recherche et Développement (R&D)",
            "✅ Département Qualité et Conformité",
            "🌍 Département Environnement, Santé et Sécurité (EHS)",
            "🚚 Département Logistique et Chaîne d’Approvisionnement",
            "👥 Département Ressources Humaines"
        ]
    )

    # Détails de chaque département
    if department == "🏭 Département de Production":
        st.markdown("#### 🏭 Département de Production")
        st.write("Ce département est responsable de la fabrication et de l'assemblage des produits conformément aux plans de production.")
        st.write("*Objectifs principaux* : Maximiser l'efficacité, réduire les coûts et maintenir une qualité constante.")
        st.write("*Tâches principales* :")
        st.write("- Planification et suivi de la production")
        st.write("- Contrôle des équipements et supervision des opérateurs")
        st.write("- Amélioration continue des processus de production")

    elif department == "🔧 Département de Maintenance Industrielle":
        st.markdown("#### 🔧 Département de Maintenance Industrielle")
        st.write("Ce département assure le bon fonctionnement des équipements industriels en effectuant des maintenances préventives et correctives.")
        st.write("*Objectifs principaux* : Minimiser les temps d'arrêt, améliorer la disponibilité des machines, et prolonger leur durée de vie.")
        st.write("*Tâches principales* :")
        st.write("- Réparations en cas de panne")
        st.write("- Entretien préventif des équipements")
        st.write("- Gestion des pièces de rechange et des outils")

    elif department == "🔬 Département de Recherche et Développement (R&D)":
        st.markdown("#### 🔬 Département de Recherche et Développement (R&D)")
        st.write("Le département R&D développe de nouveaux produits, procédés et technologies pour rester compétitif sur le marché.")
        st.write("*Objectifs principaux* : Innover, améliorer les performances et réduire les coûts de production.")
        st.write("*Tâches principales* :")
        st.write("- Études de faisabilité et prototypes")
        st.write("- Optimisation des procédés existants")
        st.write("- Collaboration avec les départements qualité et production")

    elif department == "✅ Département Qualité et Conformité":
        st.markdown("#### ✅ Département Qualité et Conformité")
        st.write("Ce département veille à ce que les produits respectent les normes de qualité et les réglementations en vigueur.")
        st.write("*Objectifs principaux* : Assurer la satisfaction des clients et garantir la conformité aux exigences légales.")
        st.write("*Tâches principales* :")
        st.write("- Contrôle qualité à chaque étape de production")
        st.write("- Gestion des certifications et audits")
        st.write("- Analyse des retours clients pour améliorer les processus")

    elif department == "🌍 Département Environnement, Santé et Sécurité (EHS)":
        st.markdown("#### 🌍 Département Environnement, Santé et Sécurité (EHS)")
        st.write("Ce département garantit un environnement de travail sûr, sain et respectueux des normes environnementales.")
        st.write("*Objectifs principaux* : Réduire les risques professionnels, minimiser l'impact environnemental et promouvoir la sécurité.")
        st.write("*Tâches principales* :")
        st.write("- Mise en place de politiques de sécurité")
        st.write("- Gestion des risques environnementaux")
        st.write("- Formation des employés aux règles EHS")

    elif department == "🚚 Département Logistique et Chaîne d’Approvisionnement":
        st.markdown("#### 🚚 Département Logistique et Chaîne d’Approvisionnement")
        st.write("Ce département gère l'approvisionnement, le stockage, et la distribution des produits et matériaux.")
        st.write("*Objectifs principaux* : Optimiser les flux, réduire les coûts et garantir une livraison rapide et fiable.")
        st.write("*Tâches principales* :")
        st.write("- Gestion des stocks et des entrepôts")
        st.write("- Planification des transports")
        st.write("- Relations avec les fournisseurs et partenaires")

    elif department == "👥 Département Ressources Humaines":
        st.markdown("#### 👥 Département Ressources Humaines")
        st.write("Le département RH gère le recrutement, la formation et le bien-être des employés de l'entreprise.")
        st.write("*Objectifs principaux* : Favoriser le développement des compétences et maintenir une bonne ambiance de travail.")
        st.write("*Tâches principales* :")
        st.write("- Recrutement et intégration des nouveaux employés")
        st.write("- Formation et développement professionnel")
        st.write("- Gestion des relations sociales et du bien-être au travail")
# Page des indicateurs clés de performance (KPI)
elif page == "📈 KPI":
    st.markdown("## 📈 Indicateurs Clés de Performance")
    col1, col2, col3 = st.columns(3)
    col1.metric("Efficacité Globale", "92%", "+5% depuis le mois dernier")
    col2.metric("Temps moyen entre pannes (MTBF)", "30 jours", "+3 jours")
    col3.metric("Temps moyen de réparation (MTTR)", "2 heures", "-15 min")

# Page de visualisation de l'efficacité avec Plotly
    st.markdown("## 📊 Évolution de l'Efficacité")
    data = {
        "Mois": ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin"],
        "Efficacité (%)": [80, 82, 85, 88, 90, 92]
    }
    fig = px.line(data, x="Mois", y="Efficacité (%)", title="Évolution de l'efficacité")
    st.plotly_chart(fig)

# Page de gestion des formations du personnel
elif page == "👷‍ Formation du Personnel":
    st.markdown("### 👷‍ Formations et Compétences du Personnel")
    formation = st.selectbox("Sélectionnez une formation", ["Sécurité", "Maintenance Avancée", "Énergie Renouvelable"])
    if formation == "Sécurité":
        st.write(
            "Formation Sécurité - Formation obligatoire pour tous les techniciens. Date de prochaine session : 20 Décembre.")
    elif formation == "Maintenance Avancée":
        st.write(
            "Maintenance Avancée - Formation pour les techniciens de maintenance expérimentés. Date : 15 Janvier.")
    elif formation == "Énergie Renouvelable":
        st.write(
            "Énergie Renouvelable - Formation sur l'optimisation de la consommation énergétique. Date : 10 Février.")

    st.write("Compétences du personnel")
    personnel = {
        "Nom": ["Alice Dupont", "Bernard Martin", "Clara Petit"],
        "Poste": ["Technicien", "Chef d'équipe", "Technicien"],
        "Formations Complétées": ["Sécurité", "Sécurité, Maintenance Avancée", "Sécurité"]
    }
    personnel_df = pd.DataFrame(personnel)
    st.table(personnel_df)

# Page des ressources
elif page == "📚 Ressources":
    st.markdown("### 📚 Ressources Importantes")
    st.write("Consultez des ressources sur les bonnes pratiques, la sécurité et la maintenance en industrie.")

    # Guide des Bonnes Pratiques en Usine
    st.markdown("#### 📘 Guide des Bonnes Pratiques en Usine")
    st.write("""
    Ce guide fournit des informations cruciales sur les meilleures pratiques pour maintenir une usine sûre, propre et efficace.
    Vous pouvez [télécharger le guide complet ici](https://ansm.sante.fr/uploads/2020/10/20/2019-guide-bpf-mai-2019-3.pdf).
    """)

    # Guide de Sécurité en Usine
    st.markdown("#### 🛡️ Guide de Sécurité en Usine")
    st.write("""
    Ce guide aborde les éléments essentiels de sécurité. Pour consulter les normes de sécurité officielles et les politiques du groupe OCP, 
    veuillez visiter ce [lien vers les normes de sécurité OCP](https://www.ocpgroup.ma/fr/sustainability/politiques-standards).
    """)
elif page == "🤖 Assistant Virtuel":
    st.markdown("### 💬 Virtual Assistant")

    # Embed Botpress chatbot using iframe
    chatbot_url = "https://cdn.botpress.cloud/webchat/v2.2/shareable.html?configUrl=https://files.bpcontent.cloud/2024/11/10/22/20241110221032-TW88NITP.json"

    # Embedding the iframe within Streamlit
    components.html(
        f"""
        <iframe 
            src="{chatbot_url}" 
            width="100%" height="600" 
            style="border:none;">
        </iframe>
        """,
        height=600
    )

# Footer with version and theme color
st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align: center; font-size: 12px;'>Industrial Monitoring Dashboard v1.1 © 2024</p>",
                    unsafe_allow_html=True)