# RAG solves problem
The problem is that Gemini doesn't automatically know your private company document.
You could put the entire document into the prompt:

But that becomes problematic when documents are:

very large
numerous
frequently updated
private
too large for the context window
expensive to repeatedly send

RAG solves this by retrieving only the relevant information.

# What does RAG stand for?
Retrieval

Find relevant information.

Augmented

Add that information to the model's context.

Generation

Ask the LLM to generate the answer using that context.
# RAG is NOT the same as fine-tuning
"RAG retrieves relevant external knowledge at inference time and provides it to the LLM as context, whereas fine-tuning changes the model's parameters through additional training."
# Fine-tuning
You modify the model's learned parameters by training it on additional data.

Base Model
   +
Training Data
   ↓
Fine-tuned Model
# RAG
Documents
   ↓
Retrieve relevant information
   ↓
Put information into prompt
   ↓
Existing LLM
# "Why don't you just put the entire document into the LLM context instead of using RAG?"
"For small documents, we could provide the entire document as context, but that becomes inefficient as the knowledge base grows. RAG allows us to retrieve only the relevant chunks, reducing context size, latency, and potentially cost while improving the relevance of the information provided to the model. It also allows the knowledge base to be updated independently of the model."
# Why not send the entire document every time?
Token usage — You send the same large document repeatedly with every question.
Cost — More input tokens generally means higher API cost.
Latency — Processing a huge context can take longer.
Context-window limits — Eventually the document/knowledge base can exceed what the model can accept.
Irrelevant information — The model receives lots of information unrelated to the current question.
# Why do we need embeddings?
Because we want semantic search, not just exact keyword matching.
# What does Qdrant store?
Point
├── ID
├── Vector
└── Payload 
{
  "id": "chunk-001",

  "vector": [
    0.12,
    -0.43,
    0.81,
    0.27
  ],

  "payload": {
    "text": "React uses a Virtual DOM to efficiently update the UI.",
    "document_id": "react-guide-001",
    "file_name": "react-guide.pdf",
    "page": 2,
    "chunk_index": 1
  }
}
# What happens after retrieval?
This is the Augmented part, We take the retrieved text and construct a prompt.