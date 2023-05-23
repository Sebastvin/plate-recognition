import labelbox
import json
import secret
import os


# Enter your Labelbox API key here
LB_API_KEY = secret.api_key
# Create Labelbox client
lb = labelbox.Client(api_key=LB_API_KEY)
# Get project by ID
project = lb.get_project('clh13dzrw0l4a07zmf36u97rd')
# Export labels created in the selected date range as a json file:
labels = project.export_labels(download=True, start="2023-04-02", end="2023-05-02")

labels_json = json.dumps(labels)

# Save to a file
with open(os.path.join('datasets', 'labels.json'), 'w') as out:
    out.write(labels_json)
