import streamlit as st

import displacement
import velocity
import acceleration
import energy

st.header(":rainbow[PHYSICS IS EVERYWHERE]:sunglasses:")
def main():


    st.write( '''It doesn't matter how beautiful your theory is it doesn't matter how smart you are If it doesn't agree with experiment, it's wrong.''')

    st.header("HARMONIC OSCILLATOR")
    col1, col2  = st.columns(2)
    with col1:
        if st.button("spring oscilaton"):
            st.image('vivek.gif', caption='spring oscilaton')
    with col2:
        if st.button("coupled oscilation"):
            st.image('vivek2.gif', caption='coupled oscilaton')
        
    selected_topic = st.selectbox("Choose a topic", ["displacement", "velocity", "acceleration", "energy"])
    if selected_topic == "displacement":
        displacement.main()
    elif selected_topic == "velocity":
        velocity.main()
    elif selected_topic == "acceleration":
        acceleration.main()
    elif selected_topic == "energy":
        energy.main()
    import random

print("Guess the Number!")
number_to_guess = random.randint(1, 100)
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number_to_guess:
        print("Congratulations! You guessed the number!")
        break
    elif guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


main()
if __name__ == "_main_":
    main()    
