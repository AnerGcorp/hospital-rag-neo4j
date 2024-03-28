from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate
)
from langchain.schema.messages import HumanMessage, SystemMessage
import dotenv

dotenv.load_dotenv()

chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

review_template_str = """Your job is to use patient
    reviews to answer questions about their experience at a hospital.
    Use the following context to answer questions. Be as detailed
    as possible, but don't make up any information that's not
    from the context. If you don't know an answer, say you don't know.

    {context}

    {question}
"""

review_template = ChatPromptTemplate.from_template(review_template_str)

context = "I had a great stay!"
question = "Did anyone have a positive experience?"



messages = [
    SystemMessage(
        content="""You're an assistant knowledgeable about
        healthcare. Only answer healthcare-related questions."""
    ),
    HumanMessage(content="How do I change a tire?"),
]
print(chat_model.invoke(messages))