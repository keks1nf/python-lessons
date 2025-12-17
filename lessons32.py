import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("datasets\\titanic.csv")

fig, ax = plt.subplots(2, 2)

# 1
df['Pclass'].value_counts().sort_index().plot(kind='bar', ax=ax[0, 0])
ax[0, 0].set_title("Кількість пасажирів у кожному класі")
ax[0, 0].set_xlabel("Клас")
ax[0, 0].set_ylabel("Кількість")

# 2
df.groupby("Pclass")["Fare"].mean().plot(kind='bar', ax=ax[0, 1])
ax[0, 1].set_title("Середня ціна квитка в кожному класі")
ax[0, 1].set_xlabel("Клас")
ax[0, 1].set_ylabel("Середня ціна")

# 3
df["Age"].plot(kind='hist', bins=30, ax=ax[1, 0])
ax[1, 0].set_title("Гістограма віку пасажирів")
ax[1, 0].set_xlabel("Вік")
ax[1, 0].set_ylabel('Частота')

# 4
df.boxplot(column="Fare", by="Survived", ax=ax[1, 1])
ax[1, 1].set_title("Ціна квитка: врятовані vs неврятовані")
ax[1, 1].set_xlabel("Врятовані vs неврятовані")
ax[1, 1].set_ylabel("Вартість")
plt.suptitle("")

# 5
values = df['Survived'].value_counts().sort_index()
labels = ["Не вижив", "Вижив"]

plt.figure()
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Частка виживших / не виживших")

plt.show()

# # df = pd.DataFrame({
# #     'years': [2020, 2021, 2022, 2023],
# #     'income': [100, 120, 130, 160],
# # })
# #
# # # df.plot(x='years', y='income')
# #
# # # df.plot(kind='bar', x='years', y='income')
# #
# # df.plot(kind='scatter', x='years', y='income')
#
# df = sns.load_dataset("tips")
#
# print(df.info())
#
# # fix, ax = plt.subplots(2, 2)
# #
# # # чайові та рахунок
# #
# # ax[0, 0].scatter(df['total_bill'], df['tip'])
# # ax[0, 0].set_xlabel('Total Bill')
# # ax[0, 0].set_ylabel('Tip')
# # ax[0, 0].set_title('Total Bill/Tip')
# #
# # # Середні чайові по дням тижня
# # mean_tips = df.groupby('day')['tip'].mean()
# #
# # # mean_tips.plot(kind='bar', ax=ax[0, 1])
# #
# # ax[0, 1].bar(mean_tips.index, mean_tips.values, edgecolor='black', width=0.5)
# #
# # ax[0, 1].set_title('Середні чайові по дням тижня')
# #
# # # Гістограма розподілу суми рахунку
# # # df['total_bill'].hist(bins=30)
# # ax[1, 0].hist(df['total_bill'], bins=30)
# # ax[1, 0].set_xlabel('Total Bill')
# # ax[1, 0].set_ylabel('Count')
# # ax[1, 0].set_title('Total Bill/Tip')
# #
# # # 4. Порівняння чайових у курящих та некурящих
# # tips_smokers = df[df['smoker'] == 'Yes']['tip']
# # tips_nonsmokers = df[df['smoker'] == 'No']['tip']
# #
# # ax[1, 1].boxplot(
# #     [tips_smokers, tips_nonsmokers],
# #     labels=['Smoker', 'Non-Smoker']
# # )
# #
# # ax[1, 1].set_title('Чайові: ті, що курять VS ті, що не курять')
#
# counts = df['day'].value_counts()
# plt.pie(counts.values, labels=counts.index, autopct='%1.0f%%')
#
# plt.show()
