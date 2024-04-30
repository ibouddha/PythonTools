import pytube

link = input("entrer votre lien youtube: ")
video_download = pytube.YouTube(link)
video_download.streams.first().download()
print("Video Successfully downloaded: ", video_download)