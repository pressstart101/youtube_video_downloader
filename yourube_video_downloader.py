import pytube

url = 'https://www.youtube.com/watch?v=blah'

youtube = pytube.YouTube(url)


all_tags = youtube.streams.all()
for i in all_tags:
    print(i) 


video = youtube.streams.get_by_itag(22)
video.download('/your/path/')
print('done')
