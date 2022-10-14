from rebase import ModelChain, node
import pandas as pd


@node(inputs=['train_set', 'params'], outputs=['model'])
def train(train_set, params):
    # Train your model
    model = None
    return [
        model, # Model must be returned here
    ]


@node(inputs=['model', 'val_x'], outputs='result')
def predict(model, val_x):
    # Run predict
    # Must return a Pandas DataFrame with 'target' as column
    df = None
    return df


def init():
    # Define your pipelines
    # In this case we have two pipeliens, train and predict
    return dict(
        train=[train],
        infer=[predict]
    )