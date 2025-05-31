import streamlit as st
import time

st.set_page_config(page_title="Know Your Personality Quiz", page_icon="🧠")

# Page Title
st.title("🧠 Know Your Personality Quiz")
st.markdown("✨ Let's discover who you truly are — through colors, food, and fun facts!")
st.markdown("---")

# Sidebar Inputs
st.sidebar.title("🎯 Enter Your Details")
name = st.sidebar.text_input("👤 Your name?")
age = st.sidebar.number_input("🎂 Your age?", min_value=1, max_value=120, step=1)
city = st.sidebar.text_input("🏙️ City you live in?")
food = st.sidebar.text_input("🍕 Your favorite food?")
color = st.sidebar.text_input("🎨 Your favorite color?")
animal = st.sidebar.text_input("🐾 Your spirit animal?")
hobby = st.sidebar.text_input("🎮 A hobby you enjoy?")
generate = st.sidebar.button("🔍 Generate My Personality")

# Run only when button is clicked
if generate:
    with st.spinner("🔮 Reading your aura..."):
        time.sleep(2)

    st.info("✨ Analyzing colors, cravings, and cosmic connections...")
    time.sleep(2)

    st.info("💡 Synthesizing a custom personality profile with advanced... vibes! 😄")
    time.sleep(2)

    # Formatting inputs
    name_clean = name.strip().title()
    city_title = city.strip().title()
    food_lower = food.lower()
    color_upper = color.strip().upper()
    hobby_lower = hobby.lower()
    animal_lower = animal.lower()
    age_months = age * 12
    personality_code = name[:2].upper() + str(age)[-1] + animal[:1].upper() + color[:1].lower()

    # Age Tag
    if age < 18:
        age_tag = "Enjoy your youth and learn as much as you can! 🌱"
    elif age <= 30:
        age_tag = "Explore and discover yourself! 🌍"
    else:
        age_tag = "Embrace your experience and share your wisdom! 🧓"

    # Display Results
    st.success(f"🎉 Hey **{name_clean}**, here's your personality report!")
    st.markdown("---")
    st.write(f"📍 You're from **{city_title}** — full of stories and dreams.")
    st.write(f"🍽️ You love **{food_lower}**, and it says a lot about your comfort and taste.")
    st.write(f"🎯 In your free time, you enjoy **{hobby_lower}**, which fuels your soul.")
    st.write(f"🎨 The color **{color_upper}** is your vibe — bold, calm, or playful.")
    st.write(f"🐾 Your spirit animal is the **{animal_lower}**, symbolizing your inner energy.")
    st.write(f"📅 You've lived through **{age_months} months** of adventure.")
    st.write(f"💡🧩 You belong to this life stage: **{age_tag}**")
    st.write(f"🔐 Your **Personality Code**: `💡 {personality_code}`")

    # Bonus Comment
    if len(hobby) > 8:
        st.info("🎨 You're deeply passionate — your hobby shows creative energy!")
    else:
        st.info("🚀 You're still exploring passions. Keep discovering!")

    # Fun End Note
    st.success("🌈 You are officially certified as: **FUNKY AND FABULOUS**! 😎")
    st.markdown("💖💖💖💖💖💖💖💖💖💖")
    st.markdown("---")
    st.balloons()
    st.caption("💬 Share this with your friends and compare your vibes!")
