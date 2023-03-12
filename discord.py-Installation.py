# Import pip as a library to install packages
import pip
# Import discord.py if installed, otherwise install it and test it
try:
    import discord
except ImportError:
    print("Discord.py is not installed")
    # Install discord.py using pip as a library
    result = pip.main(["install", "discord.py"])
    # Check if the installation was successful
    print(f"Installation {'successful' if result == 0 else 'failed'}")
else:
    print("Discord.py is installed")

# Test if discord.py is working by printing a message
def test_discord_py():
    """
    Test if discord.py is working by printing a message
    """
    print("Discord.py is working")
# Test discord.py regardless of the outcome of importing it
test_discord_py()
