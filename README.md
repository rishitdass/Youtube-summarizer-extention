

# YouTube Video Summarizer Extension

This project is a YouTube video summarization browser extension powered by a fine-tuned **Llama 3.1 8B model**. It provides concise summaries of YouTube videos using their transcripts. This tool can be applied in various contexts, including note-taking for study materials, generating recipes from cooking videos, and more.

## Features

- Summarizes YouTube video transcripts using a fine-tuned Llama 3.1 8B model.
- Simple browser extension for ease of use.
- Extracts the video transcript and generates a concise summary.
- Built using Flask, JavaScript, HTML, and CSS.

## Use Cases

1. **Study Material Note-Taking**: Quickly extract important notes from educational videos.
2. **Recipe Generation**: Get detailed recipes from cooking videos with just a click.
3. **Podcast Highlights**: Summarize long podcast discussions into key points.
4. **Tutorial Key Takeaways**: Get the main steps or instructions from how-to videos.
5. **Webinar Summaries**: Capture the essence of webinars for later review.

## Fine-tuned Model

The summarization model used in this extension is based on **Llama 3.1 8B**, which has been fine-tuned on a specialized dataset to improve its summarization capabilities for video transcripts.

## Installation

1. Clone this repository:
 
   ```bash
   https://github.com/rishitdass/Youtube-summarizer-extention.git

2. Install required python packages:
  ```bash
   pip install youtube_transcript_api openpipe flask flask_cors re
  ```
## Python Dependecies
- `youtube_transcript_api:` To retrieve transcripts from YouTube videos.
- `openpipe:` To connect to and use the fine-tuned Llama model.
- `flask:` For handling the backend server of the extension.
- `flask_cors:` For managing cross-origin resource sharing in the Flask app.
- `re:` For regular expression operations when processing the transcript.

## Tech Stack
- Backend: Python (Flask)
- Frontend: HTML, CSS, JavaScript
- Model: Youtube-Video-Summerizer Mpdel Fine-tuned Llama 3.1 8B for summarization

## How It Works
- The user selects a YouTube video to summarize.
- The extension extracts the transcript using youtube_transcript_api.
- The transcript is sent to the backend Flask server, which processes it and uses the fine-tuned Llama 3.1 8B model to generate a summary.
- The summary is displayed in the extension UI for the user to view.

## Dataset Used

Dass, Rishit. 2024. Youtube-transcript-Summarizer (Revision 2b12441). Hugging Face. https://doi.org/10.57967/hf/3040.

## Summarization Model Used

Dass, Rishit. 2024. Youtube-Video-Summarizer (Revision 1ce76d4). Hugging Face. https://doi.org/10.57967/hf/3037.

## License
This project is licensed under the Llama 3 Community License Agreement. See the LICENSE file for more details.

