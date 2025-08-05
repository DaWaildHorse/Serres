from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
import os
import getpass
from langchain_google_genai.llms import GoogleGenerativeAI
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_community.graphs import Neo4jGraph


loader = TextLoader("output.txt")
documents= loader.load()
text_splitter = CharacterTextSplitter(chunk_size=200 , chunk_overlap= 20)
texts = text_splitter.split_documents(documents)

os.environ["GOOGLE_API_KEY"] = getpass.getpass()

llm = GoogleGenerativeAI(model= "gemini-2.5-flash")

llm_transformer = LLMGraphTransformer(llm= llm)
graph_doc = llm_transformer.convert_to_graph_documents(texts)
graph_store = Neo4jGraph(url='bolt://localhost:7687' , username= 'neo4j', password= 'administrador')
graph_store.add_graph_documents(graph_doc, baseEntityLabel=True, include_source=True)
