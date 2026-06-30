import base64

base64_audio = """
#Put the link you recognize as base64 to decode the link
"""

audio_data = base64.b64decode
  (cow_base64)
with open("cow_base64.mp3", "wb") as f:
  f.write(audio_data)

print("Audio file successfully created as a cow audio mp3")
