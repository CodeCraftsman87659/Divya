Small Dataset (data.csv):
Name, Age, Salary
Alice, 28, 50000
Bob, 35, 60000
Charlie, 40, 75000
David, 32, 55000
Eva, 27, 48000

Python Script (calculate_statistics.py):
# Import necessary libraries
import pandas as pd
def calculate_statistics(data):
"""
Calculate basic statistics (mean, median) for the given dataset.
Parameters:
- data: Pandas DataFrame containing the dataset
Returns:
- Dictionary containing calculated statistics
"""
# Calculate mean, median, and other basic statistics
mean_age = data['Age'].mean()
median_age = data['Age'].median()
mean_salary = data['Salary'].mean()
median_salary = data['Salary'].median()
# Create a dictionary to store the results
statistics = {
'Mean Age': mean_age,
'Median Age': median_age,
'Mean Salary': mean_salary,
'Median Salary': median_salary
}
return statistics
def main():
# Load the dataset from CSV
data = pd.read_csv('data.csv')
# Display the loaded dataset
print("Loaded Dataset:")
print(data)
# Calculate and display basic statistics
statistics = calculate_statistics(data)
print("\nBasic Statistics:")
for key, value in statistics.items():
print(f"{key}: {value}")
if __name__ == "__main__":
main()
