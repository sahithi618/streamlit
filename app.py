import streamlit as st
from datetime import datetime 

st.title('Hello, Sahithi!')
st.header("Welcome!")
st.subheader("GFG")
st.text("welcome to geeksforgeeks")

st.markdown("# Hi")
st.markdown("## Hi")
st.markdown("### Hi")
st.markdown("Hi")

st.markdown('**GFG** is an ed-tech') ##makes it bold
st.markdown('__GFG__ is an ed-tech')
st.markdown('*GFG* is an ed-tech') ## makes it itlaic
st.markdown('_GFG_ is an ed-tech')
st.markdown('***GFG*** is an ed-tech')## bold+itlaic
st.markdown('___GFG___ is an ed-tech')

st.markdown('- First point')

st.success("Data is submitted!")
st.info("Information!")
st.warning("A warning!")
st.error("Error!?")
st.exception(ZeroDivisionError('Div not possible'))
st.help(ZeroDivisionError)
st.write("1+2+3")
st.write(1+2+3)

st.code('x=10\n'
'for i in range(x):\n'
'\tprint(i)')

st.checkbox('Male')
st.checkbox("Female")

if(st.checkbox("Adult")):
    st.write("You are an adult")

radioButton=st.radio('Select:',('Male','Female','Other'),horizontal=True)
st.write("You are",radioButton)

st.subheader('Select Box')
select_box=st.selectbox("Data Science:",['Data analysis','Web scraping','Machine learning','Deep learning','NLP','Image processing'])
st.write("You have selected:",select_box)

st.subheader("Multi Selectbox")
multiselbox=st.multiselect("Data Science:",['Data analysis','Web scraping','Machine learning','Deep learning','NLP','Image processing'])
st.write("You have selected:",len(multiselbox),"courses")

st.subheader("Button")
if (st.button("Click me")):
    st.write("Thanks for clicking")

st.subheader('Colour Picker')
st.color_picker('Pick your favourite colour')

st.subheader("Slider")
vol=st.slider("Select the volume",0,100,step=1)
st.write("Volume is:",vol)

st.subheader("Text Input")
name=st.text_input("Name:")

if (name):
    st.write('Hi ',name,'!')
username=st.text_input("Username:")
password=st.text_input("Password:",type='password')

st.subheader("Text Area")
st.text_area("Write something about yourself",height=200,max_chars=500,help='Maximum 500 characters are allowed')

st.subheader("Number input")
st.number_input("Select your age",18,100)

st.subheader("Date input")
today=datetime.now().date()
st.date_input("Date",value=today,min_value=today,max_value=today.replace(year=today.year+1))

st.subheader("Time input")
st.time_input("Time")

st.subheader("BMI Calculator")
with st.form(key='BMI Calculator'):
    col1,col2,col3=st.columns([2,2,1])
with col1:
    weight=st.number_input('Enter your weight in kgs')
with col2:
    height=st.number_input('Enter your height in meters')
with col3:
    submit=st.form_submit_button('Calculate')

if submit:
    BMI=round(weight/(height**2),2)
    if BMI<=18.5:
        st.error("Underweight")
    elif BMI>18.5 and BMI<=24.9:
        st.success("Healthy/Normal")
    elif BMI>25 and BMI<=29.9:
        st.warning("Overweight")
    else:
        st.error("Obese")