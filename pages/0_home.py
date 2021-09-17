import streamlit as st

title = 'Home'
index = 0

def run():
    _,col1,_ = st.columns(3)
    with col1:
        st.image('./resources/photo.jpeg')

    st.title("Hi, I'm Bastien. I do data science & AI")
    st.write("*which is why this website isn't very pretty.*")
    st.write('')
    st.write('')

    st.header('How can I help?')
    st.write(" I have two specialties :") 
    st.write(' - **Natural Language Processing**,')
    st.write(' - Building **start-to-finish MVPs** for any data-centered project : collection and processing of raw data --> model training --> deployment of a fully-integrated webapp. All the while leveraging all existing resources (free cloud provider credits, open-source tools, data scraping) to lower the complexity, budget and time-to-completion.')

    st.write("""In terms of sectors, I'm particularly happy to contribute to projects in the public policy, environment or finance spheres.""")
    st.write('Beyond Python, I can work in English or French. A если вы говорите медленно, на русском - тоже возможно !')

    st.header("A few words about me")
    st.write('I am a former strategy & public policy consultant and start-up COO who turned data & AI developer in 2019.')
    st.write('I am based in Paris, although I also spend significant time in Southern France and Armenia.')

    st.subheader('''Think we could work together ? Please get in touch on [**LinkedIn**](https://www.linkedin.com/in/bastien-carniel-243690b9/), by [**email**](mailto:carnielb@gmail.com), or on [**Malt**](https://www.malt.fr/profile/bastiencarniel).''')
