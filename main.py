"""exercice 3:
1 . en python les variable doivent être declarées explicitement avec un type avant dêtre utilisées : Faux

2 . une fonction en python peut retoourner plusieurs valeurs : Vrai

3 . en programmation orientée objet, l'heritage permet à une classe d'acquérire les propriétés et methodes d'une autre classe: Vrai

4 . en python , on utilise le mot-clé 'private ' pour definir des attributs privés dans une classe : Faux

5 . le module 'csv' en python est utilisés pour manipuler des données au format JSON : Faux"""



 #exercice 1:
import csv
import matplotlib.pyplot as plt



# 1) Lecture du fichier CSV:
def lire_csv(nom_fichier):

 #Lit un fichier CSV et retourne une liste de dictionnaires:

 donnees = []
 with open(nom_fichier, mode='r', encoding='utf-8') as fichier:
  lecteur = csv.DictReader(fichier, delimiter=',')
  for ligne in lecteur:

   # Conversion des nombres en entiers:

   ligne['Cas'] = int(ligne['Cas'])
   ligne['Dèces'] = int(ligne['Dèces'])
   donnees.append(ligne)
 return donnees


# 2) Calculs statistiques les totaux et taux de mortalité par préfecture.
def calculer_statistiques(donnees):

 stats = {}
 for entree in donnees:
  pref = entree['Préfecture']
  if pref not in stats:
   stats[pref] = {'cas': 0, 'deces': 0}
  stats[pref]['cas'] += entree['Cas']
  stats[pref]['deces'] += entree['Dèces']

 # Calcul du taux de mortalité
 for pref in stats:
  cas = stats[pref]['cas']
  deces = stats[pref]['deces']
  stats[pref]['taux'] = deces / cas if cas > 0 else 0.0
 return stats

# 3) Visualisation:
def visualiser_donnees(stats):

 #Génère deux diagrammes : cas totaux et taux de mortalité.

 prefectures = list(stats.keys())
 cas = [stats[pref]['cas'] for pref in prefectures]
 taux = [stats[pref]['taux'] for pref in prefectures]

 # Diagramme des cas de totaux

 plt.figure(figsize=(10, 5))
 plt.bar(prefectures, cas, color='skyblue')
 plt.title('Nombre total de cas par préfecture')
 plt.xlabel('Préfecture')
 plt.ylabel('Cas')

 # Diagramme du taux de mortalité:

 plt.figure(figsize=(10, 5))
 plt.bar(prefectures, taux, color='salmon')
 plt.title('Taux de mortalité par préfecture')
 plt.xlabel('Préfecture')
 plt.ylabel('Taux (Décès/Cas)')
 plt.ylim(0, 1)

 plt.show()


# Exécution principale:
if __name__ == "__main__":
 donnees = lire_csv('ebola_guinea.csv')
 stats = calculer_statistiques(donnees)
 visualiser_donnees(stats)


