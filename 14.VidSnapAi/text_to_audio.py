from elevenlabs.client import ElevenLabs
from config import ELEVENLABS_API_KEY
import uuid
import os

elevenlabs = ElevenLabs(
  api_key=ELEVENLABS_API_KEY,
)


def text_to_Speech(user_input,folder):
    audio = elevenlabs.text_to_speech.convert(
    text=user_input,
    voice_id="JBFqnCBsd6RMkjVDRZzb",  # "George" - browse voices at elevenlabs.io/app/voice-library
    model_id="eleven_v4",
    output_format= "mp3_44100_128",
  )

    output_path = os.path.join(os.path.dirname(__file__), "user_upload", folder, "output.mp3")
  
    with open(output_path, "wb") as f:
        for chunk in audio:
           f.write(chunk)


# if __name__ == "__main__":
#     while True:
#        user_input = input("Enter the text that you want to convert : ")
#        if(user_input == "exit"):
#            break
#        text_to_Speech(user_input=user_input)
