from google import genai

# 🔑 PUT YOUR GEMINI API KEY BETWEEN THE QUOTES
API_KEY = "YOUR_API_KEY_HERE"

client = genai.Client(api_key=API_KEY)

print("🤖 Gemini AI Assistant")
print("Type 'exit' to stop.")
print("-" * 40)

while True:
    try:
        question = input("\nYou: ")

        if question.lower() == "exit":
            print("AI: Bye! 👋")
            break

        if not question.strip():
            continue

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=question
        )

        print("\nAI:", response.text)

    except Exception as e:
        print("\n❌ Error:", e)