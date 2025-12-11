import pandas as pd

titanic_df = pd.read_csv('datasets\\titanic.csv')

# 1.
over_50 = titanic_df[titanic_df['Age'] > 50][['Name', 'Age', 'Pclass']]
print("Пасажири віком понад 50 років:")
print(over_50)

# 2.
female_first_class = titanic_df[(titanic_df['Sex'] == 'female') & (titanic_df['Pclass'] == 1)][['Name', 'Survived']]
print("\nЖінки з 1 класу та їх виживання:")
print(female_first_class)

# 3
sorted_by_age = titanic_df.sort_values("Age", ascending=True)
print('Перші 10 рядків відсортованої таблиці за віком.')
print(sorted_by_age.head(10))

# 4.
youngest_3rd_class = titanic_df[titanic_df['Pclass'] == 3].sort_values('Age').head(5)
print("\n5 наймолодших пасажирів 3 класу:")
print(youngest_3rd_class[['Name', 'Age']])

# 5
'''
Подсчёт количества значений
Для того чтобы подсчитать количество значений в конкретном столбце, можно воспользоваться следующей конструкцией:
anime.type.value_counts()
'''

counts = titanic_df['Pclass'].value_counts()
print("Кількість пасажирів у кожному класі (Pclass):")
print(counts)

# 6.
mean_age_survived = titanic_df.groupby('Survived')['Age'].mean()
print("\nСередній вік пасажирів (вижив / не вижив):")
print(mean_age_survived)

# 7.
'''
s = pd.DataFrame(df.groupby(['Sex', 'Pclass'])['PassengerId'].count().
                 reset_index())
f = s[s.Sex == 'female'] 
f['ratio'] = f.PassengerId/f.PassengerId.sum()*100
m = s[s.Sex == 'male']
m['ratio'] = m.PassengerId/m.PassengerId.sum()*100 
'''

survived_counts = (
    titanic_df[titanic_df['Survived'] == 1].groupby(['Sex', 'Pclass'])['PassengerId'].count().reset_index(name='Count')
)
print("\nКількість чоловіків і жінок, що вижили, в кожному класі:")
print(survived_counts)

f = survived_counts[survived_counts['Sex'] == 'female']
m = survived_counts[survived_counts['Sex'] == 'male']
print('Кількість жінок, що вижили, в кожному класі:')
print(f)
print('Кількість чоловіків, що вижили, в кожному класі:')
print(m)

'''
Типи даних Pandas:
1. Series - одномірний масив (вектор)
2. DataFrame - двомірний масив (таблиця)
'''

# 1. Series

l = [1, 10, 21, 35, 47, 69, 100]
d = {'Bob': 26, 'Anna': 20, 'Jason': 15}

series_1 = pd.Series(l)
series_2 = pd.Series(d)
series_3 = pd.Series(data=[1, 2, 3], index=['x', 'y', 'z'])

print(series_3)

# 2. DataFrame

data1 = {
    'Name': ['Bob', 'Anna', 'Alice'],
    'Age': [20, 25, 30],
    'Salary': [45000, 22000, 17000]
}

data2 = [
    {'Name': 'Bob', 'Age': 25, 'Salary': 26000},
    {'Name': 'Alice', 'Age': 17, 'Salary': 1000},
    {'Name': 'John', 'Age': 28, 'Salary': 20000}
]

data3 = [
    ['Bob', 30, 15000],
    ['Alice', 26, 35000],
    ['Jason', 60, 8100]
]

dataframe_1 = pd.DataFrame(data1)
dataframe_2 = pd.DataFrame(data2)

dataframe_3 = pd.DataFrame(data3, columns=['Name', 'Age', 'Salary'])

print(dataframe_3)

# 3. Робота з CSV
titanic_df = pd.read_csv('datasets\\titanic.csv')

print(titanic_df.info())
print(titanic_df['Name'])  # отримуємо всі записи в одній колонці
print(titanic_df[['Name', 'Age', 'Sex']])  # кілька колонок

print(titanic_df[titanic_df['Age'] > 20][['Name', 'Pclass']])  # рядки, у яких вік > 20 (тільки колонки Name, Pclass)

print(titanic_df.sort_values('Age'))  # сортування по колонці
print(titanic_df.sort_values('Age', ascending=False))  # сортування по колонці

