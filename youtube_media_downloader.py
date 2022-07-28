from pytube import YouTube, Playlist


def single_video(link):
    youtube1 = YouTube(link)
    videos = youtube1.streams
    resultion = int(input("Press 0 for 144p \n 1 for 360p \n 2 for 720p \n 3 for 1080p \n Enter: "))
    videos[resultion].download()

def single_audio(link):
    youtube1 = YouTube(link)
    videos = youtube1.streams.filter(only_audio=True)
    videos[0].download()

def playlist_vedios(link):
    py = Playlist(link)
    for video in py.videos:
            video.streams.get_highest_resolution().download()

def playlist_audio(link):
    py = Playlist(link)
    for video in py.videos:
        video.streams.get_audio_only().download()


def main():
    
    user_choice = int(input("Press 0 if you want to download single vedio \n Press 1 if you want to download single audio \n Press 2 to download complete playlist videos \n Press 3 to download complete playlist audios \n Enter : "))
    
    match user_choice:
        case 0:
            link = input("Enter the url of the vedio : ")
            single_video(link)
            print("Video downloaded successfully.")
        case 1:
            link = input("Enter the url of the vedio : ")
            single_audio(link)
            print("Audio downloaded successfully.")
        case 2:
            link = input("Enter the url of playlist : ")
            playlist_vedios(link)
            print("All videos downloaded successfully.")
        case 3:
            link = input("Enter the url of playlist : ")
            playlist_audio(link)
            print("All audios downloaded successfully.")
        case _:
            print("Invalid Input !!!!!")         

main()