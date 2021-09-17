import os
import importlib

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

PATH_TO_PAGES = './pages/'

dict_pages = import_pages(PATH_TO_PAGES)
print([elem[0] for elem in sorted(dict_pages.items(), key=lambda item: item[1][0])])
