import pandas as pd
import mysql.connector
from mysql.connector import Error
import os
import re
from dateutil import parser

# ---------------- DATABASE CONFIG ----------------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "admin@123",
    "database": "fleximart"
}

# ---------------- FILE PATHS ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

CUSTOMERS_FILE = os.path.join(DATA_DIR, "customers_raw.csv")
PRODUCTS_FILE  = os.path.join(DATA_DIR, "products_raw.csv")
SALES_FILE     = os.path.join(DATA_DIR, "sales_raw.csv")

# ---------------- HELPERS ----------------
def standardize_phone(phone):
    if pd.isna(phone):
        return None
    digits = re.sub(r"\D", "", str(phone))
    if len(digits) == 10:
        return f"+91-{digits}"
    return None

def parse_date(value):
    try:
        return parser.parse(str(value)).date()
    except:
        return None

# ---------------- MAIN ETL ----------------
def main():
    import os
    import pandas as pd
    import mysql.connector

    report = []          # ✅ define report FIRST
    conn = None          # ✅ define conn safely

    try:
        # -------------------------------
        # CONNECT TO DATABASE
        # -------------------------------
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print("Connected to MySQL database")

        # -------------------------------
        # READ FILES
        # -------------------------------
        customers_df = pd.read_csv(CUSTOMERS_FILE)
        products_df = pd.read_csv(PRODUCTS_FILE)
        sales_df = pd.read_csv(SALES_FILE)

        # -------------------------------
        # DATA QUALITY – CUSTOMERS
        # -------------------------------
        cust_read = len(customers_df)
        customers_df.drop_duplicates(subset=["email"], inplace=True)
        customers_df.dropna(subset=["email"], inplace=True)
        cust_loaded = len(customers_df)

        report.append(
            f"Customers: Read={cust_read}, Loaded={cust_loaded}"
        )

        # -------------------------------
        # DATA QUALITY – PRODUCTS
        # -------------------------------
        prod_read = len(products_df)
        products_df.drop_duplicates(subset=["product_name"], inplace=True)
        prod_loaded = len(products_df)

        report.append(
            f"Products: Read={prod_read}, Loaded={prod_loaded}"
        )

        # -------------------------------
        # DATA QUALITY – SALES
        # -------------------------------
        sales_read = len(sales_df)
        sales_loaded = len(sales_df)

        report.append(
            f"Sales: Read={sales_read}, Loaded={sales_loaded}"
        )

        conn.commit()

    except Exception as e:
        report.append(f"ETL Error: {e}")
        print("ETL Error:", e)

    finally:
        # -------------------------------
        # WRITE DATA QUALITY REPORT
        # -------------------------------
        report_path = os.path.join(
            os.path.dirname(__file__),
            "data_quality_report.txt"
        )

        with open(report_path, "w") as f:
            for line in report:
                f.write(line + "\n")

        if conn:
            conn.close()

        print("ETL pipeline finished")
