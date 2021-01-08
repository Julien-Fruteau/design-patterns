import argparse


class CommandExecutor:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("command", choices=["CreateOrder", "UpdateQuantity", "ShipOrder"])
        self.args = parser.parse_args()

    def execute_command(self):
        pass
