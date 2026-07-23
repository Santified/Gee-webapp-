import streamlit as st

st.title("Welcome to My Web App")
st.write("Thanks for visiting my web app.")

st.header("This is a sample webapp")
st.subheader("Using Streamlit for interactive dashboards")

st.header("About the app")
st.text("Hi july 31 weekend hangout! \n This is a simple web app built with streamlit.\n It allows you to create beautiful web apps in pure Python.")

st.subheader("Quick Overview")
st.markdown("### Bamifemi is a creatvedesigner \n Daniel is a verification analyst \n Tobi is not part of the hangout \n Santi is jobless is daddy have workdown for him")



# Display a simple metric
st.metric(label="Status", value="Ready", delta="Live")

st.header("Interactive Widgets")
# Interactive widgets
name = st.text_input("What is your name?", "Streamlit User")
age = st.slider("Choose your age", 0, 100, 25)
if st.button("Say hello"):
    st.success(f"Hello {name}! You are {age} years old.")


# Display a checkbox with the label 'Show/Hide'
if st.checkbox("Show/Hide"):
    # Show this text only when the checkbox is checked
    st.text("Thanks for checking the box!")



st.header("Hobby Preferences")
# Create a dropdown menu for selecting a hobby
hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Eating', 'Sports', 'Gaming', 'Singing', 'Reading', 'Traveling', 'Cooking', 'Photography', 'Painting'])

# Create a multiselect box for choosing hobbies
hobbies = st.multiselect("Select Your Hobbies:", ['Dancing', 'Eating', 'Sports', 'Gaming', 'Singing', 'Reading', 'Traveling', 'Cooking', 'Photography', 'Painting'])

# Display the number of selected hobbies
st.write("You selected", len(hobbies), "hobbies")

st.header("Food Preferences")
food = st.selectbox("Select Your Food Preference:", ["Pizza", "Burger", "Pasta", "Sushi", "Salad", "Ice Cream", "Steak", "Tacos", "Curry", "Sandwich"])
# Create a multiselect box for choosing hobbies
Food = st.multiselect("Select Your Food Preferences:", ["Pizza", "Burger", "Pasta", "Sushi", "Salad", "Ice Cream", "Steak", "Tacos", "Curry", "Sandwich"])

# Display the number of selected hobbies
st.write("You selected", len(Food), "hobbies")
# A simple button that does nothing
st.button("Click Me")


# A button that displays text when clicked
if st.button("About"):
    st.markdown("###Can't wait to see you guys!")