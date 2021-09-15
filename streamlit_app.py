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
        spec = importlib.util.spec_from_file_location("_", f"{PATH_TO_PAGES}{page}")
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        dict_pages[foo.title] = foo.run
    return dict_pages

dict_pages = import_pages(PATH_TO_PAGES)
page = st.sidebar.radio(
    'App Navigation', 
    dict_pages.keys(), 
    )

dict_pages[page]()