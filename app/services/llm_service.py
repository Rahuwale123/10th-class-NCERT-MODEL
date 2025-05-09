import google.generativeai as genai
from app.config import GEMINI_API_KEY, GEMINI_MODEL

class LLMService:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(GEMINI_MODEL)

    def generate_response(self, query: str, context: str) -> str:
        """
        Generate a response using Gemini model
        """
        prompt = (
            f"You are a knowledgeable assistant for school students. Answer the user's question using ONLY the textbook context provided below. "
            f"Keep your answer clear, student-friendly, and detailed. If useful, use bullet points for clarity. Do NOT generate charts, code, or unrelated data. "
            f"If no clear answer is found in the context, say so politely.\n\n"
            f"Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"
        )
        
        response = self.model.generate_content(prompt)
        return response.text.strip() 