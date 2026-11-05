from pathlib import Path
from typing import Iterable, List, Optional
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from docx import Document as DocxDocument

SUPPORTED = {".pdf",".text", ".md", ".docx"}

def load_file(path: Path)-> list[Document]:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return PyPDFLoader(str(path)).load()
    if( suffix == ".text" or suffix == ".md"):
        return TextLoader(str(path), encoding="utf-8").load()

    if suffix == ".docx":
        doc = DocxDocument(str(path))
        text = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
        return [Document(page_content=text, metadata={"source": str(path)})]
    raise ValueError(f"Unsupported file type: {suffix}") 


def chunk_documents(docs: Iterable[Document])-> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,   
        chunk_overlap=100,
       add_start_index=True,
    )
    return splitter.split_documents(list(docs))