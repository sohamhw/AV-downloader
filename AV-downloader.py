from pytube import YouTube

def video_download():
    video = YouTube(url)
    print(video.title)
    formats = video.streams.filter(file_extension='mp4', type='video', progressive=True)
    vid_list = list(enumerate(formats))
    for i in vid_list:
        print(i)
    stream_no = int(input('select the stream:'))
    print('download has started...')
    formats[stream_no].download(download_path)
    print('download completed.')


def audio_download():
    audio = YouTube(url)
    print(audio.title)
    formats = audio.streams.filter(only_audio=True)
    vid_list = list(enumerate(formats))
    for i in vid_list:
        print(i)
    stream_no = int(input('select the stream:'))
    print('download has started...')
    formats[stream_no].download(download_path)
    print('download completed.')

print("**************WELCOME**************")
print("***********made by SO-ham**********")
print("Enter the url from which you have to download.")
url = input("URL:- ")
format_input = int(input('Select the type of format you need:\n1)Audio\n2)Video\nPress the no. according to the need:\n'))
download_path = str(input('Enter the file path to save the file to respective place\nDefault is C:\\Users\\$username$\\Downloads:\n'))
if (download_path == ''):
    download_path = 'C:\\Users\\soham\\Downloads'
if (format_input == 1):
    audio_download()
elif (format_input == 2):
    video_download()
else:
    print('Entered wrong input')
