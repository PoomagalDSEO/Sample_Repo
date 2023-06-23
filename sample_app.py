import streamlit as st


@st.cache_data #cache data within app to reuse the same data again
def get_for_structure(AUDIDENCE_TPYES):# condition for STRUCTURE_TYPE Output
    if AUDIDENCE_TPYES == 'Beginner':
        return ['Problem-Solution']
        # return ['Descriptive']
    elif AUDIDENCE_TPYES == 'Intermediate':
        return ['Thematic']
        # return ['Factual']
    elif AUDIDENCE_TPYES == 'Expert':
        return ['Chronological']
        # return ['Persuasive']
    else:
        return []
def get_for_narrative(AUDIDENCE_TPYES):# condition for NARRATIVE_TYPE Output
    if AUDIDENCE_TPYES == 'Beginner':
        return ['Descriptive']
    elif AUDIDENCE_TPYES == 'Intermediate':
        return ['Factual']
    elif AUDIDENCE_TPYES == 'Expert':
        return ['Persuasive']
    else:
        return []

def main():
    # Add your previous condition input, e.g., a selectbox
    AUDIDENCE_TPYES = st.selectbox('AUDIDENCE_TPYES', ['Beginner', 'Intermediate', 'Expert'])
    # STRUCTURE_TPYES = st.selectbox('STRUCTURE_TPYES', ['Thematic', 'Problem-Solution', 'Chronological', 'Cause-Effect'])
    # NARRATIVE_TPYES = st.selectbox('NARRATIVE_TPYES', ['Factual', 'Persuasive', 'Anecdotal', 'Descriptive'])
    # to Call the function to get the structure and narrative type based on the option selected in audience type
    STRUCTURE_TYPE = get_for_structure(AUDIDENCE_TPYES)
    NARRATIVE_TYPE = get_for_narrative(AUDIDENCE_TPYES)

    # Show the final options in a selectbox or it can be written as final decision
    selected_option = st.selectbox('STRUCTURE_TYPE', STRUCTURE_TYPE)
    selected_option1 = st.selectbox('SNARRATIVE_TYPE', NARRATIVE_TYPE)

    # Display the selected option
    st.write('Selected Option:', selected_option)
    st.write('Selected Option:', selected_option1)
if __name__ == '__main__':
    main()
