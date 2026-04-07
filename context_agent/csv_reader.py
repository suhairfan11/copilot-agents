import pandas as pd

def csv_reader(file_path):
    """
    Reads a CSV file containing A/B test data.
    Columns expected: date, device, volume, ab_test, segment, page
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    return df

# Example usage
if __name__ == '__main__':
    file_path = 'path_to_your_file.csv'  # Update this with the actual path
    data = csv_reader(file_path)
    print(data.head())