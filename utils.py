from pydub import AudioSegment


def convert_ogg_to_wav(input_file, output_file):
    ogg_audio = AudioSegment.from_ogg(input_file)
    ogg_audio.export(output_file, format='wav')
