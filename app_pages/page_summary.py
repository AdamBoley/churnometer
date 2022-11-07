import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargons**\n"
        f"* A **customer** is a person who uses your service or product.\n"
        f"* A **prospect** is a potential or prospective customer.\n"
        f"* A **churned** customer is a user who has stopped using your product or service.\n "
        f"* A churned customer has a metric called **tenure**, which is the number of months this person " 
        f"has used our product or service.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset represents a **customer base from a Telco company**. "
        f"Containing individual customer data on the products and services "
        f"(like internet type, online security, online backup, tech support), "
        f"account information (like contract type, payment method, monthly charges) "
        f"and profile (like gender, partner, dependents).")

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/AdamBoley/churnometer).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client wants to understand the patterns in the customer base, "
        f"so that the client can learn the most relevant variables that are correlated to a "
        f"churned customer.\n"
        f"* 2 - The client wants to be able to determine whether or not a given prospect will churn. "
        f"If so, the client wants to know when. In addition the client wants "
        f"to learn to which cluster this prospect will belong in the customer base. "
        f"Based on that, the client wants us to present potential factors that could maintain and/or bring  "
        f"the prospect to a non-churnable cluster. "
        f"That is - they want to be able to induce a customer to stay with the company long-term"
        )

        