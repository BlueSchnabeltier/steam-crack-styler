# Steam Crack Styler (SCS)
Steam Crack Styler (SCS) is a command-line interface (CLI) tool designed to enhance the visual integration of cracked Steam games into the Steam platform. Developed using Python, this tool ensures that unauthorized game modifications mimic the appearance of legitimate games within the Steam environment.

## Installation and Usage Guide
Follow these detailed steps to use the Steam Crack Styler effectively:

### Prerequisites
- Ensure that Python is installed on your system.
- The game you wish to style must already be added to your Steam library. For instructions on adding games to Steam, please refer to the official Steam support page [here](https://help.steampowered.com/en/faqs/view/4B8B-9697-2338-40EC).

### Step-by-Step Guide
1. **Initialize Game:** Launch the game through Steam to allow it to generate the necessary application identifiers.
2. **Acquire Game Data:**
   - Navigate to [SteamDB](https://steamdb.info).
   - Use the search function to locate your game and select it.
   - Right-click on the page and select "Save as…" to download the HTML page of the game's SteamDB entry.
3. **Execute the Script:**
   - Download the script from the releases tab and unzip it.
   - Run `pip install -r requirements.txt` to install dependencies.
   - Open your command-line interface.
   - Execute the script by typing `python main.py`.
   - When prompted, enter your Steam installation directory (typically `C:\Program Files (x86)\Steam\`).
   - Select your user profile from the list provided.
   - Carefully read and accept the disclaimer.
   - Choose the game for which you downloaded the HTML data.
   - Drag and drop the HTML file into the terminal, or type the file path manually.
4. **Finalize Installation:**
   - Restart the Steam client to apply the changes.
   - Confirm that the styled game appears correctly in your library.

### Completion
Upon completion of these steps, your cracked game should now visually resemble a legitimate game within your Steam library.

### How It Works

The Steam Crack Styler (SCS) utilizes Python to enhance the visual presentation of cracked Steam games, making them appear as legitimate games within the Steam interface. Here’s a brief overview of its functionality:

1. **Directory and User Profile Identification**: SCS first identifies the user's Steam directory and profiles to locate configuration files.
   
2. **Game Data Retrieval**: The script prompts for the path to an HTML file from SteamDB that includes detailed game metadata.

3. **Visual Asset Integration**: SCS parses the HTML to extract visual assets such as icons and logos and downloads these assets to the correct directories within the Steam installation path.

4. **Shortcut Customization**: It updates the game’s shortcut within Steam, using the newly downloaded assets, to reflect changes directly in the Steam client.

5. **Configuration Updates**: Finally, the script modifies Steam’s VDF files to apply the changes, requiring a restart of the Steam client to visualize the styled game in the library. 

This process ensures a seamless integration of styled games into the Steam interface, leveraging existing system configurations and user data.
