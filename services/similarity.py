from utils.logger import logger
from utils.preprocess import preprocess
from algorithms.rabin_karp import rabin_karp

WINDOW_SIZE = 20

def calculate_similarity(text1: str, text2: str) -> dict:
    logger.info("Similarity calculation started")

    if not text1 or not text2:
        logger.warning("One or both texts are empty")
        return {"similarity_score": 0.0, "matched_segments": []}

    clean_text1 = preprocess(text1)
    clean_text2 = preprocess(text2)

    logger.debug(f"clean_text1 length: {len(clean_text1)} | clean_text2 length: {len(clean_text2)}")

    if not clean_text1 or not clean_text2:
        logger.warning("Text became empty after preprocessing")
        return {"similarity_score": 0.0, "matched_segments": []}

    logger.debug(f"Running Rabin-Karp with window_size={WINDOW_SIZE}")
    matched_strings, matched_positions = rabin_karp(clean_text1, clean_text2, WINDOW_SIZE)

    # Track which character positions in text2 were matched
    # Using a set avoids counting the same character twice
    matched_positions_set = set()
    unique_segments = []
    seen_segments = set()

    for match, position in zip(matched_strings, matched_positions):
        for char_index in range(position, position + WINDOW_SIZE):
            matched_positions_set.add(char_index)

        if match not in seen_segments:
            unique_segments.append(match)
            seen_segments.add(match)

    unique_matched_chars = len(matched_positions_set)
    similarity_score = (unique_matched_chars / len(clean_text2)) * 100
    similarity_score = min(similarity_score, 100.0)
    similarity_score = round(similarity_score, 2)

    logger.info(f"Similarity score: {similarity_score}% | Matched segments: {len(unique_segments)}")

    return {
        "similarity_score": similarity_score,
        "matched_segments": unique_segments
    }