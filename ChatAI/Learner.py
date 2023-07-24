import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv('../Titanic/train.csv')
test_data = pd.read_csv('../Titanic/test.csv')
features = ['Gender', 'Pclass', 'SibSp', 'Parch']