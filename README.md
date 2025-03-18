# Bank-loan-prediction

## A propos 
Bienvenue dans l'analyse **Analyse et la modélisation** d'éligibilté ou non d'un client. Dans le climat économique actuel,l'analyse de d'éligibilté ou non d'un client est plus pertinente que jamais. Les institutions financières sont continuellement confrontées au défi de distinguer les bons emprunteurs des mauvais pour minimiser les pertes tout en maximisant les opportunités de revenus.


## Objectif:

L'objectif de ce projet était de développer un modèle prédictif capable de classer les statuts de prêt et un interface web **Flask** qui permet de dire si le client est "éligible" ou "Non"  en fonction de quelques caractériqtiques du client.

## Structure du projet
Le projet est organisé comme suit :

```
Bank-loan-prediction
├── cleaning_preprocess_ML/
│   ├── __init__.py
│   ├── data_cleaning.py
|
├── Credit_app/
│   ├── .idea/
│   ├── .venv/
│   ├── App_deploiment/
│      ├── static 
│      ├── templates
│      ├── app.py
│      ├── model.pkl
│      ├── model.pkl1
│      ├── requirements.txt
|
├── dataset/
│   ├── train.csv
│   ├── train_cleaned.csv
|
├── Notebooks/
│   ├── data_cleaning.ipynb
│   ├── EDA.ipynb
│   ├── model.pkl
│   ├── model.pkl1
│   ├── preprossed_ML.ipynb
|
├── venv/
├── LICENSE
├── Présentation.ipynb
└── README.md
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
 - **Modèles** :
  - Logistic Regression
  - KNeighborsClassifier
  - ecisionTreeClassifier

### 6- Evaluation du modèle (accuracy)

| modèles                |   précision |
|:-----------------------|------------:|
| Logistic Regression    |       0.854 |
| KNeighborsClassifier   |       0.699 |
| DecisionTreeClassifier |       0.846 |

### Installation 