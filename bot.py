
import streamlit as st
import openai
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(page_title="Industrial Monitoring Dashboard", layout="wide", initial_sidebar_state="expanded")

# Define custom CSS for pink-purple theme and icon styling
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

# Application title with central alignment and color
st.markdown("<h1 style='text-align: center;'>Industrial Monitoring Dashboard</h1>", unsafe_allow_html=True)
st.write("Welcome to the enhanced dashboard for intuitive monitoring and information access.")

# Sidebar with icons for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Menu", 
                        ["🏠 Home", "🆔 Identifiant", "⚙️ Département", "🤖 Assistant Virtuel"])

# Sidebar section for Departments with icons
st.sidebar.markdown("### 🏢 Departments")
department = st.sidebar.selectbox("Choose a department", [
    "🏭 Département de Production", 
    "🔧 Département de Maintenance Industrielle", 
    "🔬 Département de Recherche et Développement (R&D)", 
    "✅ Département Qualité et Conformité", 
    "🌍 Département Environnement, Santé et Sécurité (EHS)", 
    "🚚 Département Logistique et Chaîne d’Approvisionnement", 
    "👥 Département Ressources Humaines"
])

# Function to display department details
def display_department_info(department_name):
    if department_name == "🏭 Département de Production":
        st.markdown("### 🏭 Département de Production")
        st.write("""
        - **Rôle Principal** : Superviser et gérer l’ensemble du processus de fabrication de l’acide phosphorique et des engrais.
        - **Sous-divisions** :
            - **Unité d’Acide Phosphorique** : Conversion de la roche phosphatée en acide phosphorique.
            - **Unité d’Engrais** : Transformation en engrais spécifiques (DAP, MAP, TSP).
        - **Tâches** :
            - Contrôle des installations.
            - Maintien des standards de qualité.
            - Optimisation des processus.
        """)

    elif department_name == "🔧 Département de Maintenance Industrielle":
        st.markdown("### 🔧 Département de Maintenance Industrielle")
        st.write("""
        - **Rôle Principal** : Assurer le bon fonctionnement des machines.
        - **Sous-divisions** :
            - **Maintenance Mécanique** : Entretien des machines.
            - **Maintenance Électrique** : Réparation des circuits électriques.
            - **Instrumentation et Contrôle** : Calibration des instruments.
        - **Tâches** :
            - Programmation des maintenances.
            - Interventions d’urgence.
            - Gestion des pièces de rechange.
        """)

    elif department_name == "🔬 Département de Recherche et Développement (R&D)":
        st.markdown("### 🔬 Département de Recherche et Développement (R&D)")
        st.write("""
        - **Rôle Principal** : Innover pour améliorer les procédés et développer de nouveaux produits.
        - **Sous-divisions** :
            - **Développement de Procédés** : Amélioration des techniques de production.
            - **Innovation Produits** : Création de nouveaux engrais.
            - **Durabilité et Économie Circulaire** : Valorisation des sous-produits.
        - **Tâches** :
            - Tests en laboratoire.
            - Pilotage de projets de recherche.
            - Collaboration avec des universités.
        """)

    elif department_name == "✅ Département Qualité et Conformité":
        st.markdown("### ✅ Département Qualité et Conformité")
        st.write("""
        - **Rôle Principal** : Assurer la conformité des produits avec les normes internationales.
        - **Sous-divisions** :
            - **Contrôle de Qualité** : Test des matières premières et produits finis.
            - **Conformité Réglementaire** : Adaptation des processus aux réglementations.
        - **Tâches** :
            - Analyses chimiques et physiques.
            - Rédaction de rapports d’audit.
            - Formation du personnel.
        """)

    elif department_name == "🌍 Département Environnement, Santé et Sécurité (EHS)":
        st.markdown("### 🌍 Département Environnement, Santé et Sécurité (EHS)")
        st.write("""
        - **Rôle Principal** : Garantir la sécurité, minimiser l’impact environnemental, et promouvoir une culture de sécurité.
        - **Sous-divisions** :
            - **Sécurité au Travail** : Protocoles de sécurité et EPI.
            - **Environnement** : Suivi des émissions et gestion des déchets.
            - **Gestion des Situations d’Urgence** : Préparation et gestion des risques.
        - **Tâches** :
            - Formation des employés.
            - Réalisation de bilans environnementaux.
            - Assurer la conformité HSE.
        """)

    elif department_name == "🚚 Département Logistique et Chaîne d’Approvisionnement":
        st.markdown("### 🚚 Département Logistique et Chaîne d’Approvisionnement")
        st.write("""
        - **Rôle Principal** : Gérer les flux de matières premières et produits finis.
        - **Sous-divisions** :
            - **Approvisionnement** : Gestion des achats et réception des matières premières.
            - **Gestion des Stocks** : Suivi des niveaux de stocks.
            - **Expédition** : Organisation des expéditions.
        - **Tâches** :
            - Coordination avec les fournisseurs.
            - Gestion des coûts logistiques.
            - Planification des expéditions.
        """)

    elif department_name == "👥 Département Ressources Humaines":
        st.markdown("### 👥 Département Ressources Humaines")
        st.write("""
        - **Rôle Principal** : Gestion du personnel, recrutement, formation, et développement des talents.
        - **Sous-divisions** :
            - **Recrutement** : Sélection et intégration des candidats.
            - **Formation** : Développement des compétences techniques et managériales.
            - **Bien-être** : Promotion des programmes de bien-être.
        - **Tâches** :
            - Organisation des formations.
            - Gestion des carrières.
            - Suivi des indicateurs RH.
        """)

# Display content based on page and department selection
if page == "🏠 Home":
    st.markdown("## 👋 Welcome to the Industrial Dashboard")
    st.write("Monitor and manage your industrial sections here with enhanced visuals and rich metrics.")

elif page == "⚙️ Département":
    display_department_info(department)

elif page == "🤖 Assistant Virtuel":
    st.markdown("### 💬 Virtual Assistant")
    chatbot_url = "https://cdn.botpress.cloud/webchat/v2.2/shareable.html?configUrl=https://files.bpcontent.cloud/2024/11/10/22/20241110221032-TW88NITP.json"
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

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align: center; font-size: 12px;'>Industrial Monitoring Dashboard v1.1 © 2024</p>", unsafe_allow_html=True)
