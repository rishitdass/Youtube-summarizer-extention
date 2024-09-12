from youtube_transcript_api import YouTubeTranscriptApi
import os
from openpipe import OpenAI
import re

def auto_bold_colon_phrases(text):
    # Use a regex pattern to find any text followed by a colon, and wrap it in '**'
    formatted_text = re.sub(r'(\w.*?):', r'<strong>\1:</strong>', text)
    return formatted_text


# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "API KEY HERE"
client = OpenAI()


# Function to extract transcript from YouTube video
def get_transcript(video_url):
    # Extract video ID from the YouTube URL
    video_id = video_url.split('v=')[-1]

    # Fetch the transcript
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return ' '.join([item['text'] for item in transcript])
    except Exception as e:
        return f"Error: {str(e)}"
def format_heading(text):
    # Define a pattern to match the desired format
    pattern = r'\n(\S+(?:\s+\S+){0,2})\n'  # Matches words between two newlines with less than 4 words

    # Replace matches with the desired format
    formatted_text = re.sub(pattern, r'\n##\1\n', text)

    return formatted_text

def format(text):
    formatted_text=[]

    lines=text.splitlines()
    for line in lines:
        words=line.split()
        if len(words)<=7:
            formatted_text.append('<h2>'+line+'</h2>')
        else:
            formatted_text.append('<p style="padding-bottom: 15px;">'+auto_bold_colon_phrases(line)+'</p>')
    return formatted_text
# Function to generate summary using OpenAI
def generate_summary(transcript_text):
    try:
        completion = client.chat.completions.create(
            model="openpipe:olive-papers-take",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant specialized in summarizing YouTube video transcripts."
                },
                {
                    "role": "user",
                    "content": f"Given the transcript of a YouTube video, your task is to generate a straight to point and informative summary. \n"
                               f"The summary should cover key points, main ideas, and critical information, organized in a coherent and structured way. \n"
                               f"Ensure that the summary does not exceed 1000 words.\n"
                               f"Make sure that the summary retains the flow and structure of the original transcript while omitting unnecessary details.\n"
                               f"Transcript:\n {transcript_text} "
                }
            ],
            temperature=0,
            openpipe={
                "tags": {
                    "prompt_id": "counting",
                    "any_key": "any_value"
                }
            },
        )

        return completion.choices[0].message.content
    except Exception as e:
        print("caught error")
        print(e)
        return f"Error generating summary: {str(e)}"

def url_to_summarize(url):
    transcript = get_transcript(url)
    if "Error" in transcript:
        failedRes = '<p style="padding-bottom: 15px;">'+transcript+'</p>'
        return failedRes, 204, {'Content-Type': 'text/html'}
    else:
        output = generate_summary(transcript)
        formated_text = format(output)
        summary = '\n'.join(formated_text)
        return summary, 200, {'Content-Type': 'text/html'}


