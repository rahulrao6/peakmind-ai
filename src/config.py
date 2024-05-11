import os

# OpenAI API Key
OPENAI_API_KEY = os.getenv('sk-proj-w4kqAir6ftemr7ZN5X4XT3BlbkFJgpPUcdlWLMeXHKf73X4q')

# Couchbase Connection Configurations
COUCHBASE_ENDPOINT = os.getenv('COUCHBASE_ENDPOINT', 'couchbases://cb.bk2qgpca1d6budjk.cloud.couchbase.com')
COUCHBASE_USERNAME = os.getenv('COUCHBASE_USERNAME', '<<rahul.rao2908@gmail.com>>')  # Replace placeholder with actual username or environment variable
COUCHBASE_PASSWORD = os.getenv('COUCHBASE_PASSWORD', '<<Te@md12345!>>')  # Replace placeholder with actual password or environment variable
COUCHBASE_BUCKET = os.getenv('COUCHBASE_BUCKET', '<<travel-sample>>')  # Replace placeholder with actual bucket name or environment variable
COUCHBASE_SCOPE = os.getenv('COUCHBASE_SCOPE', '<<inventory>>')  # Replace placeholder with actual scope name or environment variable
COUCHBASE_COLLECTION = os.getenv('COUCHBASE_COLLECTION', '<<airplane>>')  # Replace placeholder with actual collection name or environment variable

# You can set default values directly or leave them to be defined in environment variables

# Model and data settings
MODEL_NAME = os.getenv('MODEL_NAME', 'gpt-4')
SENTIMENT_MODEL = os.getenv('SENTIMENT_MODEL', 'distilbert-base-uncased')
DATA_PATH = os.getenv('DATA_PATH', 'data/Compilation_T1_Master_Preprocessed.csv')
