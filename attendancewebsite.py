import streamlit as st
import smtplib
from gsheetsdb import connect
import requests
from PIL import Image
from streamlit_player import st_player, _SUPPORTED_EVENTS
import hydralit_components as hc
import streamlit.components.v1 as components


st.set_page_config(
     page_title="SaeeAM IBM Batch Attendance",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="collapsed",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

menu_data = [
    {'id':'Metting','icon': "fas fa-archive", 'label':"Metting"},
    {'id':'Projects','icon':"fas fa-project-diagram",'label':"Projects"},
    {'id':'Doing','icon': "fas fa-stop-circle", 'label':"Learn"},
    {'id':'TeamWork','icon': "fas fa-angle-right", 'label':"Team Work"},
    {'id':'Resource','icon': "fas fa-angle-right", 'label':"Resources"},
]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='SaeeAM Classes',
    login_name='Social Media',
    hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)

def datafetch(a, b, c):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
    st.markdown(c)
  with col2:
    st.markdown(b)

def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)



def txt1(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(f'{b}')
  with col3:
    st.markdown(c)
      
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(f'{c}')
    st.components.v1.iframe(c, scrolling=True)

def txt5(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(f'{b}')
  with col3:
    st_player(c, height=200, key=b)
    
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
attendance = SaeeAM_query(f'SELECT * FROM "{sheet_url}"')

database_url = "https://docs.google.com/spreadsheets/d/1rbpLQycntZzSAyTraFm6-Nvh0kzg95xbWCWF_mBvX6k/edit?usp=sharing"
Database = SaeeAM_query(f'SELECT * FROM "{database_url}"')

def datacheck(Database, email):
    for row in Database:
        if row.Email == email:
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
  with st.form("Attadance Form", clear_on_submit=True):
      email = st.text_input(label="", placeholder="Enter Email Here")
      submitted = st.form_submit_button("Submit")
      if submitted:
          check= datacheck(attendance, email)
          st.markdown(check)
          st.success('Done')
          st.balloons()


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

if menu_id == "SaeeAM Classes":
    st.write('''
  # SaeeAM Classes, IBM Batch 2022-2024.
  ''')

    st.markdown('## Summary', unsafe_allow_html=True)
    for summary in Database:
        if summary[0] !=None:
            st.info(summary[0])

    st.markdown('''
  ## Education
  ''')
    for edu in Database:
    
        if edu[1] != None:
            datafetch(edu[1],edu[3], edu[2])               
    

        
if menu_id == "Metting":
  for metting in Database:
    with st.container():
      if metting[4] != None:
        txt1(metting[4], metting[5],metting[6])
        st.markdown("***")
       
if menu_id == "Projects":
  for projects in Database:
    if projects[3] != None:
      txt5(projects[7],projects[8], projects[9])
      st.markdown("***")
  
    
if menu_id == "TeamWork":
  for teamwork in Database:
    with st.container():
      if teamwork[13] != None:
        txt1(teamwork[13],teamwork[14],teamwork[15])
        st.markdown("***")
    
if menu_id == "Doing":
  for doing in Database:
    with st.container():
      if doing[10] != None:
        txt5(doing[10],doing[11],doing[12])
        st.markdown("***")
    

    
if menu_id == "Social Media":
  for link in Database:
    
    if link[16] != None:
      txt(link[16],link[17])
      st.markdown("***")
  
if menu_id == "Resource":
  for resource in Database:
    
    if resource[18] != None:
      txt4(resource[18],resource[19],resource[20])
      st.markdown("***")
