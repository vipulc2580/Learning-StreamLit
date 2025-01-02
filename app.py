import streamlit as fg
import json
fg.title('Welcome Geeks To GeeksForGeeks')
fg.header('The header tag')
fg.subheader('The subheader tag')
fg.text('Text tag')
fg.markdown('# Hi')
fg.markdown('## Hi')
fg.markdown('### Hi')
fg.markdown('#### Hi')


fg.success('Success')
fg.info('Information')
fg.warning('Warning')
fg.error('error')
fg.exception(ZeroDivisionError('Division is not possible'))

fg.help(ZeroDivisionError)


fg.write(range(1,10))


fg.subheader('Check box')
if(fg.checkbox('Male')):
    fg.write('Male')
if(fg.checkbox('Adult')):
    fg.write('You are an adult')

fg.subheader('Radio button')
optionselected=fg.radio('Select :',('Male','Female','Other'))
if(optionselected=='Male'):
    fg.write('You are male')
elif(optionselected=='Female'):
    fg.write('You are Female')
elif(optionselected=='Other'):
    fg.write('Other is selected')

fg.subheader('Select box:')
contentselected=fg.selectbox('Choose an Language : ',['Datascience','Data Analysis','Machine learning','Java',
                                               'C++','R','Angular','Django']
                                            )
fg.write("You've selected following languages ",contentselected)

fg.subheader('Multi select box')
skillsselected=fg.multiselect('Choose Skills : ',['Data Analysis','WebDevelopement','App Developement',
                                                  'WebScraping','Blockchain','FrontEnd Engineering','BackEnd Engineering',
                                                  'Devops','Automation','Testing','Cloud','Data Visualization'])

fg.write('Skills you have : ',json.dumps(skillsselected))

fg.subheader('Button')
if(fg.button('Click me')):
    fg.write('Thanks for Clicking')

fg.subheader('Slider')
rating=fg.slider('Select your Rating',1,10,1)
fg.write("You've selected Rating : ",rating)

fg.subheader('Text Input From User')
textEntered=fg.text_input('Enter your name : ')
# fg.write('Your Name is ',textEntered)
passwprdEntered=fg.text_input('Enter password : ',type='password')


fg.subheader('Text Area')
description=fg.text_area('Describe yourself in 500 words ')
fg.write(description)

fg.subheader('Number Input')
age=fg.number_input('Enter your age : ',18,90)
# fg.write(type(age))

fg.subheader('Date Input')
dateenter=fg.date_input('select Date : ')
# fg.write(type(dateenter))

fg.subheader('Time Input')
timeenter=fg.time_input('Enter time please : ')
# fg.write(type(timeenter))
