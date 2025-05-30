import joblib
import time

# Load model and encoder
model = joblib.load("jaundice_rf_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Simulate ADC voltage input (replace this with real reading later)
def read_voltage():
    # Example: Replace with actual voltage reading logic
    return float(input("Enter simulated voltage (0.0 to 3.3V): "))

while True:
    try:
        voltage = read_voltage()
        prediction = model.predict([[voltage]])[0]
        label = label_encoder.inverse_transform([prediction])[0]
        print(f"Voltage: {voltage:.2f} V → Prediction: {label}")
        time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting...")
        break
