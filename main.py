import os.path

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Setting the page configuration

st.set_page_config(
    page_title= 'Data Visualizer',
    layout= 'centered',
    page_icon= '📊'
)

# Title

st.title('📊 Data Visualizer')
working_directory = os.path.dirname(os.path.abspath(__file__))

folder_path = f"{working_directory}/data"

files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
selected_file = st.selectbox("Select the file ",files, index=None)

if selected_file:
    file_path = os.path.join(folder_path, selected_file)

    df = pd.read_csv(file_path)

    col1, col2 = st.columns(2)
    columns = df.columns.tolist()

    with col1:
        st.write("")
        st.write(df.head())

    with col2:
        x_axis = st.selectbox("Select X-axis", options=columns + ['None'])
        y_axis = st.selectbox("Select Y-axis", options=columns + ['None'])

        plot_list = ['Line Plot', 'Bar Chart','Scatter Plot', 'Distribution Plot','Count Plot']
        plot_type = st.selectbox('Select the type of Plot ', options = plot_list)

        if st.button('Generate Plot'):

            fig, ax = plt.subplots(figsize = (6,4))

            if plot_type == 'Line Plot':
                sns.lineplot(x = df[x_axis], y = df[y_axis], ax= ax)

            elif plot_type == 'Bar Chart':
                sns.barplot(x = df[x_axis], y = df[y_axis], ax= ax)

            elif plot_type == 'Scatter Plot':
                sns.scatterplot(x = df[x_axis], y = df[y_axis], ax= ax)

            elif plot_type == 'Distribution Plot':
                sns.histplot(df[x_axis],kde = True, ax= ax)
                y_axis = 'Density'

            elif plot_type == 'Count Plot':
                sns.countplot(x = df[x_axis], ax = ax)
                y_axis = 'Count'

            ax.tick_params(axis='x', labelsize=10)
            ax.tick_params(axis='y', labelsize=10)

            plt.title(f'{plot_type} of {y_axis} vs {x_axis}', fontsize=12)
            plt.xlabel(x_axis, fontsize = 10)
            plt.ylabel(y_axis, fontsize=10)

            st.pyplot(fig)


