import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

# train_data = pd.read_csv('../Titanic/train.csv', encoding="cp1251", sep=";")ФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФ
# test_data = pd.read_csv('../Titanic/test.csv', encoding="cp1251", sep=";")

train_data = pd.read_csv('../Titanic/train.csv')
test_data = pd.read_csv('../Titanic/test.csv')

print("Размер обучающей выборки: ", train_data.shape, "\n")
print("Количество пустых ячеек:\n", train_data.isnull().sum(), "\n")

# Количество выживших/погибших
sns.countplot(x='Survived', data=train_data)
plt.show()

# Факторы выживаемости
sns.countplot(x='Survived', hue='Gender', data=train_data)
plt.show()

sns.countplot(x='Survived', hue='Pclass', data=train_data)
plt.show()

sns.countplot(x='Survived', hue='SibSp', data=train_data)
plt.show()

sns.countplot(x='Survived', hue='Parch', data=train_data)
plt.show()

# PassengerId,Pclass,Name,Gender,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
features = ['Gender', 'Pclass', 'SibSp', 'Parch']

# Колонка "Survived"
y = train_data['Survived']

# Приведение столбца гендера в числовую форму, подготовка переменных
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])


model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)  # обучаем модель
prediction = model.predict(X_test)  # делаем предсказание

# строим дерево, выводим на экран
from sklearn import tree
plt.figure(figsize=(20,20))
_ = tree.plot_tree(model.estimators_[0], feature_names=X.columns, filled=True)
plt.show()

# формируем итоговый датафрейм и сохраняем его в csv файл
output = pd.DataFrame({'PassengerId':test_data.PassengerId, 'Survived':prediction})
output.to_csv('result.csv', index=False)