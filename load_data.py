import pandas as pd

def load_numerai_data():
    train = pd.read_csv('./numerai_training_data.csv')
    test = pd.read_csv('./numerai_tournament_data.csv')

    xtrain = train[train.columns.drop('target')]
    ytrain = train.target

    xtest = test[test.columns.drop('t_id')]
    t_id = test.t_id

    return xtrain, ytrain, xtest, t_id

