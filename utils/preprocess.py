import re
import string
from utils.logger import logger

def preprocess(text: str) -> str:
    logger.debug(f"Preprocessing text of length {len(text)}")

    # Step 1: Lowercase
    text = text.lower()

    # Step 2: Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Step 3: Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    logger.debug(f"Preprocessed text length: {len(text)}")
    return text