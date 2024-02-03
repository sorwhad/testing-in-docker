from unittest import TestCase, mock

from sklearn.datasets import load_digits

from nn.pipeline import Pipeline

import numpy as np


class TestPipelineCase(TestCase):

    @classmethod
    def setUpClass(cls):
        X, y = load_digits(return_X_y=True)
        cls.X = X
        cls.y = y

    @mock.patch(
            'nn.pipeline.Pipeline.model_path',
            new_callable=mock.PropertyMock(),
        )
    def setUp(self, mock_obj: mock.PropertyMock):
        mock_obj.return_value = 'test_models'
        self.pipeline = Pipeline(self.X[:100], self.y[:100])
    
    def test_overfit(self):

        for i in range(100):
            loss = self.pipeline.train_epoch(i)

        self.assertGreater(0.01, loss)

    def test_train_progress(self):

        losses_before = [
            self.pipeline.train_epoch(i) for i in range(5)
        ]

        losses_after = [
            self.pipeline.train_epoch(i) for i in range(5, 10) 
        ]
        
        self.assertLess(
            np.mean(losses_after), np.mean(losses_before)
        )
        