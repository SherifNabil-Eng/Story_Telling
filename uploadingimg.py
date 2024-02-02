import streamlit as st
import brain as br

IMAGE=bytearray("", 'ascii')


## instantiate the brain class
## get the image text , translate it and get the translated text
  
def buttoncallback():
    
              
    if IMAGE == bytearray("", 'ascii'):
        st.session_state.Original_text = "Please upload an image !"
        st.session_state.English_text = "Please upload an image !"
    else:
        brain_handle = br.Brain(IMAGE)
        #print ("brain_handle is ",brain_handle)
        brain_handle.getimgtext()
        #print ("after brain_handle")
 

        brain_handle.gettranslatedtext()
       # testing the getimgtext function
        imgtext =brain_handle.originallanguage
        #print ("original text is ",imgtext)

        ##### testing 

        brain_handle.texttospeechfn()
        brain_handle.outputfile()
        st.session_state.Original_text = brain_handle.originaltext
        st.session_state.English_text = brain_handle.translatedtext

    return

title = st.container()
##"st.session_state objecct ", st.session_state
if "Original_text" not in st.session_state:
    st.session_state ['Original_text'] = "Original text goes here:) "
if "English_text" not in st.session_state:
    st.session_state ['English_text'] = "Defualt English text :)"

with title:
    st.title('Story telling Test')
    st.write('This is a test for uploading files to a streamlit app')


page_content = st.container()
    
with page_content:
    sections = st.columns(2)
    with sections[0]:
        st.header('Upload Image')
        uploaded_file = st.file_uploader("Choose a file")

            
        if uploaded_file is not None:
            if uploaded_file.name.endswith('.jpg') or uploaded_file.name.endswith('.png'):
                st.image(uploaded_file)
                IMAGE=uploaded_file.getvalue()
            else:
                st.write('please upload a valid file type, we can accept only .jpg, .png')
                st.session_state.Original_text = "Please upload a valid image type !"
                st.session_state.English_text = "Please upload a valid image type !"

        
        else:
            st.write('uploaded file will be displayed here')
            
        
        
    with sections[1]:
        st.text_area('Original text',key="Original_text")
        st.text_area('English text',key="English_text")
        st.button('translate',on_click=buttoncallback)
        