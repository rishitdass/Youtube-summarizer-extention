from summarizer import url_to_summarize

def add_summary(data):
    videoUrl = data['video_url']
    res = url_to_summarize(videoUrl)
    print(type(res))
    print(res)
    return res
