import streamlit as st
from faker import Faker

fake = Faker()

# Supported field types and corresponding Faker methods
field_types = {
    "Name": fake.name,
    "Email": fake.email,
    "Phone Number": fake.phone_number,
    "Address": fake.address,
    "Company": fake.company,
    "Date": fake.date,
    "Time": fake.time,
    "Text": fake.text,
}

st.title("Configurable Schema Fake Data Generator")

# Allow users to configure the schema
st.sidebar.header("Configure Schema")
num_fields = st.sidebar.number_input("Number of Fields", min_value=1, value=3, step=1)
schema = {}

for i in range(num_fields):
    field_name = st.sidebar.text_input(f"Field Name {i+1}", value=f"Field {i+1}")
    field_type = st.sidebar.selectbox(
        f"Field Type {i+1}", options=list(field_types.keys()), index=0
    )
    schema[field_name] = field_type

# Button to generate data
if st.button("Generate Fake Data"):
    data = {}
    for field_name, field_type in schema.items():
        # Use the selected field type to generate fake data
        data[field_name] = field_types[field_type]()

    # Display the generated data
    st.json(data)
