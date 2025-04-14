from google import genai

client = genai.Client(api_key="AIzaSyAUyJtRqHZlbW7pnx7vRoJ80OKqQO3st5w")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Do you Know about an AI Software Engineer?"
)

print(response.text)