print(
    titanic_df.sort_values(['Age', 'Survived']))  # сортування по кільком колонкам(спочатку вік, потім статус виживання)
print(titanic_df.sort_values(['Survived', 'Age'], ascending=[False, True]))

print(titanic_df['Age'].mean())  # агрегаційна функція mean
print(titanic_df.groupby('Sex')['Age'].mean())  # середній вік по статі

print(titanic_df['Survived'].sum())
print(titanic_df.groupby('Pclass')['Sex'].count())

# Завдання: знайти імена всіх жінок, що вижили
only_women = titanic_df[(titanic_df['Sex'] == 'female') & (titanic_df['Survived'] == 1)]  # & - і, | - або
print(only_women.sort_values('Age', ascending=False)[['Name', 'Age']])

titanic_df.head(5)  # перші 5
titanic_df.tail(5)  # останні 5

"""
1. Імпорт та читання даних
import pandas as pd

df = pd.read_csv('data.csv')
df = pd.read_excel('file.xlsx')
df = pd.read_json('file.json')

📌 2. Огляд даних
df.head()          # перші рядки
df.tail()          # останні рядки
df.info()          # типи даних + пропуски
df.describe()      # числова статистика
df.shape           # (rows, columns)
df.columns         # назви колонок
df.index           # індекс

📌 3. Вибір колонок
df['Age']
df[['Name', 'Age']]

📌 4. Фільтрація
df[df['Age'] > 50]
df[(df['Age'] > 20) & (df['Sex'] == 'female')]
df[df['Cabin'].isna()]     # пропуски
df[df['Cabin'].notna()]    # без пропусків

📌 5. Сортування
df.sort_values('Age')
df.sort_values('Age', ascending=False)
df.sort_values(['Pclass', 'Age'], ascending=[True, False])

📌 6. Додавання нових колонок
df['Age2'] = df['Age'] ** 2
df['FullName'] = df['Name'] + ' (' + df['Sex'] + ')'

📌 7. Видалення
df.drop('Cabin', axis=1)        # колонку
df.drop([0, 1, 2], axis=0)      # рядки
df.dropna()                     # видалити всі NaN
df.dropna(subset=['Age'])       # де Age = NaN

📌 8. Заповнення пропусків
df['Age'].fillna(df['Age'].median(), inplace=True)
df.fillna(0)              # заповнити всі

📌 9. Групування (groupby)
df.groupby('Pclass')['Age'].mean()
df.groupby(['Sex', 'Pclass'])['PassengerId'].count()
df.groupby('Embarked').agg({'Fare': ['mean', 'max']})

📌 10. Перерахунок індексу
df.reset_index(drop=True)
df.set_index('PassengerId')

📌 11. Унікальні значення
df['Sex'].unique()
df['Sex'].value_counts()

📌 12. Об’єднання таблиць
pd.concat([df1, df2])                      
pd.merge(df1, df2, on='id')               
pd.merge(df1, df2, how='left', on='id')   

📌 13. Робота з рядками
df['Name'].str.contains('Mr')
df['Name'].str.upper()
df['Name'].str.len()

📌 14. Лямбда-функції (apply)
df['AgeGroup'] = df['Age'].apply(lambda x: 'Old' if x > 50 else 'Young')

📌 15. Робота з датами
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

📌 16. Зведені таблиці (pivot table)
df.pivot_table(values='Fare', index='Pclass', columns='Sex', aggfunc='mean')

📌 17. Вибір топ-N
df.nlargest(5, 'Age')
df.nsmallest(5, 'Fare')

📌 18. Умовні значення (np.where)
import numpy as np
df['IsChild'] = np.where(df['Age'] < 18, 1, 0)

📌 19. IQR — знаходження викидів
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df['Age'] < Q1 - 1.5*IQR) | (df['Age'] > Q3 + 1.5*IQR)]

📌 20. Часті агрегації
df.agg({'Age': ['mean', 'median'], 'Fare': ['min', 'max']})

📘 Бонус: 10 найважливіших команд
df.head()
df.info()
df.describe()
df.sort_values(...)
df.groupby(...).agg(...)
df.isna().sum()
df.fillna(...)
df.drop(...)
df.merge(...)
df.pivot_table(...)

"""
print(titanic_df['Age'].min())
print(titanic_df['Age'].max())

