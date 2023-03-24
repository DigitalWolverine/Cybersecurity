# Import the required libraries
import pickle
from tabulate import tabulate


# Function to add a new asset to the list of assets
def add_asset(assets):
    # Prompt the user to enter asset information and create a dictionary for the new asset
    asset = {
        'Asset ID': input('Asset ID: '),
        'Asset Type': input('Asset Type (hardware, software, data, network device): '),
        'Asset Name': input('Asset Name: '),
        'Description': input('Description: '),
        'Owner': input('Owner: '),
        'Location': input('Location: '),
        'Classification': input('Classification (public, internal, confidential, restricted): '),
        'Criticality': input('Criticality (low, medium, high): '),
        'Software Version': input('Software Version (N/A if not applicable): '),
        'Patch Level': input('Patch Level (N/A if not applicable): '),
        'Date Acquired': input('Date Acquired (YYYY-MM-DD): '),
        'End-of-Life Date': input('End-of-Life Date (YYYY-MM-DD or N/A): '),
    }
    assets.append(asset)  # Add the asset to the list of assets


# Function to display the assets in a tabular format
def view_assets(assets):
    if not assets:  # If there are no assets, print a message and return
        print("No assets found.")
        return

    # Create headers for the table using the keys of the first asset
    headers = list(assets[0].keys())
    # Prepare table data by extracting the values of each asset
    table_data = [list(asset.values()) for asset in assets]
    # Print the table using the "tabulate" library
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


# Function to save the assets to a file using pickle
def save_assets(assets, filename):
    with open(filename, 'wb') as f:  # Open the file in binary write mode
        pickle.dump(assets, f)  # Save the assets to the file


# Function to load the assets from a file using pickle
def load_assets(filename):
    with open(filename, 'rb') as f:  # Open the file in binary read mode
        return pickle.load(f)  # Load and return the assets from the file


# Function to modify an existing asset in the list of assets
def modify_asset(assets):
    # Prompt the user to enter the Asset ID to modify
    asset_id = input('Enter the Asset ID of the asset you want to modify: ')
    asset = None  # Initialize an empty asset variable
    # Iterate through the assets to find the one with the matching Asset ID
    for a in assets:
        if a['Asset ID'] == asset_id:
            asset = a
            break

    # If the asset is found, prompt the user to enter new values
    if asset is not None:
        print('Enter new values (leave blank to keep the current value):')
        for key, value in asset.items():
            new_value = input(f'{key} (current: {value}): ')
            # Update the asset's value if a new value is provided
            if new_value != '':
                asset[key] = new_value
    else:
        # Print a message if the asset with the specified ID is not found
        print(f'Asset with ID {asset_id} not found.')


# Main function to run the program
def main():
    assets = []  # Initialize an empty list to store assets
    filename = 'assets.pickle'  # Define the filename for saving/loading assets

    # Attempt to load assets from the file
    try:
        assets = load_assets(filename)
    except FileNotFoundError:  # If the file is not found, ignore the error and continue
        pass

    # Run the main loop of the program
    while True:
        # Display the menu options to the user
        print('1. Add asset')
        print('2. View assets')
        print('3. Save assets')
        print('4. Load assets')
        print('5. Modify asset')
        print('6. Exit')
        # Get the user's choice
        choice = int(input('Enter your choice: '))

        # Execute the appropriate function based on the user's choice
        if choice == 1:
            add_asset(assets)
        elif choice == 2:
            view_assets(assets)
        elif choice == 3:
            save_assets(assets, filename)
        elif choice == 4:
            assets = load_assets(filename)
        elif choice == 5:
            modify_asset(assets)
        elif choice == 6:
            break  # Exit the loop and end the program
        else:
            # If the user enters an invalid choice, display an error message
            print('Invalid choice. Please try again.')


# Check if the script is being run directly and not being imported as a module
if __name__ == '__main__':
    main()  # If so, run the main function
