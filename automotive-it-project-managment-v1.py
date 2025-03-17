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

# Placeholder for user-defined template entries
if "template_data" not in st.session_state:
    st.session_state.template_data = pd.DataFrame()

# Dashboard Page
if page == "Dashboard":
    st.title("📊 IT Project Management Dashboard")
    st.write("This dashboard provides an overview of ongoing tasks and IT responsibilities.")

    # Display task table
    st.subheader("📌 Current Tasks")
    st.dataframe(tasks_df, use_container_width=True)

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
        template_columns = ["Task", "Priority", "Status", "Owner", "Due Date"]
    elif template_type == "Punch List":
        template_columns = ["Task", "Status", "Owner"]
    elif template_type == "Checklist":
        template_columns = ["Checklist Item", "Completed"]

    # Store the template
    if st.session_state.template_data.empty:
        st.session_state.template_data = pd.DataFrame(columns=template_columns)

    # User inputs for adding to template
    st.subheader("➕ Add New Entry")
    new_task = st.text_input("Task Name / Checklist Item")
    new_status = st.selectbox("Status", ["Pending", "In Progress", "Completed"])
    new_owner = st.text_input("Assigned To")

    if st.button("Add to Template"):
        new_entry = {"Task": new_task, "Status": new_status, "Owner": new_owner}
        if template_type == "Checklist":
            new_entry = {"Checklist Item": new_task, "Completed": False}
        elif template_type == "Task Management":
            new_entry["Priority"] = "Medium"
            new_entry["Due Date"] = "TBD"

        st.session_state.template_data = st.session_state.template_data.append(new_entry, ignore_index=True)
        st.success("Entry added to template!")

    # Display updated template
    st.subheader("🔹 Generated Template")
    st.dataframe(st.session_state.template_data)

    # Download updated template as CSV
    csv = st.session_state.template_data.to_csv(index=False).encode('utf-8')
    st.download_button(label="📥 Download Template", data=csv, file_name="project_template.csv", mime="text/csv")
