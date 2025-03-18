# Bank-loan-prediction

## A propos 
Bienvenue dans l'analyse **Analyse et la modélisation** d'éligibilté ou non d'un client. Dans le climat économique actuel,l'analyse de d'éligibilté ou non d'un client est plus pertinente que jamais. Les institutions financières sont continuellement confrontées au défi de distinguer les bons emprunteurs des mauvais pour minimiser les pertes tout en maximisant les opportunités de revenus.


## Objectif:

L'objectif de ce projet était de développer un modèle prédictif capable de classer les statuts de prêt et un interface web **Flask** qui permet de dire si le client est "éligible" ou "Non"  en fonction de quelques caractériqtiques du client.

## Structure du projet
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


## modelisation 

| modèles                |   précision |
|:-----------------------|------------:|
| Logistic Regression    |       0.854 |
| KNeighborsClassifier   |       0.699 |
| DecisionTreeClassifier |       0.846 |