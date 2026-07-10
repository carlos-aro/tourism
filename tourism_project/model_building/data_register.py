from huggingface_hub.utils import RepositoryNotFoundError, HfHubHTTPError
from huggingface_hub import HfApi, create_repo
import os

# complete the code to set your Hugging Face repo_id in the format "<your-HF-user-id>/tourism"
repo_id = "carlosaro/tourism"
repo_type = "dataset"

# Initialize the Hugging Face API client using the HF_TOKEN environment variable
api = HfApi(token=os.getenv("HF_TOKEN"))

# Step 1: Check if the repository already exists; if not, create it
try:
    api.repo_info(repo_id=repo_id, repo_type=repo_type)
    print(f"Space '{repo_id}' already exists. Using it.")
except RepositoryNotFoundError:
    print(f"Space '{repo_id}' not found. Creating new space...")
    # complete the code to create a new public repository on Hugging Face
    create_repo(repo_id=repo_id, repo_type=repo_type, private=False)
    print(f"Space '{repo_id}' created.")

# Upload the local data folder to the Hugging Face dataset repository
api.upload_folder(
    folder_path="tourism_project/data",
    repo_id=repo_id,
    repo_type=repo_type,
)
