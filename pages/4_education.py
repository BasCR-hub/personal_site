import streamlit as st

title = 'Education & Certificates'
index = 4

def run():
    st.title('Education')

    st.header('Coding-related ')

    st.subheader('[Microsoft Azure](https://docs.microsoft.com/en-us/learn/certifications/exams/dp-100) | DP-100: Data Scientist Associate | 2021 | [Badge](https://www.youracclaim.com/badges/db9746f4-fe53-4652-a0c8-c8a08707772d/public_url)')
    with st.expander('More information'):
        st.write("""Training and deploying a ML/DL model on MS Azure""")
    st.text("")

    st.subheader('[Microsoft AI School by Simplon](https://simplon.co/formation/ecole-ia-microsoft/23#competences) | Data & AI Developer | 2020')
    with st.expander('More information'):
        st.write("""The Microsoft AI School and Simplon run an amazing initiative : a conscious effort is made to create
        highly dynamic socially-, ethnically- and gender-diverse cohorts. Apart from motivation to learn, there are no academic prerequisites.""")
        st.write("""The hands-on curriculum starts with an intensive 9-month full-time instruction period covering the whole range of the data/AI spectrum,
        starting from Python basics going all the way up to the training of custom Transformer models. It is followed by a year-long internship.
        """)
        st.write("""I started taking up freelance missions at the end of the instruction period so unfortunately never met the internship requirements 
        and did not graduate !""")
    st.text("")

    st.subheader('[DeepLearning.ai](https://www.deeplearning.ai/program/natural-language-processing-specialization/) | NLP Specialization | 2020 | [Badge](https://www.coursera.org/account/accomplishments/specialization/KAS9KMPRZKF2)')
    with st.expander('More information'):
        st.write("""Andrew Ng's DeepLearning.ai's flagship course on Natural Language Processing, covering the full range of NLP algorithms (starting with simple Bag of Words
        and ending with Attention models). 
        """)
    st.text("")

    st.subheader('[EdX](https://github.com/MicrosoftLearning/Dev290x) | Computer Vision and Image Analysis | 2020 | [Badge](https://courses.edx.org/certificates/26246df66fd74a50b43241885635542c)')
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    st.header("Less directly relevant degrees which nonetheless deserve a mention given how much time was spent earning them")
    
    st.subheader('[HEC Paris](https://www.hec.edu/en/overview) | Msc in Management | 2012-2015 ')
    st.text("")
    st.subheader('[Saint Petersburg State University](https://gsom.spbu.ru/en/about-gsom/) | Msc in International Business | 2014-2015')
    st.text("")
    st.subheader('[McGill University](https://www.mcgill.ca/desautels/about) | Bachelor in Finance | 2007-2010')

        



    





