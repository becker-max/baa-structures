import config

class DTC():

    def __init__(self):
        self.conn = "DB-Connection etc."
        self.params = "Hyperparameters"

    def __connect(self):
        pass

    def __disconnect(self):
        pass

    def set_connection(self,connection):
        self.conn=connection

    def train(self):
        print("trained DTC")

    def predict(self):
        print("DTC predicted something")

    def accuracy(self):
        print("i am very accurate")
