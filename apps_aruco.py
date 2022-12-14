# libaries
# import libs
import requests
import streamlit as st
import numpy as np
# import cv2
import skimage.io as io
# from skimage import io, filters, feature
# import matplotlib.pyplot as plt

# vars
plant = 'plant.png'

# main page
st.set_page_config(page_title='Plant-Since-AruCo', page_icon = plant, layout = 'wide', initial_sidebar_state = 'auto')
st.title('yuval chemke web-app')

# side bar

st.sidebar.markdown('---') # adds a devider (a line)

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
iid = st.sidebar.number_input('Marker ID', value=4, min_value = 1) # asks for input from the user

st.sidebar.markdown('---') # adds a devider (a line)

# choosing a k value (either with +- or with a slider)
size = st.sidebar.number_input('Marker size, mm', value=100, min_value = 1) # asks for input from the user
st.sidebar.markdown('---') # adds a devider (a line)



# read an image from the user
img_file_buffer = st.sidebar.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])
   
# assign the uplodaed image from the buffer, by reading it in
if img_file_buffer is not None:
    image = io.imread(img_file_buffer)
else: # if no image was uploaded, then segment the demo image
    demo_image = 'tomato.jpg'
    image = io.imread(demo_image)

 # Display the result on the right (main frame)
st.subheader('Image')
st.image(image)


def arocu(image, dictionary, iid, size):
    # Aruco Area
    aruco_area = cv2.contourArea (corners[0])
  
    if dictionary == '4X4':
        a = 4*4
    if dictionary == '5X5':
        a = 5*5
    if dictionary == '6X6':
        a = 6*6
    if dictionary == '7X7':
        a = 7*7

    # Pixel to cm ratio
    pixel_cm_ratio = a / aruco_area # since the AruCo is 5*5 cm, so we devide 25 cm*cm by the number of pixels
    print('Ratio - Each pixel is',pixel_cm_ratio, 'cm*cm')
