"""Edu page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Education :books:")
    st.markdown(
            """### Imperial College London
**PhD in Mathematics | May 2019** | [**ICL**](https://www.imperial.ac.uk/)\n


**Moscow State University | June 2012** | \n
- Computer Science and Systems Programming

""",
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    write()
