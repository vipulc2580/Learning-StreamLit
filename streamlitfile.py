import streamlit as fg
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff
# fg.title('File handling in StreamLit')
# fileselected=fg.file_uploader('Get csv file ',type=['csv'])
# # fg.write(fileselected.name) 
# if fileselected is not None:
#     # if(fileselected.name.split('.')[1]=='csv'):
#     df=pd.read_csv(fileselected)
#     fg.dataframe(df.head())

# # loading a file
# # filepath=r"G:\Python\geekssforgeeksPython\JupyterProjects\survey_results_public.csv"
# # data=pd.read_csv(filepath)
# # fg.table(data.head())
# fg.write('Dealing with images')
# imgpath=fg.file_uploader('Get image url ',type=['png',
#                                                 'jpeg'])
# if(imgpath is not None):
#     fg.image(imgpath)
# # fg.image('C:\Users\vipul\OneDrive\Pictures\pes poster.png')
# audio_filepath=fg.file_uploader("Get audio ",type=['mp3'])
# if audio_filepath is not None:
#     fg.audio(audio_filepath.read())

chart_data=pd.DataFrame(np.random.randn(20,3),columns=['line-1','line-2','line-3'])
fg.line_chart(chart_data)
fg.area_chart(chart_data)
fg.bar_chart(chart_data)

fg.header('Plotting Using Matplotlib')
data=pd.read_csv('./filldata.csv')
fg.dataframe(data.head())
age=data['Age']
dev=data['All_Devs']
plt.plot(age,dev,label='Median Salary')
plt.title('Median Salary of Developers')
plt.xlabel('Age')
plt.ylabel('Salary in USD')
fg.pyplot(plt.gcf())

fg.header('Multiple Column figure')
col1,col2=fg.columns(2)
with col1:
    col1.header="Graph 1"
    fig1,ax1=plt.subplots()
    ax1.plot(data['Age'],data['Python'],label='Python Dev')
    ax1.legend()
    ax1.set_title('Median Salary Of Python Developer')
    ax1.set_xlabel('Age')
    ax1.set_ylabel('Salary in USD')
    fg.pyplot(fig1)
with col1:
    col1.header="Graph 1"
    fig2,ax2=plt.subplots()
    ax2.plot(data['Age'],data['JavaScript'],label='JavaScript Dev')
    ax2.legend()
    ax2.set_title('Median Salary Of JavaScript Developer')
    ax2.set_xlabel('Age')
    ax2.set_ylabel('Salary in USD')
    fg.pyplot(fig2)

data3 = [np.random.normal(0, std, 100) for std in range(1, 5)]

# Create the violin plot
fig3,ax3=plt.subplots()
ax3.violinplot(data, showmeans=True, showmedians=True)

# Add labels and title
ax3.set_xticks([1, 2, 3, 4], ['Group 1', 'Group 2', 'Group 3', 'Group 4'])
ax3.set_title('Violin Plot Example')
ax3.set_ylabel('Values')
fg.pyplot(fig3)

fg.header('Plotting using Altair Scatter Plot Module')
data4=pd.DataFrame(np.random.randn(500,5),columns=['a','b','c','d','e'])
chart=alt.Chart(data4,).mark_circle().encode(x='a',y='b',size='c',tooltip=['a','b','c','d','e'])
fg.altair_chart(chart)

fg.subheader('Interactive Line Chart')
option=data.columns.to_list()[1:]
choice=fg.selectbox('Choose Category of Graph : ',option)
if choice is not None:
    gf,ay=plt.subplots()
    ay.plot(age,data[choice],label=choice)
    ay.legend()
    ay.set_title(f'Median Salary Of {choice}')
    ay.set_xlabel('Age')
    ay.set_ylabel('Salary in USD')
    fg.pyplot(gf)
choices=fg.multiselect('Select Multiple Option : ',option)
if choices is not None:
    new_data=data.loc[:,choices]
    # fg.dataframe(new_data.head(10))
    fg.line_chart(new_data)

fg.header('Data Visualization with Plotly')
fg.subheader('Histogram plot using Plotly')
d1=np.random.rand(200)
d2=np.random.rand(200)
d3=np.random.rand(200)
hist_data=[d1,d2,d3]
group_label=['Group-1','Group-2','Group-3']
fig=ff.create_distplot(hist_data,group_labels=group_label,bin_size=[.1,.25,.5])
fg.plotly_chart(fig)
