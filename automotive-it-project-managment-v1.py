import streamlit as st
import pandas as pd

# Configure Streamlit page layout
st.set_page_config(page_title="IT Project Management", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Punch List", "Checklist", "Project Management Template"])

# Sample Data for Tasks
tasks = [
    {"Task": "Help Desk Support", "Priority": "High", "Status": "In Progress", "Owner": "IT Tech", "Due Date": "Daily"},
    {"Task": "Network Monitoring", "Priority": "Medium", "Status": "Ongoing", "Owner": "IT Team", "Due Date": "Weekly"},
    {"Task": "Website Maintenance", "Priority": "Medium", "Status": "Scheduled", "Owner": "IT Tech", "Due Date": "Monthly"},
    {"Task": "ERP System Support", "Priority": "High", "Status": "As Needed", "Owner": "IT Manager", "Due Date": "Ad-hoc"},
    {"Task": "Hardware Procurement", "Priority": "Low", "Status": "Pending", "Owner": "Finance", "Due Date": "Quarterly"}
]
tasks_df = pd.DataFrame(tasks)

# Dashboard Page
if page == "Dashboard":
    st.title("📊 IT Project Management Dashboard")
    st.write("This dashboard provides an overview of ongoing tasks and IT responsibilities.")

    # Display task table
    st.subheader("📌 Current Tasks")
    st.dataframe(tasks_df, use_container_width=True)

    # IT Budget Overview
    st.subheader("💰 IT Budget & Procurement")
    budget_data = pd.DataFrame([
        {"Item": "Laptops", "Category": "Hardware", "Cost": "$5,000", "Approval Status": "Approved", "Next Purchase": "09/01/2025"},
        {"Item": "SQL Server License", "Category": "Software", "Cost": "$2,500", "Approval Status": "Pending", "Next Purchase": "04/15/2025"}
    ])
    st.dataframe(budget_data)

# Punch List Page
elif page == "Punch List":
    st.title("📝 Punch List – Track Pending & Completed Items")

    # Punch list management
    st.subheader("Add a New Punch List Item")
    task = st.text_input("Task Name")
    status = st.selectbox("Status", ["Pending", "In Progress", "Completed"])
    owner = st.text_input("Assigned To")
    
    if st.button("Add Task"):
        new_task = {"Task": task, "Status": status, "Owner": owner}
        tasks.append(new_task)
        st.success("Task added successfully!")

    # Display punch list
    st.subheader("📌 Punch List Tasks")
    punch_list_df = pd.DataFrame(tasks)
    st.dataframe(punch_list_df)

# Checklist Page
elif page == "Checklist":
    st.title("✅ IT Checklist – Step-by-Step Guide")

    st.subheader("System Maintenance Checklist")
    checks = {
        "Firewall Security Patch Applied": False,
        "Daily Server Backup Verified": False,
        "Review User Access Control": False,
        "Update Antivirus Definitions": False,
        "Check System Logs for Errors": False
    }

    # Create interactive checklist
    for item in checks.keys():
        checks[item] = st.checkbox(item, value=checks[item])

    if st.button("Submit Checklist"):
        st.success("Checklist submitted successfully!")

# Project Management Template Page
elif page == "Project Management Template":
    st.title("📂 Create a Project Management Template")
    st.write("Use this tool to generate a blank template for new projects.")

    # User selects which component to use as a template
    template_type = st.selectbox("Select a Template Type", ["Task Management", "Punch List", "Checklist"])

    if template_type == "Task Management":
        template_df = pd.DataFrame(columns=["Task", "Priority", "Status", "Owner", "Due Date"])
    elif template_type == "Punch List":
        template_df = pd.DataFrame(columns=["Task", "Status", "Owner"])
    elif template_type == "Checklist":
        template_df = pd.DataFrame(columns=["Checklist Item", "Completed"])

    # Display blank template
    st.subheader("🔹 Generated Template")
    st.dataframe(template_df)

    # Download template as CSV
    csv = template_df.to_csv(index=False).encode('utf-8')
    st.download_button(label="📥 Download Template", data=csv, file_name="project_template.csv", mime="text/csv")
