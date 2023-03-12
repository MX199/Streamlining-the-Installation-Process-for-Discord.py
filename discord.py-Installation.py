import sys
import os
packages = ["subprocess"]
for package in packages:
    result = os.system(f"{sys.executable} -m pip install --force-reinstall {package}")
    code = result >> 8
    msg = f"Package {package} installed successfully." if code == 0 else f"Failed to install package {package}."
    try:
        exec(f"import {package}")
    except Exception as e:
        exit()


import subprocess
import importlib.util


# Define a function to install discord.py using pip
def install_discord_py():
    result = subprocess.run(["pip", "install", "discord.py"], capture_output=True)
    # Check if there is any error
    if result.stderr:
        print(f"An error occurred during installation: {result.stderr.decode()}")
    else:
        print(f"Installation successful: {result.stdout.decode()}")


# Define a function to test if discord.py is working
def test_discord_py():
    try:
        import discord
        print("Discord.py is working")
    except Exception as e:
        print(f"Discord.py is not working: {e}")


# Define a main function to call your other functions
def main():
    # Check if discord.py is installed using importlib.util
    spec = importlib.util.find_spec("discord")
    if spec is None:
        install_discord_py()
    else:
        print("Discord.py is installed")

    test_discord_py()


# Call the main function if this file is executed as a script
if __name__ == "__main__":
    main()
