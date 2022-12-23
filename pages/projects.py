"""Projects page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Projects - :male-construction-worker: ")
    st.markdown(
            """### 
**Amazing Project Tech Stack]**
- item 1
- item 2

### Academic Projects [(GitHub)](www.github.com)

**The NonCommutative Analysis [Hopg Algebras, Spectral Triples]**
- Used operator algebras formalism to obtain analytical results 

""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    write()
