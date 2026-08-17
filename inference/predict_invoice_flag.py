import joblib
import pandas as pd

MODEL_PATH = "models/predict_flag_invoice.pkl"

def load_model(model_path: str = MODEL_PATH):
    """
    Load trained classifier model.
    """
    with open(model_path, "rb") as f:
        model  = joblib.load(f)
    return model

def predict_invoice_model(input_data):
    """
    Predict invoice flag  for new vendor invoices.
    
    Parameters
    ----------
    input_data : dict
    
    Returns
    -------
    pd.DataFrame with predicted flag
    """
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df['Predicted_Flag'] = model.predict(input_df).round()
    return input_df

if __name__ == "__main__":

    # Example inference run (local testing)
    sample_data = {
        "invoice_quantity": [50, 120, 10, 300],
        "invoice_dollars": [18500, 9000, 3000, 200],
        "Freight": [450, 120, 80, 30],
        "total_item_quantity": [50, 118, 10, 300],
        "total_item_dollars": [18500, 8990, 3050, 195],
    }
    prediction = predict_invoice_model(sample_data)
    print(prediction)

    