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
    ast.write_page(PAGES["About"])


if __name__ == "__main__":
    main()
