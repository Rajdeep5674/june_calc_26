import streamlit as st

st.title("🧮 Simple Calculator")

operator = st.selectbox(
    "Choose an operation:",
    ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
)

# ---------------- ADDITION ----------------

if operator == "Addition (+)":

    values = st.text_input(
        "Enter values separated by comma:",
        placeholder="Example: 10,20,30,40"
    )

    if st.button("Calculate Sum"):

        try:
            values = values.strip().split(',')

            new_list = [float(vals) for vals in values]

            result = sum(new_list)

            st.success(f"Sum of all the given values: {result}")

        except ValueError:
            st.error("Please enter valid numeric values.")


# ---------------- SUBTRACTION ----------------

elif operator == "Subtraction (-)":

    num1 = st.number_input("Enter first value:", value=0.0)

    num2 = st.number_input("Enter second value:", value=0.0)

    if st.button("Calculate Subtraction"):

        st.success(f"{num1} - {num2} = {num1 - num2}")

        st.info(f"{num2} - {num1} = {num2 - num1}")


# ---------------- MULTIPLICATION ----------------

elif operator == "Multiplication (*)":

    values = st.text_input(
        "Enter values separated by comma:",
        placeholder="Example: 2,5,10"
    )

    if st.button("Calculate Multiplication"):

        try:
            values = values.strip().split(',')

            new_list = [float(vals) for vals in values]

            result = 1

            for val in new_list:
                result = result * val

            st.success(
                f"Multiplication of all the given values: {result}"
            )

        except ValueError:
            st.error("Please enter valid numeric values.")


# ---------------- DIVISION ----------------

elif operator == "Division (/)":

    num1 = st.number_input(
        "Enter first value:",
        value=0.0,
        key="division_num1"
    )

    num2 = st.number_input(
        "Enter second value:",
        value=0.0,
        key="division_num2"
    )

    if st.button("Calculate Division"):

        if num2 != 0:

            result = num1 / num2

            st.success(
                f"{num1} / {num2} = {result}"
            )

        else:

            st.error("You cannot divide by zero.")


st.divider()

st.caption("Simple Calculator using Python and Streamlit")