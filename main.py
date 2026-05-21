import pandas as pd

input_file = "input.xlsx"
output_file = "cleaned_output.xlsx"

df = pd.read_excel(input_file)

# Remove completely empty rows
df = df.dropna(how="all")

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned file
df.to_excel(output_file, index=False)

print(f"Cleaned file saved as {output_file}")