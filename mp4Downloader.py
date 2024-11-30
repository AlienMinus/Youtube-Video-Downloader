import yt_dlp

x = str(input("Enter Video Url:"))
yt_dlp.YoutubeDL({'format':'best','outtmpl':'%(title)s.%(ext)s'}).download([x])
print("Video Downloaded Successfully")

