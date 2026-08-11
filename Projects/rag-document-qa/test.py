import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("QDRANT_API_KEY")

client = QdrantClient(
    url=qdrant_url,
    api_key=qdrant_api_key,
)

try:
    collections = client.get_collections()

    print("✅ Qdrant connected successfully!")
    print("Collections:")

    for collection in collections.collections:
        print("-", collection.name)

except Exception as e:
    print("❌ Qdrant connection failed!")
    print(type(e).__name__, ":", e)