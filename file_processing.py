import pandas as pd

# Step 1: Import the CSV file
input_file = "Other_data.csv"  # Replace with your CSV file path
data = pd.read_csv(input_file)

# Step 2: Extract the specific input field(s)
# Replace 'FieldName' with the name of the column(s) you want to extract
# For multiple fields, use a list like ['Field1', 'Field2']
specific_fields = data[['REF_DATE', 'GEO', 'VALUE']]  # Use single brackets for one column

# Step 3: Save the extracted field(s) to a new CSV file
output_file = "other_output.csv"  # Specify the output file name
specific_fields.to_csv(output_file, index=False)

###.................................
