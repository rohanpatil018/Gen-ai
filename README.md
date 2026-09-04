# Generative AI Learning Repository

A hands-on **Generative AI learning and implementation repository**
covering the core concepts and practical components of modern GenAI
applications using **LangChain** and related tools.

This repository is structured around the concepts taught in the
**CampusX Generative AI / LangChain YouTube playlist**, with
implementations and experiments organized topic-wise.

## 📚 Learning Reference

The primary learning reference for this repository is the CampusX
Generative AI playlist:

**CampusX -- Generative AI using LangChain**\
https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0

The playlist covers LangChain fundamentals, models, prompts, structured
output, output parsers, chains, runnables, document loading, text
splitting, vector stores, retrievers, RAG, tools, tool calling, and AI
agents.

> **Note:** This repository is an independent learning implementation.
> The educational content belongs to CampusX and its respective
> creators. This repository does not claim ownership of the referenced
> course material.

## 🎯 Purpose

The goal of this repository is to build a strong practical foundation in
Generative AI by:

-   Understanding the building blocks of LLM applications
-   Implementing LangChain components individually
-   Learning how different components connect together
-   Building Retrieval-Augmented Generation (RAG) systems
-   Working with vector stores and retrievers
-   Understanding tool calling and AI agents
-   Experimenting with open-source/local LLM workflows
-   Converting theoretical concepts into reusable code

## 🗂️ Repository Structure

``` text
Gen-ai/
│
├── Chains/
├── Models/
├── Prompts/
├── Retrivers/
├── Runnables/
├── Structured_Output/
├── TextSPlitter/
├── Tools/
├── Vector_Stores/
├── document_loader/
├── output_parsers/
├── yt_chatbot/
│
├── langchain_chroma.py
├── test.py
├── requirement.txt
└── README.md
```

## 🧠 Topics Covered

### 1. Models

Understanding how LLMs and model interfaces are used inside GenAI
applications.

### 2. Prompts

Working with prompt templates and designing structured inputs for
language models.

### 3. Structured Output

Getting predictable, machine-readable responses from LLMs instead of
relying only on free-form text.

### 4. Output Parsers

Parsing and transforming model outputs into useful application-level
formats.

### 5. Chains

Connecting multiple operations together to create reusable LLM
workflows.

### 6. Runnables

Understanding LangChain's runnable abstraction and composing different
operations into pipelines.

### 7. Document Loaders

Loading information from documents and other external sources so it can
be processed by an LLM application.

### 8. Text Splitters

Breaking large documents into smaller chunks suitable for embeddings,
retrieval, and LLM context windows.

### 9. Vector Stores

Storing and searching embeddings to enable semantic retrieval.

### 10. Retrievers

Fetching the most relevant pieces of information from a knowledge base.

### 11. Retrieval-Augmented Generation (RAG)

Combining retrieval with generation so an LLM can answer questions using
external knowledge.

### 12. Tools

Connecting LLM applications to external functions and capabilities.

### 13. Tool Calling

Allowing an LLM to decide when a tool/function should be invoked based
on the user's request.

### 14. AI Agents

Combining models, tools, reasoning and execution into more autonomous
workflows.

### 15. YouTube Chatbot

A practical RAG-based project that demonstrates how information from
YouTube content can be processed and used for question answering.

## 🛠️ Tech Stack

-   Python
-   LangChain
-   LangChain integrations
-   Large Language Models (LLMs)
-   Embeddings
-   Chroma / Vector Stores
-   Retrieval-Augmented Generation (RAG)
-   Prompt Engineering
-   Tool Calling
-   AI Agents

The exact dependencies are maintained in `requirement.txt`.

## ⚙️ Installation

### 1. Clone the repository

``` bash
git clone https://github.com/rohanpatil018/Gen-ai.git
cd Gen-ai
```

### 2. Create a virtual environment

``` bash
python -m venv venv
```

Activate it on Windows:

``` bash
venv\Scripts\activate
```

On Linux/macOS:

``` bash
source venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirement.txt
```

### 4. Configure API keys

Some examples may require API keys depending on the model/provider being
used.

Create a `.env` file where required and add the relevant credentials,
for example:

``` env
OPENAI_API_KEY=your_api_key
```

Do **not** commit API keys or other secrets to GitHub.

## ▶️ Running the Examples

Most folders contain topic-specific implementations. Navigate to the
relevant folder and run the Python file:

``` bash
python <filename>.py
```

For example:

``` bash
python test.py
```

For the YouTube chatbot, navigate to:

``` text
yt_chatbot/
```

and follow the implementation inside that directory.

## 🔄 Suggested Learning Path

The repository can be studied in the following order:

``` text
Models
   ↓
Prompts
   ↓
Structured Output
   ↓
Output Parsers
   ↓
Chains
   ↓
Runnables
   ↓
Document Loaders
   ↓
Text Splitters
   ↓
Vector Stores
   ↓
Retrievers
   ↓
RAG
   ↓
Tools
   ↓
Tool Calling
   ↓
AI Agents
   ↓
End-to-End GenAI Applications
```

This progression follows the general conceptual flow of the CampusX
LangChain playlist.

## 🚀 Practical Projects

### YouTube RAG Chatbot

The `yt_chatbot` module demonstrates an end-to-end application using the
RAG approach.

High-level workflow:

``` text
YouTube Content
      ↓
Document / Transcript Loading
      ↓
Text Splitting
      ↓
Embeddings
      ↓
Vector Store
      ↓
Retriever
      ↓
Relevant Context
      ↓
LLM
      ↓
Answer
```

This project brings together several concepts from the repository into a
practical GenAI application.

## 📈 Learning Progress

-   [x] LangChain fundamentals
-   [x] Models
-   [x] Prompts
-   [x] Structured output
-   [x] Output parsers
-   [x] Chains
-   [x] Runnables
-   [x] Document loaders
-   [x] Text splitters
-   [x] Vector stores
-   [x] Retrievers
-   [x] RAG fundamentals
-   [x] Tools
-   [x] Tool calling
-   [x] YouTube chatbot
-   [ ] Advanced RAG
-   [ ] Production-grade GenAI applications
-   [ ] LangGraph / advanced agentic workflows
-   [ ] GenAI evaluation and observability
-   [ ] LLMOps

## 📌 Key Concepts

### RAG

RAG allows an application to retrieve relevant information from an
external knowledge source before asking the LLM to generate an answer.

``` text
User Query
    ↓
Retriever
    ↓
Relevant Documents
    ↓
Prompt + Context
    ↓
LLM
    ↓
Generated Response
```

### Vector Search

Text is converted into numerical embeddings so semantically similar
content can be retrieved even when the exact words do not match.

### Agents

Agents extend basic LLM chains by allowing the model to select and use
tools dynamically to complete a task.

## 📖 Reference

-   **CampusX -- Generative AI using LangChain:**\
    https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0

-   **CampusX -- GenAI Roadmap / introductory overview:**\
    https://www.youtube.com/watch?v=pSVk-5WemQ0

## 👨‍💻 Author

**Rohan Patil**

GitHub:\
https://github.com/rohanpatil018

------------------------------------------------------------------------

⭐ If this repository helps you learn Generative AI, feel free to
explore, experiment, and build on top of these concepts.
