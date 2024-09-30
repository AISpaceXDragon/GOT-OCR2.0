# Web-Based Optical Character Recognition (OCR) Prototype

## Objective
This web application demonstrates the ability to perform Optical Character Recognition (OCR) on an uploaded image containing text in both **Hindi** and **English**. It also implements a basic keyword search functionality based on the extracted text. The prototype is deployed and accessible online via a live URL.

## Features
- **Image Upload**: Supports common image formats such as JPEG, JPG and PNG.
- **OCR Processing**: Extracts text in Hindi and English from the uploaded image.
- **Keyword Search**: Allows users to search within the extracted text and highlights matching sections.
- **Live Deployment**: Accessible via a public URL.

## Technology Stack
- **Backend**: Python
- **OCR Models**: 
  - Huggingface Transformers (General OCR Theory model(GOT OCR2.0)
  - PyTorch for model execution
- **Web Framework**: Streamlit
- **Deployment**: HuggingFace Spaces, Streamlit Sharing.

## Tasks Overview

### Task 1: Environment Setup and OCR Implementation
1. **Environment Setup**:
   - Set up the environment with the required dependencies:
     ```bash
     pip install torch transformers streamlit
     ```

2. **OCR Model Implementation**:
     - General OCR Theory (GOT), a 580M end-to-end OCR model was used to build this application.

### Task 2: Web Application Development
1. **Image Upload**: 
   - Allow users to upload a single image for OCR.
   
2. **Text Extraction**:
   - Use the chosen OCR model to extract text and display it on the page.

3. **Keyword Search**:
   - Implement a basic search feature where users can input a keyword.
   - Highlight the matching text within the extracted content.

### Task 3: Deployment
1. **Deploy the Web Application**:
   - Deploy the web app using platforms like Hugging Faces, Streamlit Sharing, or any other suitable platform.
   - Ensure it is accessible via a public URL.

## Running the Application Locally
To run the application on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AISpaceXDragon/GOT-OCR2.0.git```
   ```bash
   cd GOT_OCR2.0
   ```

2.**Run the streamlit app locally**
  Run the command-
```bash
streamlit run app.py
```
This command must be run only after executing the "step 1.clone the repository" given above.

## Deployment
This application is deployed on Streamlit Sharing and HuggingFace Spaces.The links for both of them are given below.
Link(Streamlit Sharing) - To be posted soon.
Link(HuggingFace Spaces) - To be posted soon.
