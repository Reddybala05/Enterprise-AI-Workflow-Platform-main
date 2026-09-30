from datetime import datetime

from airflow import DAG
from airflow.decorators import task


DAG_ID = "ml_training_pipeline"


with DAG(
    dag_id=DAG_ID,
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["ml", "machine-learning", "training"],
    description="Daily machine learning data processing and model training pipeline.",
) as dag:

    @task
    def extract_data() -> dict:
        """Extract source data for the ML pipeline."""

        print("Starting data extraction...")

        data = {
            "records": 1000,
            "source": "sample_dataset",
        }

        print(
            f"Data extraction completed: "
            f"{data['records']} records"
        )

        return data

    @task
    def process_data(data: dict) -> dict:
        """Validate and process the extracted data."""

        print(
            f"Processing data from source: "
            f"{data['source']}"
        )

        processed_data = {
            "records": data["records"],
            "source": data["source"],
            "processed": True,
        }

        print(
            f"Data processing completed: "
            f"{processed_data['records']} records"
        )

        return processed_data

    @task
    def train_model(processed_data: dict) -> str:
        """Train the ML model using processed data."""

        print(
            f"Training model using "
            f"{processed_data['records']} records..."
        )

        # Placeholder for actual model-training logic.
        model_version = "model_v1"

        print(
            f"Model training completed: "
            f"{model_version}"
        )

        return model_version

    # ------------------------------------------------------------------
    # Pipeline Dependency
    # ------------------------------------------------------------------

    extracted_data = extract_data()

    processed_data = process_data(
        extracted_data
    )

    trained_model = train_model(
        processed_data
    )
