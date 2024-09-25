import streamlit as st  #Importing required libraries
from transformers import AutoModel, AutoTokenizer
import io

def app():          #Defining the GUI using streamlit library
    st.set_page_config(
    page_title="OCR_tool",
    layout="wide",
    page_icon=":chart_with_upwards_trend:",
    )
    st.header("Optical Character Recognition for English and Hindi texts",divider="")
    st.write("Upload an image below for OCR",)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"],accept_multiple_files=False)
    print(uploaded_file._file_urls.upload_url)
    if uploaded_file is not None:
        st.success("Uploaded!",icon="🎉")
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        with st.spinner("Extracting the text..."):
            # Convert uploaded file to bytes for passing to the model
            image_bytes = uploaded_file.read()
            with open("temp_image.jpg", "wb") as f:
                f.write(image_bytes)
            extracted_text = extract_text("temp_image.jpg")
    # OCR code here
    # OCR code here
    st.success("Done!",icon="🎉")
    st.write("Extracted Text:")
    st.write(extracted_text)


def extract_text(image):        #Defining the OCR function using the SOTA(State Of The Art) GOT(General OCR Theory) model
    tokenizer = AutoTokenizer.from_pretrained('srimanth-d/GOT_CPU',trust_remote_code=True)
    model = AutoModel.from_pretrained("srimanth-d/GOT_CPU", trust_remote_code=True, low_cpu_mem_usage=True, use_safetensors=True, pad_token_id=tokenizer.eos_token_id)
    model = model.eval()
    image_file = image
    res = model.chat(tokenizer, image_file, ocr_type='ocr')
    return res


# plain texts OCR
#res = model.chat(tokenizer, image_file, ocr_type='ocr')

# format texts OCR:
# res = model.chat(tokenizer, image_file, ocr_type='format')

# fine-grained OCR:
# res = model.chat(tokenizer, image_file, ocr_type='ocr', ocr_box='')
# res = model.chat(tokenizer, image_file, ocr_type='format', ocr_box='')
# res = model.chat(tokenizer, image_file, ocr_type='ocr', ocr_color='')
# res = model.chat(tokenizer, image_file, ocr_type='format', ocr_color='')

# multi-crop OCR:
# res = model.chat_crop(tokenizer, image_file, ocr_type='ocr')
# res = model.chat_crop(tokenizer, image_file, ocr_type='format')

# render the formatted OCR results:
# res = model.chat(tokenizer, image_file, ocr_type='format', render=True, save_render_file = './demo.html')

def main():
    app()
main()