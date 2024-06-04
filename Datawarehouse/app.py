import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt 
# Load data
tickets_df = pd.read_csv('ticket.csv')
groups_df = pd.read_csv('groups.csv')
actions_df = pd.read_csv('action.csv')
incidents_df = pd.read_csv('incident.csv')
employees_df = pd.read_csv('employees_final.csv')
employees_group_df = pd.read_csv('employee_group.csv')

# Ticket Overview
st.title('Ticket Overview')

# Distribution of ticket types
ticket_type_counts = tickets_df['TICKET_TYPE'].value_counts()
st.subheader('Distribution of Ticket Types')
st.bar_chart(ticket_type_counts)

# Trend of ticket creation over time
tickets_df['CREATION_DATE'] = pd.to_datetime(tickets_df['CREATION_DATE'])
tickets_df['Date'] = tickets_df['CREATION_DATE'].dt.date
ticket_creation_trend = tickets_df.groupby('Date').size().reset_index(name='Count')
st.subheader('Trend of Ticket Creation Over Time')
st.line_chart(ticket_creation_trend.set_index('Date'))

# Distribution of tickets by status
ticket_status_counts = incidents_df['STATUS'].value_counts()
st.subheader('Distribution of Tickets by Status')
st.plotly_chart(px.pie(names=ticket_status_counts.index, values=ticket_status_counts.values, title='Ticket Status Distribution'))

# # Heatmap showing peak hours/days of ticket creation
# tickets_df['Hour'] = tickets_df['CREATION_DATE'].dt.hour
# tickets_df['Day'] = tickets_df['CREATION_DATE'].dt.day_name()
# ticket_heatmap = tickets_df.groupby(['Day', 'Hour']).size().unstack(fill_value=0)
# st.subheader('Heatmap of Ticket Creation')
# st.heatmap(ticket_heatmap)

# Group Performance
st.title('Group Performance')

# Number of tickets handled by each group
group_ticket_counts = tickets_df['Group_ID'].value_counts()
st.subheader('Number of Tickets Handled by Each Group')
st.bar_chart(group_ticket_counts)

# Distribution of ticket types within each group
group_ticket_type_counts = tickets_df.groupby('Group_ID')['TICKET_TYPE'].value_counts().unstack(fill_value=0)
st.subheader('Distribution of Ticket Types Within Each Group')
st.bar_chart(group_ticket_type_counts)

# Action Analysis
st.title('Action Analysis')

# Distribution of action completion times
fig, ax = plt.subplots()
ax.hist(actions_df['TIME_USED_TO_COMPLETE_ACTION (minutes)'], bins=20)
ax.set_xlabel('Completion Time (minutes)')
ax.set_ylabel('Frequency')
st.pyplot(fig)


# Incident Analysis
st.title('Incident Analysis')

# Distribution of incident statuses
incident_status_counts = incidents_df['STATUS'].value_counts()
st.subheader('Distribution of Incident Statuses')
status_pie_chart = px.pie(names=incident_status_counts.index, values=incident_status_counts.values, title='Incident Status Distribution')
st.plotly_chart(status_pie_chart)



# Employee Performance
st.title('Employee Performance')

# Workload per employee
employee_ticket_counts = tickets_df['BENEF_ID'].value_counts()
st.subheader('Workload Per Employee')
st.bar_chart(employee_ticket_counts)

# Employee efficiency
employee_efficiency = tickets_df.groupby('BENEF_ID').size() / employees_df.shape[0]
st.subheader('Employee Efficiency')
st.bar_chart(employee_efficiency)

# Additional KPIs
st.title('Additional KPIs')

# Add your KPI calculations here

# Ticket Management KPIs

average_resolution_time = tickets_df['Resolution Time (Minutes)'].mean()
average_delay_resolution = tickets_df['Delay resolution (Days)'].mean()
ticket_backlog = tickets_df[tickets_df['STATUS'] == 'Open'].shape[0]

# Action Management KPIs
average_action_completion_time = actions_df['TIME_USED_TO_COMPLETE_ACTION (minutes)'].mean()
average_delay_action_completion = actions_df['Delay action (minutes)'].mean()

# Incident Management KPIs
average_incident_resolution_time = incidents_df['MAX_RESOLUTION_DATE'].mean()
average_delay_incident_resolution = incidents_df['Delay resolution (Days)'].mean()

# Streamlit Dashboard
st.title('Streamlit Dashboard')

# Display Ticket Overview
st.subheader('Ticket Overview')

# Distribution of ticket types
ticket_type_counts = tickets_df['TICKET_TYPE'].value_counts()
st.subheader('Distribution of Ticket Types')
st.bar_chart(ticket_type_counts)

# Trend of ticket creation over time
tickets_df['CREATION_DATE'] = pd.to_datetime(tickets_df['CREATION_DATE'])
tickets_df['Date'] = tickets_df['CREATION_DATE'].dt.date
ticket_creation_trend = tickets_df.groupby('Date').size().reset_index(name='Count')
st.subheader('Trend of Ticket Creation Over Time')
st.line_chart(ticket_creation_trend.set_index('Date'))

# Group Performance
st.title('Group Performance')

# Number of tickets handled by each group
group_ticket_counts = tickets_df['Group_ID'].value_counts()
st.subheader('Number of Tickets Handled by Each Group')
st.bar_chart(group_ticket_counts)

# Distribution of ticket types within each group
group_ticket_type_counts = tickets_df.groupby('Group_ID')['TICKET_TYPE'].value_counts().unstack(fill_value=0)
st.subheader('Distribution of Ticket Types Within Each Group')
st.bar_chart(group_ticket_type_counts)

# Action Analysis
st.title('Action Analysis')

# Distribution of action completion times using Matplotlib histogram
fig, ax = plt.subplots()
ax.hist(actions_df['TIME_USED_TO_COMPLETE_ACTION (minutes)'], bins=20)
ax.set_xlabel('Completion Time (minutes)')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Incident Analysis
st.title('Incident Analysis')

# Distribution of incident statuses
st.subheader('Distribution of Incident Statuses')
incident_status_counts = incidents_df['STATUS'].value_counts()
status_pie_chart = px.pie(names=incident_status_counts.index, values=incident_status_counts.values, title='Incident Status Distribution')
st.plotly_chart(status_pie_chart)

# Employee Performance
st.title('Employee Performance')

# Workload per employee
st.subheader('Workload Per Employee')
employee_ticket_counts = tickets_df['BENEF_ID'].value_counts()
st.bar_chart(employee_ticket_counts)

# Additional KPIs
st.title('Additional KPIs')
# Display other KPIs
