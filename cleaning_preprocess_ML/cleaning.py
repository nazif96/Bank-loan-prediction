import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import pickle 
import os 

from sklearn.preprocessing import LabelEncoder



def datacleaning(dataframe): 
    
    """ 
    Cette fonction permet de nettoyer les données en remplissant les valeurs manquantes 
    et supprimant les colonnes inutiles.
    args:
    dataframe : le dataframe à nettoyer
    """
    
    # Séparer les colonnes numériques et catégoriques
    cat_data_train = dataframe.select_dtypes(include=['object']).copy()
    num_data_train = dataframe.select_dtypes(exclude=['object']).copy()

    # Imputation des valeurs manquantes
    num_data_train.fillna(method='bfill', inplace=True)
    cat_data_train = cat_data_train.apply(lambda x: x.fillna(x.mode()[0]))

    # Suppression d'une colonne spécifique si elle existe
    if 'Loan_ID' in cat_data_train.columns:
        cat_data_train.drop(columns=['Loan_ID'], inplace=True)

    # Concaténation des DataFrames nettoyés
    df_cleaned = pd.concat([num_data_train, cat_data_train], axis=1)
    
    return df_cleaned



def save_cleaned_data(dataframe, path):
    """
    Sauvegarde un DataFrame sous forme de fichier CSV.
    Crée le dossier s'il n'existe pas.
    
    Args:
        dataframe (pd.DataFrame): Le DataFrame à sauvegarder.
        path (str): Le chemin du fichier CSV.
    """
    
    # Extraire le répertoire du fichier
    directory = os.path.dirname(path)
    
    # Créer le dossier s'il n'existe pas
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    try:
        # Sauvegarde du DataFrame
        dataframe.to_csv(path, index=False)
        print(f"✅ Fichier enregistré avec succès : {path}")
    except Exception as e:
        print(f"❌ Erreur lors de l'enregistrement du fichier : {e}")




def preprocess_data(dataframe): 
    """
    Cette fonction encode les variables catégoriques du DataFrame en valeurs numériques.
    
    Args:
        dataframe (pd.DataFrame): Le DataFrame contenant les données à prétraiter.
    
    Returns:
        pd.DataFrame: Le DataFrame avec les colonnes catégoriques encodées.
    """
    df_copy = dataframe.copy()  # Éviter de modifier l'original

    # Sélectionner les colonnes de type "object" (catégoriques)
    cat_cols = df_copy.select_dtypes(include=['object']).columns

    # Vérifier s'il y a des colonnes catégoriques à encoder
    if len(cat_cols) == 0:
        print("Aucune variable catégorique à encoder.")
        return df_copy

    # Appliquer l'encodage LabelEncoder sur chaque colonne catégorique
    for col in cat_cols:
        le = LabelEncoder()
        df_copy[col] = le.fit_transform(df_copy[col].astype(str))

    return df_copy
