# Call Hugging Face API with open source supported model
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()

# Initialize the endpoint with a supported model
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=100
)

# Wrap it with the Chat interface
model = ChatHuggingFace(llm=llm)

# Properly formatted message
result = model.invoke([HumanMessage(content="What is the capital of France?")])
print(result.content)