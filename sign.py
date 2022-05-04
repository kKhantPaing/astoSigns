import streamlit as st
import pyaztro

#signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']

def zoidc():
    try:
        sign = st.text_input("Zodic Sign: ").lower()
        zodicSign = pyaztro.Aztro(sign = sign)
        st.write(f"Sign: {zodicSign.sign.capitalize()}\n")
        st.write(f"Desctiption:\n {zodicSign.description}\n")
        st.write(f"You will be {zodicSign.mood.capitalize()} today.")
        #print(f"Your Lucky Color is {zodicSign.color}.")
        #print(f"Your Lucky Partner is {zodicSign.compatibility}.")
        #print(f"Your Lucky Time is {zodicSign.lucky_time}.")
        #print(f"Your Lucky Number is {zodicSign.lucky_number}.\n")
    except:
        print("No Found!")
zoidc()
