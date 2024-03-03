import streamlit as st
from faker import Faker
import json
import random

# List of common locales and their display names
locales = [
    "",
    "en_US",
    "en_GB",
    "de_DE",
    "fr_FR",
    "es_ES",
    "it_IT",
    "ja_JP",
    "ko_KR",
    "zh_CN",
    "pt_BR",
    ["de_DE", "es_ES", "fr_FR", "it_IT", "ru_RU"],
    ["pt_BR", "es_MX"],
    ["en_US", "en_CA", "es_MX"],
    ["ja_JP", "zh_CN", "ko_KR", "th_TH"],
    ["en_AU", "en_NZ"],
    ["sw_KE"],
]
locale_names = [
    "Default",
    "United States",
    "Great Britain",
    "Germany",
    "France",
    "Spain",
    "Italy",
    "Japan",
    "Korea",
    "China",
    "Brazil",
    "Europe",
    "South America",
    "North America",
    "Asia",
    "Oceania",
    "Africa",
]

st.title("Configurable Schema Fake Data Generator")

# Locale (country) selection
selected_locale_name = st.selectbox(
    "Select Locale for Data Generation", options=locale_names, index=0
)
selected_locale = locales[locale_names.index(selected_locale_name)]


def set_locale_name():
    selected_locale_name = st.selectbox(
        "Select Locale for Data Generation", options=locale_names, index=0
    )
    selected_locale = locales[locale_names.index(selected_locale_name)]


fake = Faker(selected_locale)

# User input for the number of entries
num_entries = st.number_input("Number of Entries", min_value=1, value=1, step=1)

# Expanded set of field types
field_options = {
    "name": "Full Name",
    "first_name": "First Name",
    "last_name": "Last Name",
    "email": "Email",
    "city": "City",
    "country": "Country",
    "postcode": "Postal Code",
    "company": "Company",
    "job": "Job Title",
    "text": "Random Text",
    "phone_number": "Phone Number",
    "date_of_birth": "Date of Birth",
    "latitude": "Latitude",
    "longitude": "Longitude",
    "locale": "Locale",
    "currency_code": "Currency Code",
    "credit_card_number": "Credit Card Number",
    "ipv4": "IPv4 Address",
    "ipv6": "IPv6 Address",
    "user_name": "Username",
    "password": "Password",
    "uri": "URI",
    "image_url": "Image URL",
    "license_plate": "License Plate",
}

# Configure the schema
st.sidebar.header("Configure Schema")
num_fields = st.sidebar.number_input("Number of Fields", min_value=1, value=5, step=1)
schema = {}
for i in range(num_fields):
    field_name = st.sidebar.text_input(f"Field Name {i+1}", value=f"Field {i+1}")
    field_type = st.sidebar.selectbox(
        f"Field Type {i+1}", options=list(field_options.keys()), index=0
    )
    schema[field_name] = field_type


# Function to generate data based on the schema
def generate_data(fake, num_entries, schema):
    data_list = []
    for _ in range(num_entries):
        entry = {
            field_name: getattr(fake, field_type)()
            for field_name, field_type in schema.items()
        }
        data_list.append(entry)
    return data_list


# Generate and display fake data
if st.button("Generate Fake Data"):
    fake = Faker(selected_locale)
    fake_data = generate_data(fake, num_entries, schema)
    st.json(fake_data)
