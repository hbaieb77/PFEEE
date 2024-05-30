import streamlit as st
import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv('Matrice Incident (1) (1).csv' , sep=";")
pd.set_option('display.max_columns', None)
df.drop(columns=['Unnamed: 20'] , inplace=True)# Sample data
group_columns = ['Groupe 1', 'Groupe 2', 'Groupe 3', 'Groupe 4']

# df= df[(df['Groupe 1']=='AMI SIEGE')==False]

# Function to generate Sankey diagram for a specific Code appli
def generate_sankey(code_appli):
    # Filter data for the selected Code appli
    df_selected = df[df['Code appli'] == code_appli]
    
    # Initialize transitions
    transitions = []
    
    # Extract transitions for the selected Code appli
    for _, row in df_selected.iterrows():
        previous_group = None
        for group in group_columns:
            current_group = row[group]
            if pd.notna(current_group):
                if previous_group is not None:
                    transitions.append((previous_group, current_group))
                previous_group = current_group
    
    # Create a mapping of groups to indices
    all_groups = pd.unique(df_selected[group_columns].values.ravel('K'))
    all_groups = all_groups[pd.notna(all_groups)]
    group_indices = {group: i for i, group in enumerate(all_groups)}
    
    # Extract source, target, and value for the Sankey diagram
    source = [group_indices[src] for src, tgt in transitions]
    target = [group_indices[tgt] for src, tgt in transitions]
    value = [transitions.count((src, tgt)) for src, tgt in transitions]
    
    # Create the Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=list(group_indices.keys()),
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
        ))])
    
    fig.update_layout(title_text=f"Incident Management Group Relationships for Code appli: {code_appli}",
                      font_size=10)
    
    st.plotly_chart(fig)

# Load your DataFrame
# df_qlik_buo = pd.read_csv('your_data.csv')

# Create a dropdown menu for selecting Code appli
code_applis = df['Code appli'].unique().tolist()
selected_code_appli = st.selectbox('Select Code appli', code_applis)

# Display the Sankey diagram for the selected Code appli
generate_sankey(selected_code_appli)

import plotly.express as px


df_selected = df[df['Code appli'] == selected_code_appli]


df_melted = df_selected.melt(id_vars=['Code appli'], value_vars=['Groupe 1', 'Groupe 2', 'Groupe 3', 'Groupe 4'],
                             var_name='Group Type', value_name='Group')

# Remove rows where 'Group' is NaN
df_melted = df_melted.dropna(subset=['Group'])

# Aggregate the data
agg_data = df_melted.groupby(['Group Type', 'Group']).size().reset_index(name='Count')

# Create an interactive grouped bar chart using Plotly Express
bar_fig = px.bar(agg_data, x='Group', y='Count', color='Group Type', barmode='group',
                 title=f'Relationship between Groups and Incidents for {selected_code_appli}',
                 labels={'Group': 'Group', 'Count': 'Count of Incidents', 'Group Type': 'Group Type'})

bar_fig.update_layout(xaxis={'categoryorder':'total descending'})

# Display the bar chart
st.plotly_chart(bar_fig)




st.write("Réponse column values for the selected Code appli:")
st.table(df_selected[['Nom CI','Question','Code question','Réponse']])


