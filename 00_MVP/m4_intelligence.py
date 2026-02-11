"""
Manager 4: Intelligence Layer.
Performs Sentiment Analysis and Insight Generation using Llama 3.2.
Optimized for 8GB RAM via 4-bit quantization (Ollama).
"""
import ollama
import json

class IntelligenceManager:
    def __init__(self, model_name: str = "llama3.2:3b-instruct-q4_K_M"):
        # Requirement: Use 4-bit quantized model to prevent OOM
        self.model = model_name

    def analyze_sentiment(self, text: str) -> dict:
        """Requirement FUNC01: Sentiment Analysis on geopolitical data."""
        prompt = (
            "Analyze the sentiment of the following geopolitical text. "
            "Return ONLY a JSON object with keys: 'sentiment' (Pro-USA, Pro-Iran, or Neutral) "
            f"and 'score' (0.0 to 1.0). Text: {text}"
        )
        
        try:
            response = ollama.generate(
                model=self.model,
                prompt=prompt,
                stream=False,
                format="json" # Ensures structured output for Manager 5/6
            )
            return json.loads(response['response'])
        except Exception as e:
            print(f"Intelligence Error: {e}")
            return {"sentiment": "Unknown", "score": 0.0}

    def generate_insight(self, context_chunks: list, query: str) -> str:
        """Synthesizes multiple VDB chunks into a single intelligence report."""
        context_str = "\n".join(context_chunks)
        prompt = (
            f"Based on these authoritative sources:\n{context_str}\n"
            f"Answer the following query regarding USA-Iran Geopolitics: {query}"
        )
        
        response = ollama.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        return response['response']

# Example Usage
if __name__ == "__main__":
    brain = IntelligenceManager()
    # test_text = "Tensions rise as diplomatic channels close between Washington and Tehran."
    # print(brain.analyze_sentiment(test_text))