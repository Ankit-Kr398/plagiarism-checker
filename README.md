# Text Similarity & Plagiarism Checker

A backend system that compares two text documents and returns a similarity score using the Rabin-Karp string matching algorithm. Built with Python and Flask — no AI or external similarity libraries used.

---

## Features

- Preprocesses text before comparison (lowercase, remove punctuation, normalize whitespace)
- Detects exact and near-exact substring matches using Rabin-Karp
- Returns similarity score as a percentage
- Returns matched text segments
- REST API with input validation and error handling
- Centralized logging throughout the application

---

## Folder Structure

```plaintext
plagiarism_checker/
├── app.py
├── routes/
│   ├── __init__.py
│   └── compare.py
├── services/
│   ├── __init__.py
│   └── similarity.py
├── algorithms/
│   ├── __init__.py
│   └── rabin_karp.py
├── tests/
│   ├── __init__.py
│   └── test_similarity.py
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   └── preprocess.py
├── requirements.txt
└── README.md
```

---

## Setup Instructions

**1. Clone or download the project**
```bash
cd plagiarism_checker
```

**2. Create and activate virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python app.py
```

Server starts at `http://localhost:5000`

---

## API Endpoints

### GET /api/health
Check if server is running.

```bash
curl.exe http://localhost:5000/api/health
```

Response:
```json
{
  "status": "Server is running"
}
```

---

### POST /api/compare
Compare two texts and get similarity score.

```bash
curl.exe -X POST http://localhost:5000/api/compare -H "Content-Type: application/json" -d "{\"text1\": \"the quick brown fox jumped over the lazy dog\", \"text2\": \"the quick brown fox\"}"
```

Request body:
```json
{
  "text1": "first document text here",
  "text2": "second document text here"
}
```

Response:
```json
{
  "similarity_score": 67.3,
  "matched_segments": ["the quick brown fox"],
  "status": "High similarity detected"
}
```

Status labels:
- `score >= 70` → High similarity detected
- `score >= 40` → Moderate similarity detected
- `score < 40`  → Low similarity detected

---

## Run Unit Tests

```bash
python -m unittest tests/test_similarity.py -v
```

---

## Known Limitations

- Does not detect paraphrasing or synonym substitution
- Does not understand meaning — only matches text character by character
- Compares only two documents at a time, no database
- Similarity score depends on window size (currently fixed at 20)
- Short texts under 20 characters will always score 0 due to window size

---

## Future Improvements

- Adjustable window size via API parameter
- Support for comparing multiple documents
- File upload support (PDF, DOCX)
- Persistent storage to store and search against a document database
- Highlighted diff view showing exactly which segments matched