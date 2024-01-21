import streamlit as st
from pages import inference_page, base_models_page, meta_model_page

def main():
    st.sidebar.title("Navigation")

    # Create a sidebar with page options
    page_options = ["Inference", "Meta model monitoring", "Base models monitoring" ]
    selected_page = st.sidebar.radio("Select Page", page_options)

    # Render the selected page
    if selected_page == "Inference":
        inference_page.show()
    elif selected_page == "Meta model monitoring":
        meta_model_page.show()
    elif selected_page == "Base models monitoring":
        base_models_page.show()

if __name__ == "__main__":
    main()
