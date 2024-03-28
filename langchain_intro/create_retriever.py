from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import dotenv

REVIEWS_CSV_PATH = '../data/reviews.csv'
REVIEWS_CHROMA_PATH = 'chroma_data'

dotenv.load_dotenv()

loader = CSVLoader(
    file_path=REVIEWS_CSV_PATH,
    source_column='review'
)

reviews = loader.load()

reviews_vector_db = Chroma.from_documents(
    documents=reviews,
    embedding=OpenAIEmbeddings(),
    persist_directory=REVIEWS_CHROMA_PATH
)

question = """Has anyone complained about communication with the hospital staff?"""

relevant_docs = reviews_vector_db.similarity_search(question)

# print(relevant_docs)