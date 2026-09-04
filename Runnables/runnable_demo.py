from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


model=ChatGoogleGenerativeAI(model='gemini-2.5-flash',temperature=0.7)


prompt=PromptTemplate(
    template='suggest a catchy blog title about {topic}', 
    input_variables=['topic']
    )

topic=input("Enter the topic: ")

formatted_prompt=prompt.format(topic=topic)

blog_title=model.predict(formatted_prompt)

print("Generated Blog Titile: ",blog_title)
