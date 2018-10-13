from youtube_dl import YoutubeDL
# dl = YoutubeDL()
# dl.dowload(["https://www.youtube.com/watch?v=0I647GU3Jsc"])
options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
dl = YoutubeDL(options)
dl.download(['Youngblood '])

options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
dl = YoutubeDL(options)
dl.download(['On My Way to You'])