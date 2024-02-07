import streamlit as st
from pages import inference_page

def main():
    st.sidebar.title("Navigation")

    # Create a sidebar with page options
    page_options = ["Inference", ]
    selected_page = st.sidebar.radio("Select Page", page_options)

    # Render the selected page
    if selected_page == "Inference":
        inference_page.show()

if __name__ == "__main__":
    main()
