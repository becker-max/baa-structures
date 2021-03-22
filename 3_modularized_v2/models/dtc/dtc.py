from util import config

class DTC():

    def __init__(self):
        self.config = config
        self.params = "set Hyperparameters"

    def get_params(self):
        return self.params

    def train(self):
        print("trained DTC")

    def predict(self):
        print("DTC predicted something")

    def accuracy(self):
        print("i am very accurate")
