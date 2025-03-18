# 💰Bank-loan-prediction

## A propos 
Bienvenue dans l'analyse **Analyse et la modélisation** d'éligibilté ou non d'un client. Dans le climat économique actuel,l'analyse de d'éligibilté ou non d'un client est plus pertinente que jamais. Les institutions financières sont continuellement confrontées au défi de distinguer les bons emprunteurs des mauvais pour minimiser les pertes tout en maximisant les opportunités de revenus.

 

## 🎯 Objectif:

L'objectif de ce projet était de développer un modèle prédictif capable de classer les statuts de prêt et un interface web **Flask** qui permet de dire si le client est "éligible" ou "Non"  en fonction de quelques caractériqtiques du client.

## 🗃️Structure du projet
Le projet est organisé comme suit :

```
Bank-loan-prediction
├── cleaning_preprocess_ML/  # package pour nettoyage et pretraitement des données 
│   ├── __init__.py
│   ├── data_cleaning.py 
|
├── Credit_app/  # dossier de l'interface flask de prediction 
│   ├── .idea/
│   ├── .venv/
│   ├── App_deploiment/
│      ├── static 
│      ├── templates
│      ├── app.py    # l'interface flask pour prédire éligibilité d'un client à un prêt 
│      ├── model.pkl  #modèle entraîné et retenu pour la prediction 
│      ├── model.pkl1
│      ├── requirements.txt
|
├── dataset/
│   ├── train.csv  # Données brutes utilisées pour le projet 
│   ├── train_cleaned.csv # Données propres 
|
├── Notebooks/
│   ├── data_cleaning.ipynb # jupyter Notebook pour le nettoyage des données
│   ├── EDA.ipynb           # jupyter Notebook pour l'analyse exploratoire 
│   ├── model.pkl
│   ├── model.pkl1
│   ├── preprossed_ML.ipynb # jupyter Notebook pour le pretaritement et l'entraînement des modèles
│   ├── resultat.csv # sauvegarde de la precission des modèles
|
├── venv/
├── poetry.lock 
├── LICENSE
├── Présentation.ipynb
├── pyproject.toml
├── README.md
└── requirements.txt 
```  


## Mise en place du modèle prédictif 

### 1. Chargement des données
Les données ont éte chargées à partir du fichier  `dataset/train_data.csv ` qui contient les informations telles que :
- **Le genre, , revenu du demandeur, revenu du conjoint** etc 
-  **status de prêt** (Cible) indiquant si le prêt est accordé (Y) ou pas (N)

### 2. Nettoyage des données 
- **Nettoyage des données** : Gestion des valeurs manquantes, suppression des varibales unitiles dans `Notebooks/data_cleaning.ipynb`

### 3. Analyse Exploratoire (EDA)
- **Analyse UNivariée et Bivariée** pour comprendre la distribution des variables  et leur relation avec `Loan_status`
- **Visualisations** pour identifier les tendances et les schemas pertinents

### 4- Prétraitement des données 
- **Encodage des variables catégorielles** : Utilisation de techniques d'encodage adaptés (Label Encoding)

### 5- Création et entrainements du modèle 
 - **Modèles entrainé** :
  - Logistic Regression
  - KNeighborsClassifier
  - DecisionTreeClassifier

### 6- Evaluation du modèle (accuracy)

| modèles                |   précision |
|:-----------------------|------------:|
| Logistic Regression    |       0.854 |
| KNeighborsClassifier   |       0.699 |
| DecisionTreeClassifier |       0.846 |

## Installation 

### Prérequis 
- **PyCharm Community** installé.  # utiliser pour developper l'interface flask 
- **Pip** pour la gestion des packages 

**Etapes** 
1. **Clonez  le Dépôt** 

```bash 
git clone https://github.com/nazif96/Bank-loan-prediction.git

```
2. **Specifiez environnement virtuel** 

3. **Deplacez dans le dossier**

```bash
cd Credit_app 
cd App_deploiment 

```
4. **Installez les dépendances**

```bash
pip install -r requirements.txt 

```

### 🚀Utilisation 

1. **Lancez l'interface flask de simulation de l'éligibilité du client**

```bash
python app.py

```

![Credit_app](https://github.com/nazif96/Bank-loan-prediction/blob/main/Credit_app/credit_APP.png)

2. **renseignez les données puis lancez la prediction** 

## 👤Auteur
**AFOLABI Nazifou**

- **Datascientist | Machine Learning & Modeling** 
- Passionné par les sciences de données et l'intelligence artificielle.
- **Email** : [afolabinazif96@gmail.com](mailto.afolabinazif96@gmail.com)
- **LinkedIn** : [Nazifou AFOLABI](https://www.linkedin.com/in/nazifou-afolabi-10544729b/)



