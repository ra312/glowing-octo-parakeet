import base64
import streamlit as st


def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = (
        f'<iframe src="data:application/pdf;base64,{base64_pdf}" '
        'width="700" height="1000" type="application/pdf"></iframe>'
    )

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


if __name__ == "__main__":
    displayPDF(file="pages/phd.award.pdf")