print(titanic_df['Age'].std())

print(titanic_df['Age'].size)

# Скільки людей у кожному класі
print(titanic_df.groupby('Pclass')['PassengerId'].count())

# Скільки людей кожної статі вижило
print(titanic_df.groupby(['Sex', 'Pclass'])['Survived'].sum())

# Середній вік та середній тариф (сер та медіана) для кожного класу
print(titanic_df.groupby('Pclass')[['Age', 'Fare']].agg(['mean', 'median']))

# Перейменування

# titanic_df = titanic_df.rename(columns={'PassengerId': 'id', 'Survived': 'survived'})

# titanic_df.columns = (titanic_df.columns.str.lower().str.strip())

# Видалення

# titanic_df = titanic_df.drop(columns=['Cabine', 'Ticket'])
# print(titanic_df.info())

# Чистка тексту

# titanic_df['Name'] = titanic_df['Name'].str.lower()
# print(titanic_df['Name'])

# titanic_df['lower_name'] = titanic_df['Name'].str.lower()
# print(titanic_df.info())

# Робота з пропусками

print(titanic_df.isna().sum())

titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].median())
# заповнення пустих значень (inplace міняє вихідний DF, а не повертає результат)
titanic_df['Cabin'] = titanic_df['Cabin'].fillna('Unknown')

# 5. Робота з датами (на абстрактному фреймі df)
# df['Date'] = pd.to_datetime(df['Date'], format='%d|%m|%Y')  # перетворення на Дату

# 6. Перетворення даних
# titanic_df['Age'] = titanic_df['Age'].astype('int')

# 7 Нові колонки на основі категорій

titanic_df['age_group'] = pd.cut(
    titanic_df['Age'],
    [0, 10, 20, 40, 60, 100],
    labels=['Дитина', 'Молодий', 'Дорослий', 'Похилого віку', 'Старий']
)

# conditions = [
#     titanic_df['age'] < 10,
#     (titanic_df['age'] >= 10) & (titanic_df['age'] < 20),
#     (titanic_df['age'] >= 20) & (titanic_df['age'] < 60),
#     (titanic_df['age'] >= 60)
# ]
#
# choices = [
#     'Дитина',
#     'Підліток',
#     'Дорослий',
#     'Похилого віку'
# ]
#
# titanic_df['age_group'] = np.select(condlist=conditions,
#                                     choicelist=choices,
#                                     default='Невідомо')  # другий спосіб (гнучкий)

# def classify_age(age):
#     if pd.isna(age):
#         return 'Невідомо'
#
#     if age < 10:
#         return 'Дитина'
#
#     if age < 20:
#         return 'Підліток'
#
#     if age < 60:
#         return 'Дорослий'
#
#     return 'Похилого віку'
#
#
# titanic_df['age_group'] = titanic_df['age'].apply(classify_age)

print(titanic_df)

# 1
a_names = titanic_df[titanic_df['Name'].str.startswith('A')]
print(a_names[['Name', 'Age', 'Pclass']])

# 2
age_stats = titanic_df.groupby('Pclass')['Age'].agg(['min', 'max'])
print(age_stats)

# 3
stats = titanic_df.groupby('Pclass').agg({
    'Age': 'mean',
    'Fare': 'mean',
    'Survived': 'mean'
})

# відсотки
stats['Survived'] = stats['Survived'] * 100
print(stats)

# 4
top10_fare = titanic_df.sort_values('Fare', ascending=False).head(10)
print(top10_fare)

# 5
titanic_df["FamilySize"] = titanic_df["SibSp"] + titanic_df["Parch"] + 1

titanic_df["IsAlone"] = (titanic_df["FamilySize"] == 1).astype(int)

stats_by_sex = titanic_df.groupby("Sex").agg({
    "Age": "mean",
    "Fare": "mean",
    "Survived": "mean",
    "FamilySize": "mean"})

stats_by_sex["Survived"] *= 100

print(stats_by_sex)

'''''
             Age       Fare   Survived  FamilySize
Sex                                                
female  27.929936  44.479818  74.203822    2.343949
male    30.126811  25.523893  18.890815    1.665511

         mean_age  mean_fare  survived_percent  mean_family_size
Sex                                                             
female  27.929936  44.479818         74.203822          2.343949
male    30.126811  25.523893         18.890815          1.665511

'''
