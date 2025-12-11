import pandas as pd

df = pd.read_csv(
    "datasets/data_global_data.csv",
    parse_dates=["date"],
    date_format="%m/%d/%y"
)

print(df.head())

# 1. Країни за загальною кількістю смертей
print("\n\n--- 1. Загальна кількість смертей по країнах ---")
total_deaths_by_country = (df.groupby("country")["deaths"].sum().sort_values(ascending=False))
print(total_deaths_by_country)

# 2. День з найбільшою кількістю смертей для кожної країни
print("\n\n--- 2. День з найбільшою кількістю смертей у кожній країні ---")
idx = df.groupby("country")["deaths"].idxmax()
max_deaths_per_country = df.loc[idx][["country", "date", "deaths"]].sort_values("country")
print(max_deaths_per_country)

# 3. Найбільш постраждала країна кожного дня
print("\n\n--- 3. Найбільш постраждала країна кожного дня ---")
daily_max = df.loc[df.groupby("date")["deaths"].idxmax()][["date", "country", "deaths"]]
daily_max = daily_max.sort_values("date")
print(daily_max)

# 4. Сумарна кількість смертей за весь час
print("\n\n--- 4. Загальна кількість смертей за весь період ---")
total_deaths = df["deaths"].sum()
print("Сумарна кількість смертей:", total_deaths)

'''
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
df.loc вибрати дані за мітками (іменами) рядків або колонок, вибрати рядки з таблиці за індексами всередині [...].

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
df.groupby("country")["deaths"].idxmax() індекс рядка,з макс значенням

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
