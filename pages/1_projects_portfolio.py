import streamlit as st

title = 'Projects portfolio'
index = 1

def run():
    st.title('Selected projects')
    st.write('A full list can be found on my [Malt profile](https://www.malt.fr/profile/bastiencarniel)')
    st.write('')

    st.subheader('Natural Language Processing')

    st.write('**Fully-customized specialized search engine for biomedical research | 2021 | Science Feedback **')
    st.write('*BioBert (HuggingFace implementation), ElasticSearch (deployed on AWS), Streamlit*')
    st.write('- Using the PubMeb API, collection of the abstract, title and metadata of 2.3 million research articles, 20 million keywords, 30 million authors.')
    st.write('- Reprocessing : researchers & affiliation disambiguation, connecting with other data sources (s.a. journals quality databases), text cleaning...')
    st.write('- Embedding of keywords using BioBert to create a vector search space.')
    st.write('- Deployment of an ElasticSearch database on AWS to index the keywords.')
    st.write('- Ad-hoc scoring system to identify the most relevant specialist for any biomedical topic (taking into account publication history, publication quality, first-author status, citations...)')

    st.write('** Automatic monitoring of a subreddit discussion board | 2021 | RaiseIn **')
    st.write('*Spacy, FastAPI (deployed on AWS), Bubble*')
    st.write('- In the wake of the GameStop situation, automatic monitoring of financial asset mentions and sentiment on the r/wallstreebets discussion board (100k messages per hour at its peak)')
    st.write("- Module for ingestion and preprocessing of subreddit data via the site's API")
    st.write("- NLP Module for Named Entity Recognition (identification of assets discussed) and sentiment analysis using Spacy")
    st.write("- Dashboard module built on Bubble displaying insights from the modules above")
    st.write("- All the above deployed on AWS virtual machines (EC2 and LightSail) using Docker, interfaced using FastAPI, using a PostgreSQL database hosted on AWS RDS")
    st.write('-----')

    st.subheader('Tabular data modeling')

    st.write('** Prediction of the occurrence of a disease | 2021 | Sanofi-Pasteur **')
    st.write('*Scikit-Learn, Streamlit*')
    st.write('- Epidemiological data collection')
    st.write('- Development of a regression model to predict the DALYs of a disease based on epidemiological parameters (R-sq. of .965).')
    st.write("- Deployment of a Streamlit-based webapp for non-technical users to be able to make predictions.")

    st.write('** Sports game results predictions | 2019-Ongoing | Personal project **')
    st.write('*Scikit-Learn, Tensorflow, Catboost, Matplotlib, Seaborn, Aimhub*')
    st.write("- Prediction of the results of sports games (football and tennis). High-sensitivity system in which a 0.3 percentage point change in accuracy tips a strategy into positive or negative territory.")
    st.write("- In-depth experiments with feature engineering, data cleaning, custom loss functions, hyperparameter tuning")
    st.write("- Over 10,000 model runs (ML/DL) tracked through Aimhub, development of custom dashboard and metrics")
    st.write('-----')

    st.subheader('Data infrastructure')

    st.write('** Automated sports betting system | 2019-Ongoing | Personal project **')
    st.write('*async, MollybetAPI*')
    st.write("- Development and deployment of an automated sports betting system (football and tennis)")
    st.write("- Extremely strong production constraints linked to the volume and the in-game nature of the bets placed : 99.99% uptime, 99.5% errorless data, 2-second system refresh intervals.")
    st.write("- Live consolidation of data from different sources.")
    st.write("- Weekly : 4,000+ games monitored, 6 million+ data points collected, 2,000 bets placed")

    st.subheader('Scraping')

    st.write('** Scraping of a mobile application | 2021 | JB Consulting **')
    st.write('*MITM, Android Virtual Studio, APK-MITM*')
    st.write("- Reverse engineering of an Android mobile app API")
    st.write("- Proxy rotations to circumvent rate limiting")
    st.write("- 10,000 daily API calls in under 10 minutes")

    st.write('** Sports odds scraping | 2021 | Personal project **')
    st.write('*Selenium*')
    st.write("- Parallel scraping of odds data for 500,000 football and tennis games (20 data points per game)")
    st.write("- IP rotations to circumvent rate limiting")
    st.write('-----')
