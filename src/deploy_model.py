from google.cloud import aiplatform

# Initialize
aiplatform.init(project="your-project-id", location="us-central1")

# Get model from registry
model = aiplatform.Model.list(filter="display_name=adapter_model")[-1]

# Deploy model
endpoint = model.deploy(
    machine_type="n1-standard-4",
    min_replica_count=1,
    max_replica_count=3
)

print(f"Model deployed at endpoint: {endpoint.resource_name}")
