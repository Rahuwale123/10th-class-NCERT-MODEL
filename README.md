# School Master Chatbot

A RAG-based chatbot for school students using Gemini and vector search.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure Qdrant is running locally on port 6333

3. Run the application:
```bash
python -m uvicorn app.main:app --reload
```

## API Usage

The API will be available at `http://localhost:8000`

- API Documentation: `http://localhost:8000/docs`
- Endpoint: POST `/ask`
- Request Body:
```json
{
    "query": "Your question here"
}
```

## Features

- Vector search using Qdrant
- Text generation using Google's Gemini model
- FastAPI backend with automatic API documentation
- Clean, modular code structure 