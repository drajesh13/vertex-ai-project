from google.cloud import aiplatform

PROJECT_ID = "your-project-id"
BUCKET_URI = "gs://your-bucket"
MODEL_PATH = "adapters/task_adapter"

# Initialize Vertex AI
aiplatform.init(project=PROJECT_ID, location="us-central1")

# Upload model
model = aiplatform.Model.upload(
    display_name="adapter_model",
    artifact_uri=f"{BUCKET_URI}/{MODEL_PATH}",
    serving_container_image_uri="gcr.io/cloud-aiplatform/prediction/tf2-cpu.2-4:latest"
)
print(f"Model uploaded successfully: {model.resource_name}")
