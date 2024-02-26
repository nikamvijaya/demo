import streamlit as st

import displacement
import velocity
import acceleration
import energy

st.header(":rainbow[PHYSICS IS EVERYWHERE]:sunglasses:")
def main():


    st.write( '''It doesn't matter how beautiful your theory is it doesn't matter how smart you are If it doesn't agree with experiment, it's wrong.''')

    st.header("HARMONIC OSCILLATOR")
    col1, col2 , col3 = st.columns(3)
    with col1:
        if st.button("spring oscilaton"):
            st.image('vivek.gif', caption='spring oscilaton')
    with col2:
        if st.button("coupled oscilation"):
            st.image('vivek2.gif', caption='coupled oscilaton')
    with col3:
        if st.button("vivek"):
            st.image('IMG-20240222-WA0013.jpg', caption='vivu')
        
    selected_topic = st.selectbox("Choose a topic", ["displacement", "velocity", "acceleration", "energy"])
    if selected_topic == "displacement":
        displacement.main()
    elif selected_topic == "velocity":
        velocity.main()
    elif selected_topic == "acceleration":
        acceleration.main()
    elif selected_topic == "energy":
        energy.main()

main()
if __name__ == "_main_":
    main()    
