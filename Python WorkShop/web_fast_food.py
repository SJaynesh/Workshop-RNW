import streamlit as st

# print("Fast Food Order Menu Drive System")

st.sidebar.image("https://cdni.iconscout.com/illustration/premium/thumb/food-truck-with-barbecue-illustration-download-in-svg-png-gif-file-formats--barbeque-grill-pot-breakfast-private-transportation-van-pack-drink-illustrations-4144378.png")
st.sidebar.title("Fast Food 🏪")

st.sidebar.success("Created by Jaynesh Sarkar")

st.title("Menu")

st.markdown("##### Press 01 for 🌭 Hot Dog")
st.markdown("##### Press 02 for 🍟 Chips")
st.markdown("##### Press 03 for 🍦 Ice Cream")

n = st.text_input("Enter your choice : ")


if st.button("Order Now 🛒") :
    if(n=='1') :
        st.info("Your Ordered a 🌭 Hot Dog")
    elif(n=='2'):
        st.info("Your Ordered a 🍟 Chips")
    elif(n=='3'):
        st.info("Your Ordered 🍦 Ice Cream")
    else:
        st.info("Your Ordered is Invalid 😮")