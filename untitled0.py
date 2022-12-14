# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OKbKJfCI4BvWADoxhzu7ghuMfQyXDInG
"""

# libaries
import streamlit as st

# vars
plant = 'plant.png'     # Symnol
DEMO_IMAGE = 'tomato.jpg' # a demo image for the segmentation page, if none is uploaded

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

# Dictionary
dictionary = st.sidebar.selectbox('Dictionary',
                                  ['4X4', '5X5', '6X6', '7X7'])

st.sidebar.markdown('---') # adds a devider (a line)

# Marker ID
id = st.sidebar.number_input('Marker ID', value=4, min_value = 1) # asks for input from the user

st.sidebar.markdown('---') # adds a devider (a line)

# Marker size, mm
st.sidebar.number_input('Marker size, mm', value=100, min_value = 1) # asks for input from the user
st.sidebar.markdown('---') # adds a devider (a line)













    # read an image from the user
img_file_buffer = st.sidebar.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])
   
   # assign the uplodaed image from the buffer, by reading it in
if img_file_buffer is not None:
    image = io.imread(img_file_buffer)
else: # if no image was uploaded, then segment the demo image
    demo_image = DEMO_IMAGE
    image = io.imread(demo_image)

    # display on the sidebar the uploaded image
st.sidebar.text('Original Image')
st.sidebar.image(image)



!pip install opencv-contrib-python

# import libs
from skimage import measure, io, img_as_ubyte, morphology, util, color
import matplotlib.pyplot as plt
from skimage.color import label2rgb, rgb2gray
import numpy as np
import pandas as pd
import cv2
import imutils

def arocu(image, dictionary, id, size):
# Aruco Area
  aruco_area = cv2.contourArea (corners[0])

  # Pixel to cm ratio
  pixel_cm_ratio = dictionary / aruco_area # since the AruCo is 5*5 cm, so we devide 25 cm*cm by the number of pixels
  print('Ratio - Each pixel is',pixel_cm_ratio, 'cm*cm')
