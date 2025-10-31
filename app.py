from flask import Flask, render_template, request, jsonify
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io, base64, json, os

app = Flask(__name__)

# -----------------------------
# Load Datasets
# -----------------------------
crop_path = "Dataset/crop_production.json"
rain_path = "Dataset/rainfall.csv"

# --- Load crop data (JSON) ---
with open(crop_path, "r", encoding="utf-8") as f:
    data = json.load(f)
crop_data = pd.DataFrame(data["Table"])

# --- Load rainfall data (CSV) ---
rainfall = pd.read_csv(rain_path)

print("✅ Crop and Rainfall datasets loaded successfully!")
print("Rainfall Columns:", rainfall.columns.tolist())
print("Crop Columns:", crop_data.columns.tolist())

# -----------------------------
# Graph generator function
# -----------------------------
def generate_graph(df, x_col, y_col, title):
    plt.figure(figsize=(6, 3))
    plt.plot(df[x_col], df[y_col], marker='o', color='blue', linewidth=2)
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return encoded


# -----------------------------
# Flask Routes
# -----------------------------
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get("query", "").lower()
    response_text = "Sorry, I couldn’t understand your question."
    graph = None

    # --- Rainfall Trend Query ---
    if "rainfall" in user_query:
        for state in rainfall["SUBDIVISION"].unique():
            if state.lower() in user_query:
                state_data = rainfall[rainfall["SUBDIVISION"].str.lower() == state.lower()]
                yearly_avg = state_data.groupby("YEAR")["ANNUAL"].mean().reset_index()
                response_text = f"Average annual rainfall trend for {state}:"
                graph = generate_graph(yearly_avg, "YEAR", "ANNUAL", f"Rainfall Trend - {state}")
                break

    # --- Crop Production / Output Trend Query ---
    elif "production" in user_query or "crop" in user_query or "output" in user_query:
        for state in crop_data["StateName"].unique():
            if state.lower() in user_query:
                filtered = crop_data[crop_data["StateName"].str.lower() == state.lower()]
                yearly_sum = filtered.groupby("FinYearId")["TOTAL"].sum().reset_index()
                response_text = f"Total agricultural output trend for {state}:"
                graph = generate_graph(yearly_sum, "FinYearId", "TOTAL", f"Agricultural Output Trend - {state}")
                break

    return jsonify({"answer": response_text, "graph": graph})


# -----------------------------
# Run Flask App
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
