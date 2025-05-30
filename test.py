import pandas as pd


df = pd.read_csv("jaundice_voltage_with_display.csv")  # Replace with your actual filename

# Drop the 1st (Timestamp) and 4th (Display) columns
df_cleaned = df.drop(columns=[df.columns[0], df.columns[3]])

def classify_jaundice(adc_value):
    if adc_value > 800:
        return "Severe Jaundice"
    elif adc_value > 600:
        return "Moderate Jaundice"
    elif adc_value > 400:
        return "Mild Jaundice"
    else:
        return "Normal"

# Apply classification
df_cleaned['Jaundice Level'] = df_cleaned['ADC Value'].apply(classify_jaundice)

# Save to new CSV
df_cleaned.to_csv("classified_jaundice_voltage.csv", index=False)

print("File saved as classified_jaundice_voltage.csv")
