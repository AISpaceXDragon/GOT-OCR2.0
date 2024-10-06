## NOTE:(To the reviewer of my work(IIT R))
- Before looking into the project, I would like to convey that with all efforts to satisfy your requirements,I have tried my level best to implement an OCR model to extract both English and Hindi Texts from an image.But due to limited compute resources and data,I was unable to finetune an effective model for Hindi OCR(loss value 0.8) so I only implemented English version.
- Also note that this model takes significantly large processing time per image i.e., 5-7 minutes as per my observation during inference because it runs on CPU.As GOT OCR2.0 is only available on GPU, but due to no compute resources, I implemented a CPU version of it and uploaded it HuggingFace Models Hub [https://huggingface.co/srimanth-d/GOT_CPU](https://huggingface.co/srimanth-d/GOT_CPU) and contributing to the CPU version of GOT as mentioned in the official repository of [GOT OCR2.0](https://github.com/ElvisClaros/GOT-OCR2.0).
- Here are the finetuned model weights which were finetuned on this dataset --> [https://huggingface.co/datasets/damerajee/hindi-ocr](https://huggingface.co/datasets/damerajee/hindi-ocr) Link to finetuned weights(finetuned using [ms-swift](https://github.com/modelscope/ms-swift)) --> [https://drive.google.com/file/d/1qbupBRk8yIgiD3WzIwKP54-Fn4wpgpg1/view?usp=sharing](https://drive.google.com/file/d/1qbupBRk8yIgiD3WzIwKP54-Fn4wpgpg1/view?usp=sharing)
- I could have quantized the model, but the accuracy reduces greatly.So I refrained from doing so.
- I also noted that few other students who did this task used my implementation of GOT CPU from HuggingFace(not boasting about my work or myself).


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
     pip install -r requirements.txt
     ```
     If you are running this command before cloning this repository you may get an error. That is first clone this repository and then change your current directory to GOT_OCR2.0 .
     The commands for which are given below in the [Running the Application Locally](#running-the-application-locally) section step number 1.

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
   git clone https://github.com/AISpaceXDragon/GOT-OCR2.0.git
   ```

   ```bash
   cd GOT_OCR2.0
   ```

2.**Run the streamlit app locally**
  ```bash
  streamlit run app.py
  ```
This command must be run only after executing the "step 1.clone the repository" given above.

## Deployment
This application is deployed on Streamlit Sharing and HuggingFace Spaces.The links for both of them are given below.

1.Link(Streamlit Sharing) - Removed due to some issue,but if you want to access it here is the link -->[https://got-ocr20-nwcwgf2njkjf8esqyfwxhc.streamlit.app](https://got-ocr20-nwcwgf2njkjf8esqyfwxhc.streamlit.app)

2.Link(HuggingFace Spaces) - [https://huggingface.co/spaces/srimanth-d/OCR_app](https://huggingface.co/spaces/srimanth-d/OCR_app)
