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
st.sidebar.number_input('Marker ID', value=4, min_value = 1) # asks for input from the user

st.sidebar.markdown('---') # adds a devider (a line)

# choosing a k value (either with +- or with a slider)
st.sidebar.number_input('Marker size, mm', value=100, min_value = 1) # asks for input from the user
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

# call the function to segment the image
	# Load Aruco detector
	parameters = cv2.aruco.DetectorParameters_create()
	aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
	
	# Get Aruco marker
	corners, _, _ = cv2.aruco.detectMarkers(image, aruco_dict, parameters=parameters)
	
	# Draw polygon around the marker
	int_corners = np.int0(corners)
	cv2.polylines(image, int_corners, True, (0, 255, 0), 50)
	#plt.imshow(image)
	
	# Aruco Area
	aruco_area = cv2.contourArea (corners[0])
	# Pixel to cm ratio
	pixel_cm_ratio = 4*4 / aruco_area# since the AruCo is 4*4 cm, so we devide 16 cm*cm by the number of pixels
	
# segment using kmeans
image =io.imread(f'{folder_path}/images/tomato.jpg')
k=3
attempts=10
segmented_kmeans, labels, centers = segment_image_kmeans(image, k, attempts)
#plt.imshow(segmented_kmeans)

# lets get the index of the leafs row 

for i,center in enumerate(centers):
  if np.all(center == ([133,165,26])):
    leaf_center_index = i
    #print(leaf_center_index)
	
# copy source img
img = image.copy()
masked_image = img.copy()

# convert to the shape of a vector of pixel values (like suits for kmeans)
masked_image = masked_image.reshape((-1, 3))

index_to_remove = leaf_center_index

# color (i.e cluster) to exclude
list_of_cluster_numbers_to_exclude = list(range(k)) # create a list that has the number from 0 to k-1
list_of_cluster_numbers_to_exclude.remove(index_to_remove) # remove the cluster of leaf that we want to keep, and not black out
for cluster in list_of_cluster_numbers_to_exclude:
  masked_image[labels== cluster] = [0, 0, 0] # black all clusters except cluster leaf_center_index

# convert back to original shape
masked_image = masked_image.reshape(img.shape)
masked_image_grayscale = rgb2gray(masked_image)

# show the image
color_map=input()
plt.imshow(masked_image_grayscale, cmap=color_map)
plt.colorbar()

# count how many pixels are in the foreground and bg
leaf_count = np.sum(np.array(masked_image_grayscale) >0)
bg_count = np.sum(np.array(masked_image_grayscale) ==0)

print('Leaf px count:', leaf_count, 'px')
print('Area:', leaf_count*pixel_cm_ratio, 'cm\N{SUPERSCRIPT TWO},', 'which is:',  f'{0.0001*leaf_count*pixel_cm_ratio:.3f}', 'm\N{SUPERSCRIPT TWO}')
