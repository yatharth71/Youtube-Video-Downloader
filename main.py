from pytube import YouTube

video_link  = input("Enter the link of the video which you wanted to download : ")

YouTube(video_link).streams.get_highest_resolution().download("./Downloads/")
