import streamlit as st
from functions.file_reader import read_file

def main():
    if  "file_object" not in st.session_state:
        st.session_state.file_object = None

    st.set_page_config(
        page_title="Data Cleaner",
        page_icon=":lower_left_paintbrush:",
        layout="wide"
    )

    st.header("Data Cleaner: :lower_left_paintbrush:")
    st.subheader("Your CSV/XLSX documents")

    st.session_state["file_object"] = st.file_uploader(
        "Upload single file",
        accept_multiple_files=False,
        type=["csv", "xlsx"]
    )

    if st.session_state["file_object"] is not None:
        with st.spinner("Processing Your File"):
            df = read_file(file_object=st.session_state["file_object"])
            st.write(df.head())

if __name__=="__main__":
    main()