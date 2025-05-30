import gradio as gr
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import load_prompt

# Load environment variables
load_dotenv()

# Load model and prompt
model = ChatOpenAI()
template = load_prompt('template.json')

# Inference function
def generate_summary(paper_input, style_input, length_input):
    chain = template | model
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    return result.content

# Gradio UI components
paper_names = [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis"
]

styles = ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
lengths = ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]

# Launch Gradio interface
interface = gr.Interface(
    fn=generate_summary,
    inputs=[
        gr.Dropdown(paper_names, label="Select Research Paper Name"),
        gr.Dropdown(styles, label="Select Explanation Style"),
        gr.Dropdown(lengths, label="Select Explanation Length")
    ],
    outputs=gr.Textbox(label="Summary"),
    title="Research Assistant",
    description="Get summaries of famous AI papers in your preferred style and length."
)

interface.launch()