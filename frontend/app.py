import streamlit as st # type: ignore
from streamlit_lottie import st_lottie # type: ignore
import requests # type: ignore

# Load a lottie animation from a URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Define a function for the financial management app
def financial_management_app():
    st.title("Financial Management System 💰")

    # Load Lottie animations
    lottie_party = load_lottie_url("https://assets8.lottiefiles.com/packages/lf20_lk80fpsm.json")  # Party popper animation

    # Input fields for income
    st.header("💵 Income")
    salary = st.number_input("Enter your Salary:", min_value=0.0, value=0.0, step=100.0)

    # Input fields for expenses
    st.header("🧾 Expenses")
    rent = st.number_input("Rent:", min_value=0.0, value=0.0, step=10.0)
    utilities = st.number_input("Utilities:", min_value=0.0, value=0.0, step=10.0)
    groceries = st.number_input("Groceries:", min_value=0.0, value=0.0, step=10.0)
    transportation = st.number_input("Transportation:", min_value=0.0, value=0.0, step=10.0)
    entertainment = st.number_input("Entertainment:", min_value=0.0, value=0.0, step=10.0)

    # Calculate total expenses
    total_expenses = rent + utilities + groceries + transportation + entertainment
    st.write(f"Total Expenses: **Rs. {total_expenses}**")

    # Input fields for savings
    st.header("💼 Savings")
    emergency_fund = st.number_input("Emergency Fund:", min_value=0.0, value=0.0, step=100.0)
    retirement_savings = st.number_input("Retirement Savings:", min_value=0.0, value=0.0, step=100.0)
    investments = st.number_input("Investments:", min_value=0.0, value=0.0, step=100.0)

    # Calculate total savings
    total_savings = emergency_fund + retirement_savings + investments
    st.write(f"Total Savings: **Rs. {total_savings}**")

    # Calculate balance (Income - Expenses)
    balance = salary - total_expenses
    st.write(f"Remaining Balance (Income - Expenses): **Rs. {balance}**")

    # Show a summary of financial details
    st.header("📊 Summary")
    if st.button("Show Summary"):
        st.write(f"**Income:** Rs. {salary}")
        st.write(f"**Total Expenses:** Rs. {total_expenses}")
        st.write(f"**Total Savings:** Rs. {total_savings}")
        st.write(f"**Remaining Balance:** Rs. {balance}")
        
        if balance > 0:
            st.success("🎉 You're saving money! Well done! 💸")
            st_lottie(lottie_party, height=200, key="party")
        elif balance == 0:
            st.warning("⚖️ You're breaking even. No savings, but no loss either!")
        else:
            st.error("❌ You're overspending! Try reducing your expenses.")

    # Fun message at the end
    st.markdown("### Keep up with your financial goals and make saving a fun habit! 🚀")

# Call the function to run the app
if __name__ == "__main__":
    financial_management_app()
