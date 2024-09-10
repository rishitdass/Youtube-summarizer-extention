import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import textwrap
import os
from openpipe import OpenAI
import re
import markdown
import nltk

def auto_bold_colon_phrases(text):
    # Use a regex pattern to find any text followed by a colon, and wrap it in '**'
    formatted_text = re.sub(r'(\w.*?):', r'<strong>\1:</strong>', text)
    return formatted_text


# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "opk_8abdaf9e82aa04173d5d52e9ddf8e23396fd555077"
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
        if len(words)<=4:
            formatted_text.append('<h2>'+line+'</h2>')
        else:
            formatted_text.append('<p>'+auto_bold_colon_phrases(line)+'</p>')
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
        return f"Error generating summary: {str(e)}"

# Streamlit UI
def main():
    st.title("YouTube Transcript Summarizer")
    st.write("Enter the YouTube video link below, and the app will fetch the transcript and summarize it.")

    # Input for the YouTube video URL
    video_url = st.text_input("Enter YouTube video URL")

    if st.button("Summarize"):
        if video_url:
            # Fetch transcript
            with st.spinner('Fetching transcript...'):
                transcript = get_transcript(video_url)

            # Check if transcript was successfully retrieved
            if "Error" in transcript:
                st.error(transcript)
            else:
                # Generate summary
                with st.spinner('Generating summary...'):
                    output = generate_summary(transcript)
                    formated_text = format(output)
                    summary = '\n'.join(formated_text)
                    print(summary)
                    # Display summary
                    # st.subheader("Summary")
                    st.markdown("<h2>Summary<h1>"+summary,unsafe_allow_html=True)
        else:
            st.error("Please enter a valid YouTube URL.")


# Run the app
if __name__ == '__main__':
    main()
