from datasets import load_dataset, load_metric
from beir import util


# Get dataset
datasets_ = load_dataset("squad_v2", split=['train[:20000]', 'validation[:5000]'])

# Get metric for evaluation
metric = load_metric("squad_v2")

util.download_and_unzip(url, "datasets")