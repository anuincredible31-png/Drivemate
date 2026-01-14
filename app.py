import streamlit as st

st.set_page_config(page_title="DriveMate", page_icon="🚗")

# Store bookings
if "bookings" not in st.session_state:
    st.session_state.bookings = []

st.title("🚗 DriveMate")
st.write("Use your own car • Rent your idle car • Book trusted drivers")

menu = st.sidebar.selectbox(
    "Choose Mode",
    [
        "Book a Driver",
        "Emergency Mode",
        "My Booking Status",
        "Driver Dashboard"
    ]
)

# ---------------- BOOK DRIVER ----------------
if menu == "Book a Driver":
    st.header("🧑‍✈️ Book a Driver")

    name = st.text_input("Your Name")
    location = st.text_input("Pickup Location")

    if st.button("Book Driver"):
        st.session_state.bookings.append({
            "user": name,
            "location": location,
            "type": "Normal",
            "status": "Pending",
            "driver": "Not assigned"
        })
        st.success("✅ Booking created. Waiting for driver acceptance.")

# ---------------- EMERGENCY MODE ----------------
elif menu == "Emergency Mode":
    st.header("🚨 Emergency Driver Request")

    name = st.text_input("Your Name")
    location = st.text_input("Current Location")

    if st.button("Request Emergency Driver"):
        st.session_state.bookings.append({
            "user": name,
            "location": location,
            "type": "Emergency",
            "status": "Pending",
            "driver": "Not assigned"
        })
        st.error("🚨 Emergency booking sent with HIGH priority!")

# ---------------- USER VIEW STATUS ----------------
elif menu == "My Booking Status":
    st.header("📄 My Booking Status")

    username = st.text_input("Enter your name to check status")

    found = False
    for booking in st.session_state.bookings:
        if booking["user"] == username:
            found = True
            st.write(f"📍 Location: {booking['location']}")
            st.write(f"⚠️ Type: {booking['type']}")
            st.write(f"📌 Status: {booking['status']}")
            st.write(f"🧑‍✈️ Driver: {booking['driver']}")
            st.divider()

    if not found:
        st.info("No booking found for this name.")

# ---------------- DRIVER DASHBOARD ----------------
elif menu == "Driver Dashboard":
    st.header("🧑‍✈️ Driver Dashboard")

    driver_name = st.text_input("Driver Name")

    for i, booking in enumerate(st.session_state.bookings):
        if booking["status"] == "Pending":
            st.subheader(f"Booking {i+1}")
            st.write(f"👤 User: {booking['user']}")
            st.write(f"📍 Location: {booking['location']}")
            st.write(f"⚠️ Type: {booking['type']}")

            if st.button(f"Accept Booking {i+1}"):
                booking["status"] = "Accepted"
                booking["driver"] = driver_name
                st.success("✅ Booking accepted!")
