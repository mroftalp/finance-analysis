# 💰 Analyse Financière & Détection de Fraude

> **Secteur :** Finance / Banque | **Auteur :** Oriane Dessaux | **Date :** September 2026

![Finance](https://img.shields.io/badge/Finance-0a0e1a?style=flat&logoColor=00d4ff) ![Fraude](https://img.shields.io/badge/Fraude-0a0e1a?style=flat&logoColor=00d4ff) ![Anomalie](https://img.shields.io/badge/Anomalie-0a0e1a?style=flat&logoColor=00d4ff) ![Banque](https://img.shields.io/badge/Banque-0a0e1a?style=flat&logoColor=00d4ff) ![Risque](https://img.shields.io/badge/Risque-0a0e1a?style=flat&logoColor=00d4ff)

---

## 📋 Description

Détection d'anomalies et analyse des transactions financières

Ce projet d'analyse de données répond à **4 questions métier clés** à travers une exploration approfondie du dataset, des visualisations interactives et des recommandations actionnables.

## ❓ Questions analysées

1. Quelle est la répartition temporelle des transactions frauduleuses ?
2. Les montants des fraudes diffèrent-ils des transactions normales ?
3. Y a-t-il des patterns horaires dans les fraudes ?
4. Quel seuil de montant déclenche le plus de fraudes ?

## 📈 KPIs principaux

| KPI | Description |
|-----|-------------|
| **Taux de fraude (%)** | Calculé et visualisé dans le notebook |
| **Montant moyen fraudé** | Calculé et visualisé dans le notebook |
| **Pic horaire de fraude** | Calculé et visualisé dans le notebook |
| **Perte estimée totale** | Calculé et visualisé dans le notebook |

## 🗂️ Structure du projet

```
finance_analysis/
├── data/
│   └── creditcard.csv          # Dataset source
├── outputs/
│   ├── 01_distributions.png             # Distribution des variables
│   ├── 02_correlation_matrix.png        # Matrice de corrélation
│   ├── 03_interactive_scatter.html      # Scatter plot interactif
│   └── 04_category_analysis.html        # Analyse catégorielle
├── analysis.py                           # Script d'analyse principal
├── requirements.txt                      # Dépendances Python
└── README.md                             # Ce fichier
```

## 🚀 Installation & Utilisation

```bash
# 1. Cloner le repo
git clone https://github.com/orianedessaux/finance-analysis.git
cd finance-analysis

# 2. Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Télécharger les données
# Source : https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
# Placer le fichier CSV dans le dossier data/

# 5. Lancer l'analyse
python analysis.py
```

## 📊 Aperçu des visualisations

| Distribution des variables | Matrice de corrélation |
|:--------------------------:|:---------------------:|
| ![dist](outputs/01_distributions.png) | ![corr](outputs/02_correlation_matrix.png) |

> Les graphiques interactifs (HTML) se trouvent dans le dossier `outputs/`

## 🛠️ Stack technique

```python
import pandas
import matplotlib
import seaborn
import plotly
import sklearn
```

- **Analyse** : pandas, numpy
- **Visualisation statique** : matplotlib, seaborn
- **Visualisation interactive** : plotly
- **Environnement** : Python 3.11, Jupyter / VS Code

## 💡 Insights & Recommandations

L'analyse de ce dataset permet d'identifier des patterns clés dans le secteur **Finance / Banque**.
Les visualisations révèlent des tendances actionables pour les décideurs.

> 📌 Voir le script `analysis.py` pour le détail des calculs et les commentaires explicatifs.

## 📚 Sources

- Dataset : [https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Documentation pandas : https://pandas.pydata.org/docs/
- Plotly : https://plotly.com/python/

---

*Projet réalisé dans le cadre du développement du portfolio data analyst — September 2026*
*Auteur : [Oriane Dessaux](https://github.com/orianedessaux)*
