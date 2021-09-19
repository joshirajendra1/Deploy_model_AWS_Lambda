"""
Your module description
"""
import os
import ast
import torch
import pickle
import json
import pandas as pd
import numpy as np
from torch import nn
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error
from torch.utils.data import Dataset, DataLoader

# import model and data module for ML
from src.regression import Regression
from src.input_data import InputData

from model import PredictScore

def lambda_handler(event, context):
    """Sample pure Lambda function
    """

    print(event)
    predicted_score = PredictScore(event)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Your predicted output is " + str(predicted_score),
            }
        ),
    }



