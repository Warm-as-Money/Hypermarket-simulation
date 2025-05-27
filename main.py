import json
import os
import time
import sys

class User:
    def __init__(self, name, wallet, assets, balance):
        self.name = name
        self.wallet = wallet
        self.assets = assets
        self.balance = balance

def type_print(text, delay=0.5):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def load_user(name):
    filename = f"{name}.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
            return User(**data) # Taking the dictionary into the class
    else:
        return None
    
def save_user(user):
    data = {
        "name": user.name,
        "wallet": user.wallet,
        "assets": user.assets,
        "balance": user.balance,
    }
    with open(f"{user.name}.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    name = input("Enter your username: ")
    user = load_user(name)
    if user is None:
        print("Welcome to the Hypermarket Simulation!")
        wallet = {}
        assets = {}
        balance = 1000
        user = User(name, wallet, assets, balance)
        save_user(user)
    else:
        print(f"Welcome back, {user.name}!")