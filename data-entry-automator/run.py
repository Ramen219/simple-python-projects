import pandas as pd  # Import the pandas library, which is used for data manipulation and analysis

def automate_data(data, file_path):
    try:
        try:
            # Try to read the existing data from the CSV file
            exist_data = pd.read_csv(file_path)
        except FileNotFoundError:
            # If the file does not exist, create an empty DataFrame
            exist_data = pd.DataFrame()

        # Convert the new data (a list of dictionaries) into a DataFrame
        new_data = pd.DataFrame(data)
        
        # Concatenate the existing data and the new data into a single DataFrame
        combined_data = pd.concat([exist_data, new_data], ignore_index=True) #ignore_index=True: index is reset,begn  numbered sequentially starting from 0
        
        # Save the combined data back to the CSV file, without the index
        combined_data.to_csv(file_path, index=False)
        
        # Print a success message
        print(f"Data entry successful")
        
    except Exception as e:
        # If any exception occurs, print an error message with the exception details
        print(f"An error occurred: {e}")

# Sample data to be entered into the CSV file
data_to_enter = [
    {"name": "John Doe", "age": 30, 'city': 'New York'},
    {"name": "Jane Doe", "age": 25, 'city': 'London'},
    {"name": "Mary Doe", "age": 35, 'city': 'Paris'}
]

# Path to the CSV file where data will be stored
csv_file_path = "data.csv"

# Call the function to automate data entry
automate_data(data_to_enter, csv_file_path)
