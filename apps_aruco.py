# libaries
import streamlit as st

# vars
plant = 'plant.png'

# main page
st.set_page_config(page_title='Plant-Since-AruCo', page_icon = plant, layout = 'wide', initial_sidebar_state = 'auto')
st.title('yuval chemke web-app')

# side bar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] . div:first-child{
        width: 350px
    }
    
    [data-testid="stSidebar"][aria-expanded="false"] . div:first-child{
        width: 350px
        margin-left: -350px
    }    
    </style>
    
    """,
    unsafe_allow_html=True,


)

st.sidebar.title('Work Flow')
st.sidebar.subheader('Upload an image with an AruCu on it  https://chev.me/arucogen/')

# add dropdown to select pages on left
app_mode = st.sidebar.selectbox('Dictionary',
                                  ['4X4', '5X5', '6X6', '7X7'])

st.sidebar.markdown('---') # adds a devider (a line)

# choosing a k value (either with +- or with a slider)
  st.sidebar.number_input('Marker ID (number of clusters):', value=4, min_value = 1) # asks for input from the user
  st.sidebar.markdown('---') # adds a devider (a line)
