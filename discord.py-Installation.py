# Import the subprocess module to run commands in the terminal
import subprocess


# Define a function to install discord.py using pip
def install_discord_py():
    # Run the command "pip install discord.py" in the terminal and store the output and error
    output, error = subprocess.Popen(["pip", "install", "discord.py"], stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE).communicate()

    # Check if there is any error
    if error:
        # Print the error message
        print(f"An error occurred during installation: {error.decode()}")
    else:
        # Print the output message
        print(f"Installation successful: {output.decode()}")


# Define a function to test if discord.py is working
def test_discord_py():
    # Try to import discord.py and catch any exception
    try:
        import discord
        print("Discord.py is working")
    except Exception as e:
        print(f"Discord.py is not working: {e}")


# Call the functions to install and test discord.py
install_discord_py()
test_discord_py()