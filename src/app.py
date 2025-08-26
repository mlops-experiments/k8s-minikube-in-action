import streamlit as st
from calculator import square, cube, fifth_power
from calculator import add, subtract, multiply, divide, power

# Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube, and fifth power.")

# Get user input
n = st.number_input("Enter an integer", value=1, step=1)

# Calculate results
square = square(n)
cube = cube(n)
fifth_power = fifth_power(n)

# Display results
st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")

print("Streamlit app is running...")
