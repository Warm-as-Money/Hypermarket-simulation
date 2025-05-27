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

def type_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_animation():
    clear()
    print("\n" * 3)
    type_print("🛒 WELCOME TO THE", 0.1)
    time.sleep(0.3)
    type_print("💰 HYPERMARKET SIMULATOR 💰", 0.08)
    time.sleep(0.5)

    loading_text = "Loading"
    for x in range(3):
        sys.stdout.write(loading_text + "." * (x + 1) + " \r")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")

    type_print("Get ready to build your empire......\n", 0.07)
    time.sleep(0.5)
    type_print("🚀 Launching simulation......", 0.07)
    time.sleep(1)
    clear()

if __name__ == "__main__":
    name = input("Enter your username: ")
    user = load_user(name)
    if user is None:
        welcome_animation()
        wallet = {}
        assets = {}
        balance = 1000
        user = User(name, wallet, assets, balance)
        save_user(user)
    else:
        print(f"Welcome back, {user.name}!")