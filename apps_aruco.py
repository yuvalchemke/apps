# libaries
import streamlit as st
from skimage import measure, io, img_as_ubyte, morphology, util, color
import matplotlib.pyplot as plt
from skimage.color import label2rgb, rgb2gray
import numpy as np
import pandas as pd
import cv2
import imutils

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
st.sidebar.subheader('fdsfsfsdf')

# add dropdown to select pages on left
app_mode = st.sidebar.selectbox('Dictionary',
                                  ['4X4', '5X5', '6X6', '7X7])
