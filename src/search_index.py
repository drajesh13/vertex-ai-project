from google.cloud import aiplatform

# Initialize
aiplatform.init(project="your-project-id", location="us-central1")

# Create a search index
index = aiplatform.MatchingEngineIndex.create_tree_ah_index(
    display_name="document_search_index",
    contents_delta_uri="gs://your-bucket/documents/",
    dimensions=768
)

print(f"Index created: {index.resource_name}")

# Query the index
query = "What is in document 1?"
results = index.find_neighbors(embedding=[0.1, 0.2, ...], num_neighbors=5)

for result in results:
    print(f"Found document ID: {result.id} with score: {result.distance}")
