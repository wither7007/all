# import ffmpeg

# audio_input = ffmpeg.input('cut.mp3')
# audio_cut = audio_input.audio.filter('atrim', duration=5)
# audio_output = ffmpeg.output(audio_cut, 'out.mp3')
# ffmpeg.run(audio_output)


import ffmpeg

in_file = ffmpeg.input('pd.mp4')
overlay_file = ffmpeg.input('ov.jpg')
(
    ffmpeg
    .concat(
        in_file.trim(start_frame=10, end_frame=20),
        in_file.trim(start_frame=30, end_frame=40),
    )
    .overlay(overlay_file.hflip())
    .drawbox(50, 50, 120, 120, color='red', thickness=5)
    .output('out.mp4')
    .run()
)


ffmpeg - ss 630 - i cut.mp3 - acodec copy outputfile.mp3
