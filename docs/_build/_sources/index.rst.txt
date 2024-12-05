.. Projet IA Indus documentation master file, 

Bienvenue dans la documentation de Projet IA Indus
==================================================

Ce projet consiste en la création d'un tableau de bord de surveillance industrielle avec un assistant virtuel (chatbot). Ce document présente les principales étapes, fonctionnalités et technologies utilisées dans le développement du projet.

**Réalisé par :**  
- Drief Nisrine  
- Marwa Chouacha  

**Encadré par :**  
Mr. Masrour  

Objectif
--------

Développer une application industrielle comprenant :
- Un tableau de bord interactif développé avec Streamlit.
- Un chatbot basé sur Botpress pour assister les utilisateurs avec des informations sur l'entreprise, l'historique des pannes, et les protocoles de sécurité.

Pipeline du projet
------------------

1. **Collecte et préparation des données :**
   - Sources : PDF fournis par un agent OCP, fichiers texte générés par ChatGPT, site officiel de l'entreprise.
2. **Développement de l'interface Streamlit :**
   - Visualisation des données industrielles.
   - Fonctionnalités clés : suivi des pannes, alertes, KPI (MTBF, MTTR, efficacité globale).
3. **Développement et entraînement du chatbot :**
   - Créé avec Botpress, une plateforme open-source pour le développement de chatbots.
4. **Visualisation des résultats sur l'application :**
   - Intégration des graphiques et du chatbot dans l'interface Streamlit.

Collecte de données
-------------------

Les données utilisées dans le projet proviennent de plusieurs sources :
- Rapports de stage et documents PDF.
- Informations issues du site officiel de l'entreprise.
- Fichiers texte pour enrichir les réponses du chatbot.

Développement de l'interface Streamlit
--------------------------------------

Le tableau de bord industriel inclut :
- **Page d'accueil :**
  - Données sur l'efficacité actuelle.
  - Historique des pannes détectées et alertes actives.
  - Guide d'intervention et coordonnées de l'assistance technique.
- **Département :**
  - Visualisation des tâches et objectifs par département.
- **KPI :**
  - Indicateurs clés (MTBF, MTTR).
  - Visualisation graphique de l'efficacité.
- **Formation du personnel :**
  - Informations sur les formations prévues, liste des inscrits.
- **Ressources :**
  - Guides de bonnes pratiques et de sécurité.

Développement du chatbot
------------------------

**Technologie utilisée :** Botpress  
- **Fonctionnalités principales :**
  - Interface visuelle pour concevoir les conversations.
  - Base de connaissances importée depuis divers supports.
  - Formation des modèles NLP directement dans Botpress.
  - Intégration des LLM (comme GPT-3.5).
- **Fonctionnement logique :**
  - Réponses basées sur une recherche dans la base de données.
  - Interaction en boucle jusqu'à la fin de la conversation.

Test du chatbot
---------------

Le chatbot est intégré et testé dans le code source. Les réponses et l'interface sont optimisées pour garantir une expérience utilisateur fluide.

Publication
-----------

- **Code source :** Hébergé sur GitHub.  
- **Documentation :** Publiée sur Read the Docs.

Fin de documentation
--------------------
Pour en savoir plus sur le projet et son architecture, consulte le code source sur GitHub ou la documentation technique complète.
