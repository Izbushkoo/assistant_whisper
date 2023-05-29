import openai
import speech_recognition as sr


# recognizer = sr.Recognizer()
#
# with sr.Microphone(device_index=) as source:
#     print('say smth')
#     audio = recognizer.listen(source, phrase_time_limit=4)
#
# # recognize speech using Whisper API
# OPENAI_API_KEY = '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'  # pay to go
#
# try:
#     print(
#         f"Whisper API thinks you said {recognizer.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)}")
# except sr.RequestError as e:
#     print("Could not request results from Whisper API")
#
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(
        index, name))
