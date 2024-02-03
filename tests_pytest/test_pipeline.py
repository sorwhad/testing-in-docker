import numpy as np
import pytest
from sklearn.datasets import load_digits

from nn.pipeline import Pipeline


@pytest.fixture(scope='module')
def dataset():
    return load_digits(return_X_y=True)


@pytest.fixture(scope='function')
def pipeline(dataset):
     # setUp
    X, y = dataset
    pipeline = Pipeline(X[:100], y[:100])

    yield pipeline

    # tearDown


def test_overfit(pipeline):
    for i in range(100):
        loss = pipeline.train_epoch(i)

    assert loss < 0.01


def test_train_progress(pipeline):

    losses_before = [
        pipeline.train_epoch(i) for i in range(5)
    ]

    losses_after = [
        pipeline.train_epoch(i) for i in range(5, 10) 
    ]
    
    assert np.mean(losses_after) < np.mean(losses_before)
