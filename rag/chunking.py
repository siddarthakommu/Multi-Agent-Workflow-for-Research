from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text, chunk_size=800, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_text(text)
