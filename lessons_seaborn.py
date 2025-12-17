import seaborn as sns

# df = sns.load_dataset('tips')
#
# sns.scatterplot(x='total_bill', y='tip', hue='sex', data=df, style='smoker', size='size', sizes=(50, 100))
# print(df.info())
#
# plt.show()
#
# sns.lineplot(
#     x='day',
#     y='tip',
#     data=df,
#     hue='sex'
# )
# plt.show()


'''
1. Кількісна змінна (числова):
- scatterplot: точковий 
- lineplot: лінійний
- pairplot: порівнює всі кількісні змінні (або ті, що передали)
- jointplot: взаємозв'язок кількісних змінних
- heatmap: кореляція числових змінних
- histplot, kdeplot: розподіл даних

2. Категоріальна змінна:
- barplot, boxplot
- stripplot - точковий графік по окремій категорії
- swarmplot - аналог stripplot, точки не зливаються
'''

df = sns.load_dataset('penguins')
print(df.info())

# # ----Barplot
# sns.barplot(
#     data=df,
#     x='species',
#     y='body_mass_g',
#     hue='sex'
# )

# # ----Jointplot
# sns.jointplot(
#     data=df,
#     x='body_mass_g',
#     y='bill_length_mm',
#     hue='species'
# )

# # ----Violinplot
# # sns.violinplot(
# #     data=df,
# #     x='species',
# #     y='body_mass_g',
# #     hue='sex'
# # )
#
# sns.violinplot(
#     data=df,
#     x='island',
#     y='body_mass_g',
#     hue='species'
# )

# # ----Histogram
# sns.histplot(
#     data=df,
#     x='body_mass_g',
#     bins=20,
#     kde=True,
#     hue='sex'
# )

# # ----Pairplot
# sns.pairplot(df, hue='species', vars=['body_mass_g', 'flipper_length_mm'])

# ----Heatmap
# corr = df.corr(numeric_only=True)
#
# sns.heatmap(
#     data=corr,
#     annot=True,
#     cmap='coolwarm'
# )
#
# plt.show()
#
# sns.kdeplot(
#     data=df,
#     x='body_mass_g',
#     fill=True,
#     hue='species'
# )
# plt.show()
