import json
import inspect
from pathlib import Path
import pandas as pd
import numpy as np

def save_df_to_csv(df, label=''):
    # Define the directory and filename
    outer_func_name = inspect.stack()[1].function
    directory = Path("user_data/vis")  # Target directory
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

def default_converter(obj):
    """Custom converter for objects not serializable by default json.dump."""
    if isinstance(obj, pd.DataFrame):
        return obj.to_dict(orient='records')  # or obj.to_json(orient='records') for JSON string
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

def save_dict_to_json(d, label=''):
    try:
        directory = Path("user_data/vis")
        outer_func_name = inspect.stack()[1].function
        json_filename = directory / f"{outer_func_name}{label}.json"

        directory.mkdir(parents=True, exist_ok=True)

        if not json_filename.exists():
            with open(json_filename, 'w') as json_file:
                json.dump(d, json_file, default=default_converter, indent=4)
            print(f"Dictionary saved as {json_filename}")
        # else:
        #     print(f"File {json_filename} already exists. No action taken.")
    except Exception as e:
        print(f"An error occurred: {e}")

def save_array_to_csv(array, label=''):
    # Define the directory and filename
    outer_func_name = inspect.stack()[1].function
    directory = Path("user_data/vis")  # Target directory
    csv_filename = directory / f"{outer_func_name}{label}.csv"

    # Check if the file already exists
    if not csv_filename.exists():
        # Ensure the directory exists; if not, create it
        directory.mkdir(parents=True, exist_ok=True)

        # Save the NumPy array to a CSV file
        np.savetxt(csv_filename, array, delimiter=',')
        print(f"Array saved as {csv_filename}")
    else:
        print(f"File {csv_filename} already exists. No action taken.")
