from utils.logger import logger

BASE = 256
PRIME = 101

def rabin_karp(text1: str, text2: str, window_size: int) -> tuple[list[str], list[int]]:
    matched_strings = []
    matched_positions = []

    n = len(text1)
    m = window_size

    if m > n or m > len(text2):
        logger.debug("Window size larger than one of the texts. No matches possible.")
        return matched_strings, matched_positions

    logger.debug(f"Starting Rabin-Karp | text1 length: {n} | window_size: {m}")

    # h = BASE^(m-1) % PRIME
    # Used to remove the leftmost character during rolling hash
    h = 1
    for _ in range(m - 1):
        h = (h * BASE) % PRIME

    # Slide window across text2 and collect all window hashes
    pattern_hashes = set()
    pattern_windows = set()

    pattern_hash = 0
    for i in range(m):
        pattern_hash = (BASE * pattern_hash + ord(text2[i])) % PRIME

    pattern_hashes.add(pattern_hash)
    pattern_windows.add(text2[0:m])

    for i in range(1, len(text2) - m + 1):
        pattern_hash = (BASE * (pattern_hash - ord(text2[i - 1]) * h) + ord(text2[i + m - 1])) % PRIME
        pattern_hash = (pattern_hash + PRIME * BASE) % PRIME
        pattern_hashes.add(pattern_hash)
        pattern_windows.add(text2[i:i + m])

    # Slide window across text1 and search for matches
    text1_hash = 0
    for i in range(m):
        text1_hash = (BASE * text1_hash + ord(text1[i])) % PRIME

    if text1_hash in pattern_hashes:
        window = text1[0:m]
        if window in pattern_windows:
            matched_strings.append(window)
            matched_positions.append(0)
            logger.debug(f"Match found at position 0: '{window}'")

    for i in range(1, n - m + 1):
        text1_hash = (BASE * (text1_hash - ord(text1[i - 1]) * h) + ord(text1[i + m - 1])) % PRIME
        text1_hash = (text1_hash + PRIME * BASE) % PRIME

        if text1_hash in pattern_hashes:
            window = text1[i:i + m]
            if window in pattern_windows:
                matched_strings.append(window)
                matched_positions.append(i)
                logger.debug(f"Match found at position {i}: '{window}'")

    logger.debug(f"Total matches found: {len(matched_strings)}")
    return matched_strings, matched_positions