import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')
df.info()

# # 1
# sns.kdeplot(
#     data=df,
#     x="petal_length",
#     hue="species",
#     fill=True
# )
#
# plt.title("KDE-розподіл довжини пелюстки за видами")
# plt.xlabel("Довжина пелюстки")
# plt.ylabel("Щільність")
# plt.show()
#
# # 2
# sns.jointplot(
#     data=df,
#     x="sepal_length",
#     y="sepal_width",
#     hue="species"
# )
#
# plt.xlabel("Довжина чашолистика")
# plt.ylabel("Ширина чашолистика")
#
# plt.show()
# # 3
# sns.histplot(
#     data=df,
#     x="sepal_width",
#     hue="species",
#     kde=True
# )
#
# plt.title("Розподіл ширини чашолистка")
# plt.xlabel("Ширина чашолистка")
# plt.show()

# 4
corr = df.corr(numeric_only=True)

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Кореляції")
plt.show()
'''
petal_length і petal_width мають найбільшу кореляцію 
довші листки зазвичай і ширші

чашолистки майже не пов’язані між собою (sepal_length, sepal_width)
кореляція близька до 0

'''
