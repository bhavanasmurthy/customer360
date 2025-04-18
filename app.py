from flask import Flask, jsonify
import pyodbc
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/customers")
def get_customers():
    conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=yourserver.database.windows.net;DATABASE=yourdb;UID=youruser;PWD=yourpwd")
    df = pd.read_sql("SELECT TOP 1000 * FROM CustomerData", conn)
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)