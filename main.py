import os

import script
from pydub import AudioSegment

video_file = r"C:\Users\anwar\Nextcloud\Meeting Personal\InfoImage\infoimage leads\Zoom Meeting 2023-06-10 00-09-01_optimized.mp4"

song = AudioSegment.from_file(video_file, "mp4")

# PyDub handles time in milliseconds
ten_minutes = 10 * 60 * 1000
total_length = len(song)

# loop through the song, adding 10 minutes to each slice
for i in range(0, total_length, ten_minutes):
    # add 10 minutes
    t1 = i
    t2 = i + ten_minutes

    # limit the last slice to the total_length
    if t2 > total_length:
        t2 = total_length

    # create a new file for each slice
    sliced_audio = song[t1:t2]
    sliced_audio.export(f"slice{i}.mp3", format="mp3")

    script.api_key = os.environ["OPENAI_API_KEY"]

    response = script.whi