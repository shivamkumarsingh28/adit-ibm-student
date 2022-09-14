import streamlit as st
import smtplib
from gsheetsdb import connect
import requests
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(
     page_title="SaeeAM IBM Batch Attendance",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )
conn = connect()

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def SaeeAM_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = "https://docs.google.com/spreadsheets/d/1HfViq19h-Kb04P0WEyLBZi04ApcfCq3JBZUWN_Ajeh8/edit?usp=sharing"
Database = SaeeAM_query(f'SELECT * FROM "{sheet_url}"')

def datacheck(Database, name, email):
    for row in Database:
        st.write(name)
        if row.Email == email or row.Name == name:
            return row.Url
        
# col1, col2, col3 = st.columns(3)

# with col1:
#     if st.button('SaeeAM Whatsapp', key="whatsapp"):
#         webbrowser.open_new_tab('https://chat.whatsapp.com/KvqQTGzvYp405hofDsHyuO') 
# with col2:
#     if st.button('SaeeAM Business', key="business"):
#         webbrowser.open_new_tab('https://g.page/r/CR93AGLEpeP_EAE') 
# with col3:
#     if st.button('SaeeAM Telegram', key="telegram"):
#         webbrowser.open_new_tab('https://t.me/+4Wwajk1RorA0OTE9')


with st.sidebar:
  with st.form("Have Any Query", clear_on_submit=True):
            name= st.text_input(label="Name",value="", placeholder="Enter Name Here", type="default", key="name")
            email =st.text_input(label="Email",value="", placeholder="Enter Email Here", type="default", key="email")
            number= st.text_input(label="Number",value="", max_chars=10, placeholder="Enter Number Here", type="default", key="number")
            message= st.text_area(label="Message",value="", max_chars=1000, placeholder="Enter Number Here", key="message")

            submitted = st.form_submit_button("Hire")
          
            
            if submitted:
                conn= smtplib.SMTP('smtp.gmail.com', 587)
                conn.starttls()
                conn.login('startupsaeeam@gmail.com','qckkfvequfvzxrnl')
                sendmsg= ("SaeeAM ----" +name+" "+email+" "+number+" "+message)
                conn.sendmail('startupsaeeam@gmail.com', [email.split(","), 'startupsaeeam@gmail.com'], sendmsg)
                conn.quit()
                st.success('Done')
                st.balloons()
                
cont1 = st.container()

cont1col1, cont1col2= cont1.columns([3,2])


with cont1col1:


    st.subheader("""SaeeAM IBM ADIT BATCH- 2022-2024""")
    st.write("Indian Collage Student Batch")
    options = st.multiselect(
     'Select Services How May I Help You',
     ['computer science','SaeeAM Team', 'Javascripts', 'HTML', 'CSS','Python', 'Cloud Computing','More & More'],['computer science','SaeeAM Team', 'Javascripts', 'HTML', 'CSS','Python', 'Cloud Computing','More & More'])

    st.code(options)
with cont1col2:
    youths =  "https://assets4.lottiefiles.com/packages/lf20_ljotbiif.json"
    lottie_json_youth = load_lottieurl(youths)

    st_lottie(lottie_json_youth)
        

                
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Fill Data For Ibm Adit STudent Attendance")
with col2:
    email = st.text_input(label="", placeholder="Enter Email Here", key="ibmname")
with col3:
    name = st.text_input(label="", placeholder="Enter Name Here")
    

# print(type(name))
check= datacheck(Database, name, email)
print(check)
st.write(check)