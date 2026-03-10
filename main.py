import json
from groq import Groq

# Replace with your actual Groq API Key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def generate_path(topic):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a professional tutor. Return ONLY a JSON object with this structure: {'topic': str, 'steps': [{'title': str, 'description': str, 'source': str}]}"
                },
                {"role": "user", "content": f"Create a 5-step learning roadmap for {topic}"}
            ],
            response_format={"type": "json_object"}
        )
        return json.loads(completion.choices[0].message.content)
    except Exception as e:
        return {"error": str(e), "steps": []}