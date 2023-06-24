import streamlit as st

# @st.cache_data #cache data within app to reuse the same data again
# Main Streamlit app code
def main():
    AUDIDENCE_TPYE = st.selectbox('AUDIDENCE_TYPE', ['Beginner', 'Intermediate', 'Expert'])
    STRUCTURE_TPYES = ['Thematic', 'Problem-Solution', 'Chronological', 'Cause-Effect']
    NARRATIVE_TPYES = ['Factual', 'Persuasive', 'Anecdotal', 'Descriptive']
    if AUDIDENCE_TPYE == 'Beginner':
        STRUCTURE_TPYE = ['Thematic', 'Problem-Solution']
        # return ['Descriptive']
    elif AUDIDENCE_TPYE == 'Intermediate':
        STRUCTURE_TPYE = ['Problem-Solution', 'Chronological']
        # return ['Factual']
    elif AUDIDENCE_TPYE == 'Expert':
        STRUCTURE_TPYE = ['Chronological', 'Cause-Effect']
        # return ['Persuasive']
    else:
        STRUCTURE_TPYE = []

    STRUCTURE_TPYE = st.selectbox('STRUCTURE TYPE', STRUCTURE_TPYE)

    if STRUCTURE_TPYE == 'Thematic':
        return ['Descriptive']
    elif STRUCTURE_TPYE == 'Problem-Solution':
        NARRATIVE_TPYE = ['Factual']
    elif STRUCTURE_TPYE == 'Chronological':
        NARRATIVE_TPYE = ['Persuasive']
    elif STRUCTURE_TPYE == 'Cause-Effect':
        NARRATIVE_TPYE = ['Anecdotal']
    else:
        NARRATIVE_TPYE = []

    st.write(f"NARRATIVE TYPE IS:   {NARRATIVE_TPYE}")

if __name__ == '__main__':
    main()
