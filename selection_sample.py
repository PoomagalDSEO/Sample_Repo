import streamlit as st
import pandas as pd
# To give title for the page
st.title('Image Prompter')

# To give header for the page
st.header('Start to Prompt here')

# To give sub-headingings
st.subheader('Going to create prompt for Avatar')

# if st.button('Create'): # to create button
df1 = pd.DataFrame({'second_col': ['Round', 'Oval-shaped', 'Cat', 'Wide-set']})
df2 = pd.DataFrame(
   {'third_col': ['Amber', 'Fair', 'Beige', 'Bronze', 'Brown', 'Caramel', 'Tan', 'Tawny', 'Walnut', 'Wheat']})
df = pd.DataFrame(
          {'first column': ['Oval', 'Round', 'Square', 'Heart-shaped', 'Diamond-shaped', 'Long or rectangular']})
Facial_Shape = st.selectbox('Facial shape', df['first column'])
Eye_Shape = st.selectbox('eye shape', df1['second_col'])
Skin_Tone = st.selectbox('Skin Tone', df2['third_col'])
'create an avatar with facial shape as', Facial_Shape, 'face with eye shape as', Eye_Shape, 'eyes with', Skin_Tone, 'skin tone'
    # else:
     # st.write('Goodbye')

