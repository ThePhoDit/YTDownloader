from pytube import YouTube
from os import rename

ytInput = input('Enter a YouTube link: ')
yt = YouTube(ytInput)

# Provide info about the video.
print(f'''
Title: {yt.title}
Views: {yt.views}
Rating: {yt.rating}
''')

formatInput = input('Get the video or the audio: ')
if formatInput.lower() == 'video':
    stream = yt.streams.filter(progressive=True).get_highest_resolution()
elif formatInput.lower() == 'audio':
    stream = yt.streams.filter(only_audio=True)[0]
else:
    print('Invalid type. Please, start over.')
    exit()

print('Downloading...')
stream.download()
if formatInput.lower() == 'audio':
    rename(f'{yt.title}.mp4', f'{yt.title}.mp3')

print('Downloaded!')
