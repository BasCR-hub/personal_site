import os
import streamlit as st
import numpy as np
import importlib.util
import os
import importlib
import sys 

PATH_TO_PAGES = './pages/'

def import_pages(PATH_TO_PAGES):
    '''Import all .py pages from the PATH_TO_PAGES directory
    Pages' content must be wrapped in a function named run. Title must be stored in a variable named title. 
    Use any page in the pages folder as template.
    '''
    pages_paths = [page for page in os.listdir(path = PATH_TO_PAGES) if page[-3:]=='.py']
    dict_pages= {}
    for page in pages_paths:
        spec = importlib.util.spec_from_file_location(name="",location=f"{PATH_TO_PAGES}{page}")
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        dict_pages[foo.title] = [foo.index,foo.run]
    return dict_pages

dict_pages = import_pages(PATH_TO_PAGES)

st.sidebar.title("Bastien Carniel's CV")
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
page = st.sidebar.radio('',[elem[0] for elem in sorted(dict_pages.items(), key=lambda item: item[1][0])],index=0)
dict_pages[page][1]()
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.title("About this mini-site")
st.sidebar.info("This 100% Python mini-app was built and hosted using the amazing [Streamlit](https://streamlit.io) toolkit.")
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('''Think we could work together ? Please get in touch on [**LinkedIn**](https://www.linkedin.com/in/bastien-carniel-243690b9/), by [**email**](mailto:carnielb@gmail.com), or on [**Malt**](https://www.malt.fr/profile/bastiencarniel).''')


