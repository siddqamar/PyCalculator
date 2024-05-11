import streamlit as st

# Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Calculator function
def calculator():
    st.title("Simple Calculator")
    st.markdown("### By Siddiqui Qamar")  # Subheading

    # Input fields for numbers
    num1 = st.number_input("Enter the first number", step=1)
    num2 = st.number_input("Enter the second number", step=1)

    # Operation selection
    operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    result = None

    # Perform operation based on user input
    if st.button("Calculate"):
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)

        # Display result
        if result is not None:
            st.success(f"Result: {result}")

# Run the calculator function
calculator()
