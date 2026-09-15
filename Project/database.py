import os
import sys

import pandas as pd
from sqlalchemy import create_engine, text

DB_USER = "root"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "campus_db"

SERVER_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"
DATABASE_URL = f"{SERVER_DATABASE_URL}/{DB_NAME}"


def ensure_database() -> None:
    default_engine = create_engine(SERVER_DATABASE_URL)
    try:
        with default_engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`"))
    finally:
        default_engine.dispose()


def init_db(csv_path: str) -> None:
    if not csv_path or not os.path.exists(csv_path):
        raise FileNotFoundError(f"Source file '{csv_path}' was not found")

    ensure_database()
    engine = create_engine(DATABASE_URL)
    try:
        df = pd.read_csv(csv_path)

        if "Open_source_Contribution" in df.columns:
            median = df["Open_source_Contribution"].median()
            df["Open_source_Contribution"] = df["Open_source_Contribution"].fillna(median)

        df.to_sql("student", con=engine, if_exists="replace", index=False)

        if "college_Tier" in df.columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE student ADD INDEX idx_tier (college_Tier(50))"))

    finally:
        engine.dispose()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 Project/database.py <csv_path>")
    init_db(sys.argv[1])

