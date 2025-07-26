from openai import OpenAI
import google.generativeai as genai

def generate_answer(query, docs, fallback="openai"):
    prompt = f"""Use this context to answer:\n\n{docs[0]}\n\nQ: {query}\nA:"""
    if fallback == "openai":
        response = OpenAI().ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    else:
        genai.configure(api_key="YOUR_GEMINI_API_KEY")
        model = genai.GenerativeModel("gemini-pro")
        return model.generate_content(prompt).text