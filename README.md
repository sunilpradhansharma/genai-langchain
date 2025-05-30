
# 🦜 LangChain Overview

LangChain is an open-source framework that helps build applications powered by **Large Language Models (LLMs)**. It provides modular components and end-to-end tools to create powerful AI solutions like:

- Chatbots
- Question-answering systems
- Retrieval-Augmented Generation (RAG)
- Autonomous agents
- And more!

---

## 🚀 Why LangChain?

- ✅ Supports all major LLMs
- ✅ Simplifies building LLM-powered applications
- ✅ Seamless integration with popular tools
- ✅ Open source and actively maintained
- ✅ Suits a wide range of GenAI use cases

- ![LangChain](docs/LangChain.png)
---

## 🔍 Search Capabilities

1. **Normal Keyword Search**  
2. **Semantic Search** (understand query & retrieve contextually)

### 🧠 LangChain “Brain” Features:
- Natural Language Understanding (NLU)
- Context-Aware Text Generation

---

## ⚠️ Challenges Before LangChain

- Where to host LLMs?
- How to manage doc uploaders, text splitters, embeddings, retrieval?
- Can you build and maintain these from scratch?
- How to switch models without rewriting everything?

- ![Chatbot Diagram](docs/EBook_Chatbot_Diagram.png)
---

## ✅ Benefits of LangChain

- ![LangChain example](docs/PDF_to_Brain_Workflow.png)
- 
- Concept of **Chains** to build logic
- **Model Agnostic** development
- Robust **Ecosystem**
- **Memory and State** handling (e.g., for past conversations)

---

## 🔄 Alternatives

- [LlamaIndex](https://www.llamaindex.ai/)
- [Haystack](https://haystack.deepset.ai/)

---

## 🧩 Core LangChain Components

- ![LangChain Components](docs/LangChain_Components_Diagram.png)

Types of Memory:
| Component                      | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `ConversationBufferMemory`    | Stores full transcript (can get large)                                      |
| `ConversationBufferWindowMemory` | Keeps last N interactions to reduce memory                                 |
| `Summarizer-Based Memory`     | Summarizes chat history for memory-efficient context                        |
| `Custom Memory`               | Tailored memory for user preferences, facts, etc.                           |

> 📚 [Docs: LangChain Introduction](https://python.langchain.com/docs/introduction/)

---

## 🧠 What are Models?

LangChain abstracts complexity from interacting with:

- Language Models (LLMs & Chat Models)
- Embedding Models (for semantic search)

These models can be **local** or **API-based**, and LangChain provides a **unified interface** for both.

- ![Model Types Diagram](docs/Model_Types_Diagram.png)
---

## 🆚 LLMs vs Chat Models

| Feature            | LLMs (Base Models)                 | Chat Models (Instruction-Tuned)            |
|--------------------|------------------------------------|--------------------------------------------|
| Purpose            | Free-form text generation          | Multi-turn conversations                   |
| Training Data      | Books, articles                    | Dialogue, user-assistant chats             |
| Memory & Context   | None                               | Maintains structured conversation history  |
| Role Awareness     | No                                 | Understands `user`, `assistant`, `system`  |
| Example Models     | GPT-3, LLaMA-2-7B, Mistral-7B       | GPT-4, GPT-3.5-turbo, Claude, Mistral-Instruct |
| Use Cases          | Text gen, summarization, code      | Chatbots, support, tutoring                 |

---

## 🔓 Open Source Model Comparison

| Model             | Developer     | Parameters | Best Use Case                          |
|------------------|---------------|------------|----------------------------------------|
| LLaMA-2-7B/13B/70B | Meta AI      | 7B–70B     | General text generation                |
| Mixtral-8x7B     | Mistral AI     | 8x7B MoE   | Fast, efficient responses              |
| Mistral-7B       | Mistral AI     | 7B         | Best small-scale model                 |
| Falcon-7B/40B    | TII UAE        | 7B–40B     | High-speed inference                   |
| BLOOM-176B       | BigScience     | 176B       | Multilingual generation                |
| GPT-J-6B         | EleutherAI     | 6B         | Lightweight and efficient              |
| GPT-NeoX-20B     | EleutherAI     | 20B        | Large-scale applications               |
| StableLM         | Stability AI   | 3B–7B      | Compact chatbot models                 |

---

## ✍️ Prompts

Prompts are input instructions or queries given to a model to guide its output
1. Text based Prompts
2. MultiModal Prompts (image, sounds, videos)

- ![Research Assistant](docs/Research_Assistant_UI.png)

- **Static Prompts**: Hardcoded questions  
- **Dynamic Prompts**: Template-based and flexible



```python
# Static Prompt
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("What is the capital of France?")

# Dynamic Prompt
prompt = PromptTemplate.from_template("What is the capital of {country}?")
filled_prompt = prompt.format(country="India")
```

### Prompt Template

A PromptTemplate in LangChain is a structured way to create prompts dynamically by inserting variables into a predefined template. Instead of hardcoding prompts, PromptTemplate allows you to define placeholders that can be filled in at runtime with different inputs.
This makes it reusable, flexible, and easy to manage, especially when working with dynamic user inputs or automated workflows.

- ![Static vs Dynamic Messages](docs/Invoke_Static_vs_Dynamic_Messages.png)
- 
### Prompt Template Use Case

```text
Please summarize the research paper titled ”{paper_input}” with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}

If mathematical equations are present, explain using simple code or analogies.
Respond “Insufficient information available” if not found.
```

---

## 🖼️ Image Placeholders

> 📌 Replace these with actual image files or relative paths.





---

## 📚 Resources

- 🌐 [LangChain Official Docs](https://python.langchain.com/docs/introduction/)
- 📦 [LangChain GitHub](https://github.com/langchain-ai/langchain)

---

## 🙌 Contributing

Contributions welcome! Feel free to open issues or pull requests.

---

## 📝 License

LangChain is licensed under the MIT License.