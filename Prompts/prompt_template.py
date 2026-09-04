from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=[
        "paper_input",
        "style_input",
        "length_input"
    ],
    template="""
You are an AI research assistant.

Explain the research paper "{paper_input}" in a {style_input} style.

The explanation should be {length_input}.

Include:
1. Problem Statement
2. Key Idea
3. Architecture
4. Advantages
5. Limitations
6. Real-world Applications
"""
)

template.save('template.json')