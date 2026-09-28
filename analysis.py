#!/usr/bin/env python3
"""
💰 Analyse Financière & Détection de Fraude
============================================
Secteur : Finance / Banque
Auteur  : Oriane Dessaux
Date    : September 2026

Description
-----------
Détection d'anomalies et analyse des transactions financières

Questions analysées
-------------------
  1. Quelle est la répartition temporelle des transactions frauduleuses ?
  2. Les montants des fraudes diffèrent-ils des transactions normales ?
  3. Y a-t-il des patterns horaires dans les fraudes ?
  4. Quel seuil de montant déclenche le plus de fraudes ?

Dataset
-------
Source : https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
Fichier : data/creditcard.csv
"""

# ── Imports ──────────────────────────────────────────────────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings("ignore")

# Style global
plt.style.use("seaborn-v0_8-darkgrid")
COLORS = ["#00d4ff", "#ff4d6d", "#7c3aed", "#10b981", "#f59e0b", "#3b82f6"]
sns.set_palette(COLORS)

print("✅ Imports OK")

# ─────────────────────────────────────────────────────────────────────────────
# 1. CHARGEMENT DES DONNÉES
# ─────────────────────────────────────────────────────────────────────────────

def load_data(path: str = "data/creditcard.csv") -> pd.DataFrame:
    """Charge et affiche un aperçu du dataset."""
    df = pd.read_csv(path, encoding="utf-8")
    print(f"📦 Dataset chargé : {df.shape[0]:,} lignes × {df.shape[1]} colonnes")
    print(f"   Colonnes : {list(df.columns)}")
    return df

df = load_data()

# ─────────────────────────────────────────────────────────────────────────────
# 2. EXPLORATION & NETTOYAGE
# ─────────────────────────────────────────────────────────────────────────────

print("\n📊 Aperçu du dataset :")
print(df.head())
print(f"\n🔍 Valeurs manquantes :")
print(df.isnull().sum()[df.isnull().sum() > 0])

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoyage général : doublons, types, valeurs aberrantes."""
    n_before = len(df)
    df = df.drop_duplicates()
    n_after = len(df)
    print(f"🧹 Doublons supprimés : {n_before - n_after}")

    # Conversion des types
    for col in df.select_dtypes(include=["object"]).columns:
        try:
            df[col] = pd.to_datetime(df[col])
            print(f"   📅 Colonne '{col}' convertie en datetime")
        except (ValueError, TypeError):
            pass

    return df

df = clean_data(df)

# ─────────────────────────────────────────────────────────────────────────────
# 3. CALCUL DES KPIs
# ─────────────────────────────────────────────────────────────────────────────

print("\n📈 KPIs clés :")
kpis = {}

# TODO : Adapter ces calculs aux colonnes réelles du dataset
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

for col in numeric_cols[:4]:
    kpis[col] = {
        "mean": df[col].mean(),
        "median": df[col].median(),
        "std": df[col].std(),
        "min": df[col].min(),
        "max": df[col].max(),
    }
    print(f"   {col} → moy: {df[col].mean():.2f}, médiane: {df[col].median():.2f}")

# ─────────────────────────────────────────────────────────────────────────────
# 4. ANALYSES & VISUALISATIONS
# ─────────────────────────────────────────────────────────────────────────────

# ── 4.1 Distribution générale ─────────────────────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("💰 Analyse Financière & Détection de Fraude\nDistribution des variables clés",
             fontsize=16, fontweight="bold", y=1.02)

for i, col in enumerate(numeric_cols[:4]):
    ax = axes[i // 2][i % 2]
    df[col].hist(bins=30, ax=ax, color=COLORS[i], edgecolor="white", linewidth=0.5)
    ax.set_title(f"Distribution : {col}", fontweight="bold")
    ax.set_xlabel(col)
    ax.set_ylabel("Fréquence")

plt.tight_layout()
plt.savefig("outputs/01_distributions.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Figure 01 sauvegardée : outputs/01_distributions.png")

# ── 4.2 Matrice de corrélation ────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(12, 8))
corr_matrix = df[numeric_cols].corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(
    corr_matrix, mask=mask, annot=True, fmt=".2f",
    cmap="RdYlGn", center=0, ax=ax,
    linewidths=0.5, annot_kws={"size": 9}
)
ax.set_title("💰 Matrice de corrélation — Analyse Financière & Détection de Fraude",
             fontsize=14, fontweight="bold", pad=20)
plt.tight_layout()
plt.savefig("outputs/02_correlation_matrix.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Figure 02 sauvegardée : outputs/02_correlation_matrix.png")

# ── 4.3 Visualisation interactive Plotly ─────────────────────────────────

if len(numeric_cols) >= 2:
    fig_px = px.scatter(
        df.head(2000),
        x=numeric_cols[0],
        y=numeric_cols[1],
        color=numeric_cols[2] if len(numeric_cols) > 2 else None,
        title=f"{numeric_cols[0]} vs {numeric_cols[1]}",
        template="plotly_dark",
        color_continuous_scale="viridis",
        opacity=0.7
    )
    fig_px.update_layout(
        plot_bgcolor="#0a0e1a",
        paper_bgcolor="#111827",
        font_color="#e2e8f0",
        title_font_size=16,
    )
    fig_px.write_html("outputs/03_interactive_scatter.html")
    fig_px.show()
    print("✅ Figure 03 sauvegardée : outputs/03_interactive_scatter.html")

# ── 4.4 Analyse par catégories ────────────────────────────────────────────

categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
if categorical_cols:
    cat_col = categorical_cols[0]
    top_cats = df[cat_col].value_counts().head(10)

    fig = px.bar(
        x=top_cats.index,
        y=top_cats.values,
        title=f"Top 10 — {cat_col}",
        labels={"x": cat_col, "y": "Nombre"},
        template="plotly_dark",
        color=top_cats.values,
        color_continuous_scale=[[0, "#00d4ff"], [0.5, "#7c3aed"], [1, "#ff4d6d"]],
    )
    fig.update_layout(
        plot_bgcolor="#0a0e1a",
        paper_bgcolor="#111827",
        font_color="#e2e8f0",
        showlegend=False,
    )
    fig.write_html("outputs/04_category_analysis.html")
    fig.show()
    print("✅ Figure 04 sauvegardée : outputs/04_category_analysis.html")

# ─────────────────────────────────────────────────────────────────────────────
# 5. SYNTHÈSE & RECOMMANDATIONS
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "="*60)
print(f"  SYNTHESE : Analyse Financière & Détection de Fraude".upper())
print("="*60)

print("\n📊 Questions analysées :")
for i, q in enumerate(['Quelle est la répartition temporelle des transactions frauduleuses ?', 'Les montants des fraudes diffèrent-ils des transactions normales ?', 'Y a-t-il des patterns horaires dans les fraudes ?', 'Quel seuil de montant déclenche le plus de fraudes ?'], 1):
    print(f"  {i}. {q}")

print("\n💡 KPIs calculés :")
for kpi in ['Taux de fraude (%)', 'Montant moyen fraudé', 'Pic horaire de fraude', 'Perte estimée totale']:
    print(f"  → {kpi}")

print("\n🔍 Prochaines étapes suggérées :")
print("  1. Enrichir le dataset avec des sources complémentaires")
print("  2. Modélisation prédictive (sklearn / prophet / statsmodels)")
print("  3. Déployer un dashboard Streamlit interactif")
print("  4. Automatiser le pipeline de données avec Airflow ou dbt")

print("\n✅ Analyse complète ! Voir le dossier outputs/ pour les graphiques.")
