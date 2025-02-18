from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()


client = OpenAI(
    api_key=os.getenv("API_KEY_1"),
)


def get_text_response(user_input: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "assistant",
                    "content": "Act like a friendly taxi dispatcher. Only talk about the taxi order. If the user tries to talk about something else deflect the topic and go back to the order."
                },
                {
                    "role": "user",
                    "content": user_input
                },
            ],
            max_tokens=150,
            temperature=0.7,
        )
        assistant_reply = completion.choices[0].message.content

        return assistant_reply
    except Exception as e:
        return f"An error occurred {str(e)}"


def start_text_conversation() -> None:
    print("Welcome to the Taxi Dispatcher Assistant. Type 'exit' to quit the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            break

        assistant_response = get_text_response(user_input)
        print(f"Assistant: {assistant_response}")


def get_audio_transcription() -> str:
    audio_file = open('./audio_file.mp3', 'rb')
    transcription = client.audio.transcriptions.create(
        model='whisper-1',
        file=audio_file,
    )

    return transcription.text


if __name__ == "__main__":
    print(get_audio_transcription())