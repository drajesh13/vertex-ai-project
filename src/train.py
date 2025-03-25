from transformers import BertModel
from transformers.adapters import AdapterConfig

# Load base model
model = BertModel.from_pretrained("bert-base-uncased")

# Add an adapter layer
adapter_config = AdapterConfig.load("pfeiffer")
model.add_adapter("task_adapter", config=adapter_config)
model.set_active_adapters("task_adapter")

# Save model and adapter
model.save_pretrained("adapters/task_adapter")
print("Adapter saved successfully!")

