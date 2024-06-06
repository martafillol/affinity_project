import streamlit as st

def creative_demo_page(prompt, response):
    st.title("Creative Demo Page")
    st.write("This page shows the generated image based on the user's input.")

    # Display the prompt
    st.write(f"Prompt: {prompt}")

    # Display the generated image
    if response.data and response.data[0] and response.data[0].url:
        image_url = response.data[0].url
        st.image(image_url, caption="Generated Image", use_column_width=True)
    else:
        st.write("No image was generated.")

    # Add a button to navigate back to the main page
    if st.button("Go Back to Main Page", key='back_to_main_demo'):
        st.session_state.page = 'main'
        st.experimental_rerun()
