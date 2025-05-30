import gradio as gr
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def embed_text(text):
    embedding = model.encode([text])[0]
    return str(embedding)

iface = gr.Interface(
    fn=embed_text,
    inputs=gr.Textbox(label="Enter text"),
    outputs=gr.Textbox(label="Embedding"),
    title="Text Embedding Generator"
)

if __name__ == "__main__":
    iface.launch()