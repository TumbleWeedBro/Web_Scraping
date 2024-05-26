from bs4 import BeautifulSoup
import streamlit as st
import requests

page_to_scrape = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll('small', attrs={"class": "author"})

#genereate the page
st.title("Quotes to Scrape Teekay style")
st.markdown("This is a demo of whats to come lmao")

#output data
for quote, author in zip(quotes, authors):
    st.text_area(author.text, quote.text)
