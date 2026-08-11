# "Explain your RAG retrieval pipeline."
"First, we extract the document text and split it into chunks. Each chunk is converted into an embedding using our embedding model and stored in Qdrant along with an ID and metadata such as the source document, page, and chunk text. When a user asks a question, we generate an embedding for the query using the same embedding model. Qdrant compares that query vector against the stored vectors using the configured distance metric, ranks the results, and returns the top-K relevant points along with their scores and payloads. We take the relevant text from those payloads, construct a prompt containing the retrieved context and the user's question, and send that to the generative LLM to produce the final answer."

# Why QDrant
Qdrant provides:

vector storage
similarity/distance search
indexing
metadata/payload
filtering
persistence
scalable retrieval capabilities

# What does sparse search actually capture?
It is particularly useful for exact or keyword-heavy queries such as:
"React.memo"
"ERR_CONNECTION_REFUSED"
"ABC-12345"
"JWT"
"gemini-embedding-2-preview"

# Where does BM25 come in?
One common sparse retrieval method is BM25.
BM25 considers things such as:
TF  → Term Frequency
IDF → Inverse Document Frequency
Document length
So if a rare term appears in a document, it can contribute more strongly to the relevance score.

That's why you enabled:

Use IDF → ✅

in your Qdrant collection.
# "Why did you use hybrid search instead of only embeddings?"
"Dense embeddings are excellent for semantic similarity, but they can miss exact lexical signals such as product names, identifiers, error codes, or specific technical terms. Hybrid retrieval combines dense semantic search with sparse lexical retrieval such as BM25, giving us better recall across both semantic and exact-match queries."
