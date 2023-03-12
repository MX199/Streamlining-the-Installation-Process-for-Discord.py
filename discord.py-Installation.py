import sys
import os
packages = ["subprocess"]
for package in packages:
    result = os.system(f"{sys.executable} -m pip install --force-reinstall {package}")
    code = result >> 8
    msg = f"Package {package} installed successfully." if code == 0 else f"Failed to install package {package}."
    # print(msg)
    try:
        exec(f"import {package}")
        # print(f"Package {package} is working.")
    except Exception as e:
        # print(f"Package {package} is not working: {e}")
        exit()


# Import the subprocess module to run commands in the terminal
import subprocess
# Import the importlib.util module to check for discord.py
import importlib.util


# Define a function to install discord.py using pip
def install_discord_py():
    # Run the command "pip install discord.py" in the terminal and capture the output and error
    result = subprocess.run(["pip", "install", "discord.py"], capture_output=True)

    # Check if there is any error
    if result.stderr:
        # Print the error message using f-string
        print(f"An error occurred during installation: {result.stderr.decode()}")
    else:
        # Print the output message using f-string
        print(f"Installation successful: {result.stdout.decode()}")


# Define a function to test if discord.py is working
def test_discord_py():
    # Try to import discord.py and catch any exception
    try:
        import discord
        print("Discord.py is working")
    except Exception as e:
        print(f"Discord.py is not working: {e}")


# Define a main function to call your other functions
def main():
    # Check if discord.py is installed using importlib.util
    spec = importlib.util.find_spec("discord")
    # If spec is None, then discord.py is not installed
    if spec is None:
        install_discord_py()
    else:
        print("Discord.py is installed")

    test_discord_py()


# Call the main function if this file is executed as a script
if __name__ == "__main__":
    main()
