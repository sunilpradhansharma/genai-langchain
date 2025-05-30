from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Documents and query
documents = [
    "Amazon S3 is a scalable object storage service that lets you store and retrieve any amount of data from anywhere on the web.",
    "AWS Lambda allows you to run code without provisioning or managing servers, making it ideal for building serverless applications.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Amazon EC2 provides resizable compute capacity in the cloud, enabling you to launch virtual machines for various workloads.",
    "Amazon SageMaker is a fully managed service that helps developers and data scientists build, train, and deploy machine learning models quickly."
]
query = "tell me about SageMaker"

# Generate embeddings
doc_embeddings = model.encode(documents)
query_embedding = model.encode([query])

# Combine for PCA
all_embeddings = doc_embeddings.tolist() + query_embedding.tolist()

# Reduce dimensions for plotting (PCA or t-SNE can be used)
pca = PCA(n_components=2)
reduced_embeddings = pca.fit_transform(all_embeddings)

# Split back
doc_points = reduced_embeddings[:-1]
query_point = reduced_embeddings[-1]

# Plot
plt.figure(figsize=(10, 6))
for i, point in enumerate(doc_points):
    plt.scatter(point[0], point[1], label=f'Doc {i+1}')
    plt.text(point[0]+0.01, point[1]+0.01, f'Doc {i+1}', fontsize=9)

# Plot the query
plt.scatter(query_point[0], query_point[1], c='red', label='Query', marker='X', s=100)
plt.text(query_point[0]+0.01, query_point[1]+0.01, 'Query', fontsize=10, fontweight='bold', color='red')

plt.title("2D Visualization of Document and Query Embeddings")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()