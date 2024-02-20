import streamlit as st

import displacement
import velocity
import acceleration
import energy
def main():
    st.title("Physics App")
    st.write(
        "Welcome to the Amazing World Of PHYSICS.")

    st.header("HARMONIC OSCILLATOR")
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
