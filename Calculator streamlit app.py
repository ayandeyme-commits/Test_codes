import streamlit as st

st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Simple Calculator")
st.write("Select an operation and enter the required values.")

operator = st.selectbox(
    "Select Operation",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (*)",
        "Division (/)"
    ]
)

# -----------------------------
# ADDITION
# -----------------------------
if operator == "Addition (+)":

    values = st.text_input(
        "Enter values separated by comma",
        placeholder="Example: 10,20,30,40"
    )

    if st.button("Calculate Addition"):

        if values:

            try:
                splitted_vals = values.split(",")

                val_list = [
                    float(val.strip())
                    for val in splitted_vals
                ]

                result = sum(val_list)

                st.success(
                    f"Addition of all given values = {result}"
                )

            except ValueError:
                st.error("Please enter valid numbers.")

        else:
            st.warning("Please enter some values.")


# -----------------------------
# SUBTRACTION
# -----------------------------
elif operator == "Subtraction (-)":

    num1 = st.number_input(
        "Enter first number",
        value=0.0
    )

    num2 = st.number_input(
        "Enter second number",
        value=0.0
    )

    if st.button("Calculate Subtraction"):

        result1 = num1 - num2
        result2 = num2 - num1

        st.success(f"{num1} - {num2} = {result1}")
        st.info(f"{num2} - {num1} = {result2}")


# -----------------------------
# MULTIPLICATION
# -----------------------------
elif operator == "Multiplication (*)":

    values = st.text_input(
        "Enter values separated by comma",
        placeholder="Example: 2,5,10"
    )

    if st.button("Calculate Multiplication"):

        if values:

            try:

                splitted_vals = values.split(",")

                val_list = [
                    float(val.strip())
                    for val in splitted_vals
                ]

                result = 1

                for i in val_list:
                    result = result * i

                st.success(
                    f"Multiplication of all given values = {result}"
                )

            except ValueError:
                st.error("Please enter valid numbers.")

        else:
            st.warning("Please enter some values.")


# -----------------------------
# DIVISION
# -----------------------------
elif operator == "Division (/)":

    num1 = st.number_input(
        "Enter first number",
        value=0.0,
        key="division_num1"
    )

    num2 = st.number_input(
        "Enter second number",
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

            st.error(
                "You cannot divide by zero. Please try again."
            )


st.divider()

st.caption("Simple Calculator using Python + Streamlit")

