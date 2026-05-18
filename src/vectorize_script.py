import os
from dotenv import load_dotenv

from src.vectorize_book import CLASS_SUBJECT_NAME
from vectorize_book import vectorize_book_and_store_to_db, vectorize_chapter

load_dotenv()

vectorize_book_and_store_to_db(
    CLASS_SUBJECT_NAME,"class_12_biology_vector_db"
)

vectorize_chapter(CLASS_SUBJECT_NAME)

