import streamlit as st

# @st.cache_data #cache data within app to reuse the same data again
# Main Streamlit app code
def main():
    # AUDIDENCE_TPYE = st.selectbox('AUDIDENCE_TYPE', ['Beginner', 'Intermediate', 'Expert'])
    STRUCTURE_TPYES = ['Thematic', 'Problem-Solution', 'Chronological', 'Cause-Effect']
    NARRATIVE_TPYES = ['Factual', 'Persuasive', 'Anecdotal', 'Descriptive']

    AUDIDENCE_TPYE = st.selectbox('AUDIDENCE_TYPE', ['Beginner', 'Intermediate', 'Expert'])

    if AUDIDENCE_TPYE == 'Beginner':
        STRUCTURE_TPYE = ['Thematic', 'Problem-Solution']
        # NARRATIVE_TPYE = ['Descriptive']
        # return ['Descriptive']
    elif AUDIDENCE_TPYE == 'Intermediate':
        STRUCTURE_TPYE = ['Problem-Solution', 'Chronological']
        # NARRATIVE_TPYE = ['Persuasive']
        # return ['Factual']
    elif AUDIDENCE_TPYE == 'Expert':
        STRUCTURE_TPYE = ['Chronological', 'Cause-Effect']
        # NARRATIVE_TPYE = ['Persuasive']
        # return ['Persuasive']
    else:
        STRUCTURE_TPYE = []

    STRUCTURE_TPYE = st.selectbox('STRUCTURE TYPE', STRUCTURE_TPYE)

    if STRUCTURE_TPYE == 'Thematic':
        NARRATIVE_TPYE = 'Descriptive'
    elif STRUCTURE_TPYE == 'Problem-Solution':
        NARRATIVE_TPYE = 'Factual'
    elif STRUCTURE_TPYE == 'Chronological':
        NARRATIVE_TPYE = 'Persuasive'
    elif STRUCTURE_TPYE == 'Cause-Effect':
        NARRATIVE_TPYE = 'Anecdotal'
    else:
        NARRATIVE_TPYE = []

    # st.write(f"NARRATIVE TYPE IS:   {NARRATIVE_TPYE}")
    st.code(f"AUDIENCE_TPYES = {AUDIDENCE_TPYE}")
    st.code(f"STRUCTURE_TPYES = {STRUCTURE_TPYE}")
    st.code(f"NARRATIVE_TPYES = {NARRATIVE_TPYE}")

uploaded_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image')

if __name__ == '__main__':
    main()
