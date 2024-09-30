import re
import streamlit as st  # Importing required libraries
from transformers import AutoModel, AutoTokenizer
import io
import logging
from PIL import Image

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# Helper function for logging and displaying errors
def handle_error(error_message):
    logging.error(error_message)
    st.error(f"An error occurred: {error_message}")

# Cache the model and tokenizer to avoid reloading on every run
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained('srimanth-d/GOT_CPU', trust_remote_code=True)
    model = AutoModel.from_pretrained("srimanth-d/GOT_CPU", trust_remote_code=True, low_cpu_mem_usage=True, use_safetensors=True, pad_token_id=151643)
    model.eval()
    return model, tokenizer

# OCR function using the cached model
def extract_text(image_bytes):
    try:
        # Load the cached model and tokenizer
        model, tokenizer = load_model()

        # Open the image from bytes in memory and convert to PNG for the model
        image = Image.open(io.BytesIO(image_bytes))
        image.save("temp_image.png", format="PNG")

        # Extract text using the cached model
        res = model.chat(tokenizer, "temp_image.png", ocr_type='ocr')
        return res

    except Exception as e:
        handle_error(f"Error during OCR extraction: {str(e)}")
        return None

# Function to search for the keyword in the extracted text and highlight it in red
def search_keyword(extracted_text, keyword):
    # Using regex for case-insensitive and whole-word matching
    keyword = re.escape(keyword)  # Escape any special characters in the keyword
    regex_pattern = rf'\b({keyword})\b'  # Match the whole word

    # Count occurrences
    occurrences = len(re.findall(regex_pattern, extracted_text, flags=re.IGNORECASE))

    # Highlight the keyword in red using HTML
    highlighted_text = re.sub(regex_pattern, r"<span style='color:red'><b>\1</b></span>", extracted_text, flags=re.IGNORECASE)

    return highlighted_text, occurrences

# Cache the image and OCR results
@st.cache_data
def cache_image_ocr(image_bytes):
    return extract_text(image_bytes)

# Main function for setting up the Streamlit app
def app():
    st.set_page_config(
        page_title="OCR Tool",
        layout="wide",
        page_icon=":chart_with_upwards_trend:"
    )
    
    st.header("Optical Character Recognition for English and Hindi Texts")
    st.write("Upload an image below for OCR:")

    # Initialize session state to store extracted text
    if 'extracted_text' not in st.session_state:
        st.session_state.extracted_text = None

    # Create a two-column layout
    col1, col2 = st.columns([1, 1])  # Equal width columns

    with col1:
        st.subheader("Upload and OCR Extraction")
        # File uploader with exception handling
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"], accept_multiple_files=False)
        
        if uploaded_file is not None:
            # Displaying uploaded image
            st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

            # Convert uploaded file to bytes
            image_bytes = uploaded_file.read()

            # Use cache to store the OCR results
            if st.session_state.extracted_text is None:
                with st.spinner("Extracting the text..."):
                    # Cache the OCR result
                    extracted_text = cache_image_ocr(image_bytes)

                    if extracted_text:
                        st.success("Text extraction completed!", icon="🎉")
                        
                        # Store the extracted text in session state so it doesn't re-run
                        st.session_state.extracted_text = extracted_text
                        
                        st.write("Extracted Text:")
                        st.write(extracted_text)

                    else:
                        st.error("Failed to extract text. Please try with a different image.")

            else:
                # If text is already in session state, just display it
                st.write("Extracted Text:")
                st.write(st.session_state.extracted_text)

        else:
            # Clear extracted text when the image is removed
            st.session_state.extracted_text = None
            st.info("Please upload an image file to proceed.")

    # Keyword search functionality (only after text is extracted)
    with col2:
        st.subheader("Keyword Search")
        
        if st.session_state.extracted_text:
            keyword = st.text_input("Enter keyword to search")

            if keyword:
                with st.spinner(f"Searching for '{keyword}'..."):
                    highlighted_text, occurrences = search_keyword(st.session_state.extracted_text, keyword)

                    if occurrences > 0:
                        st.success(f"Found {occurrences} occurrences of the keyword '{keyword}'!")
                        # Display the text with red-colored highlights
                        st.markdown(highlighted_text, unsafe_allow_html=True)
                    else:
                        st.warning(f"No occurrences of the keyword '{keyword}' were found.")
        else:
            st.info("Please upload an image and extract text first.")

# Main function to launch the app
def main():
    try:
        app()
    except Exception as main_error:
        handle_error(f"Unexpected error in the main function: {str(main_error)}")

if __name__ == "__main__":
    main()
