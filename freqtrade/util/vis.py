import json
import inspect
from pathlib import Path

def save_df_to_csv(df, label=''):
    # Define the directory and filename
    outer_func_name = inspect.stack()[1].function
    directory = Path("vis")  # Target directory
    csv_filename = directory / f"{outer_func_name}{label}.csv"

    # Check if the file already exists
    if not csv_filename.exists():
        # Ensure the directory exists; if not, create it
        directory.mkdir(parents=True, exist_ok=True)

        # Save the DataFrame to a CSV file
        df.to_csv(csv_filename, index=False)
        print(f"DataFrame saved as {csv_filename}")
    # else:
    #     print(f"File {csv_filename} already exists. No action taken.")

def save_dict_to_json(d, label=''):
    # Define the directory and filename
    outer_func_name = inspect.stack()[1].function
    directory = Path("vis")  # Target directory
    json_filename = directory / f"{outer_func_name}{label}.json"

    # Check if the file already exists
    if not json_filename.exists():
        # Ensure the directory exists; if not, create it
        directory.mkdir(parents=True, exist_ok=True)

        # Save the dictionary to a JSON file
        with open(json_filename, 'w') as json_file:
            json.dump(d, json_file, indent=4)
        print(f"Dictionary saved as {json_filename}")
    # else:
    #     print(f"File {json_filename} already exists. No action taken.")
