# AI Bot with Video Input and Voice Output

## Overview
This project features an AI bot that takes video input through a web interface created with Shiny, processes the input using the GPT-4 API to perform various tasks, and then outputs its response in voice format. The bot is capable of handling tasks such as identifying devices, solving math equations, and responding to Hindi language input, among other potential uses.

## Demo Video
Check out the [demo video](https://drive.google.com/file/d/1NniZfWqZZnJpzz1u2-2whKS_hH-SLRql/view?usp=sharing) to see the AI bot in action.

## Features
- **Versatile Task Handling**: Uses GPT-4o API for understanding and processing various inputs.
- **Object Identification**: Can recognize objects (e.g., phone) from the video input.
- **Math Equation Solving**: Extracts and solves math equations from the video input.
- **Multiple Languages Response**: Understands and responds to input given in Any language.
- **Voice Output**: Provides responses in voice format using Whisper for speech synthesis.

## Technology Stack
- **Shiny**: Web framework to create interactive web applications.
- **Python**: For processing video input and generating responses.
- **GPT-4o API**: For advanced natural language processing and understanding.
- **Whisper**: For converting text responses to speech.
- **FFmpeg**: For handling audio and video file conversions and manipulations.
