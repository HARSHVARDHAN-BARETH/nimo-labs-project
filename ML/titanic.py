import pandas as pd

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

train.drop(columns=['Cabin'], inplace=True)
train['Embarked'].fillna('S', inplace=True)

test.drop(columns=['Cabin'], inplace=True)
test['Age'].fillna(test['Age'].mean(), inplace=True)
train['Age'].fillna(train['Age'].mean(), inplace=True)

print(train.drop(columns=['Ticket', 'Fare'], inplace=True))
print(test.drop(columns=['Ticket', 'Fare'], inplace=True))

print(train.drop(columns=['Name'], inplace=True))
print(test.drop(columns=['Name'], inplace=True))

train['Family'] = train['SibSp'] + train['Parch'] + 1
test['Family'] = train['SibSp'] + train['Parch'] + 1

print(train['Family'].value_counts())
print(train.groupby(['Family'])['Survived'].mean())

def cal(number):
    if number == 1:
        return 'Alone'
    elif 1 < number < 5:
        return 'Medium'
    else:
        return 'Large'

train['Family_size'] = train['Family'].apply(cal)
test['Family_size'] = test['Family'].apply(cal)

train.drop(columns=['SibSp', 'Parch', 'Family'], inplace=True)
test.drop(columns=['SibSp', 'Parch', 'Family'], inplace=True)

passengerId = test['PassengerId'].values

train.drop(columns=['PassengerId'], inplace=True)
test.drop(columns=['PassengerId'], inplace=True)

sex_mapping = {"male": 0, "female": 1}
train['Sex'] = train['Sex'].map(sex_mapping)
test['Sex'] = test['Sex'].map(sex_mapping)

embarked_mapping = {"S": 1, "Q": 2, "C": 3}
train['Embarked'] = train['Embarked'].map(embarked_mapping)
test['Embarked'] = test['Embarked'].map(embarked_mapping)

family_mapping = {"Alone": 1, "Medium": 2, "Large": 3}
train['Family_size'] = train['Family_size'].map(family_mapping)
test['Family_size'] = test['Family_size'].map(family_mapping)

test_final = test.copy()

predictor = train.drop(columns=['Survived'])
target = train['Survived']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(predictor, target, test_size=0.2)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, Y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_pred, Y_test)

x_final = test_final[X_train.columns]
y_final = classifier.predict(x_final)

final = pd.DataFrame({'PassengerId': passengerId, 'Survived': y_final})
print(final)
