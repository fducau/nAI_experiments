import pandas as pd

def load_numerai_data():
    train = pd.read_csv('./numerai_training_data.csv')
    test = pd.read_csv('./numerai_tournament_data.csv')

    xtrain = train[train.columns.drop('target')]
    ytrain = train.target

    xtest = pd.read_csv('./numerai_tournament_data.csv',index_col=0)
    
    return xtrain, ytrain, xtest
