# Main page for streamlit resume
import streamlit as st
import pages.about
import pages.projects
import pages.edu
import pages.pdf
import resources.ast as ast

PAGES = {
    "About": pages.about,
    "Education": pages.edu,
}


def main():
    """Main function of App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.write_page(page)


if __name__ == "__main__":
    main()
