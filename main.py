import time

print("🧠 Welcome to the 'Know Your Personality' Quiz!")
print("✨come on Let's discover who you truly are!")
print("="*60)

# Collecting basic info

name = input("👤 What's your name? ").strip()
age = int(input("🎂 What's your age? "))
city = input("🏙️ What's your city? ").strip()
food = input("🍕 What's your favorite food? ").strip()
color = input("🎨 What's your favorite color? ").strip()
animal = input("🐾 What's your favorite animal? ").strip()
hobby = input("🎯 What's your favorite hobby? ").strip() 

# Convert name and color for formatting
name_clean = name.title()
color_upper = color.upper() 


# Age-based personality tag 
if age < 18:
    age_tag = "Enjoy your youth and learn as much as you can! 🌱"
elif 18 <= 30:
    age_tag = " explore and self-discovery!🌍"
else:
    age_tag = "Embrace it and share your wisdom! 🧓"


# Basic personality analysis based on inputs

print("\n 🧠 Analyzing your personality...\n")
time.sleep(3)  # Simulate processing time

print(f"👋 Hello {name}, here are some fun insights about you!\n")
print(f"🎂 Age: {age} — You're at a great stage to {age_tag} 🚀")
print(f"🏙️ City: {city} — A vibrant place with unique vibes! (🔡 {len(city)} characters)")
print(f"🍽️ Favorite Food: {food} — Yummy! That says a lot about your comfort zone 🍽️")
print(f"🎨 Favorite Color: {color} — A beautiful choice that reflects your mood 🌈")
print(f"🐾 Favorite Animal: {animal} — This shows your spirit and character 🐾")
print(f"🎯 Favorite Hobby: {hobby} — That’s how you express yourself and relax 🧘")
print(f"🔍 Data Type Check: Your age is of type {type(age)}")


 # Age in months 
age_months = age * 12
print(f"Your age in months is: {age_months} months")   

# Generate a unique personality code
personality_code = name[0:2].upper() + str(age)[-1]+ animal[0:2] + color[0]
print(f"Your unique personality code is: {personality_code}") 


print("\n🎭 yayy Finalizing your personality ...")
time.sleep(2)
print("=" * 60) 

# Final Result
print(f"🎉 Hey {name_clean}, here's your fun personality report!")
print(f"🌆 You're from {city.title()}, a place of dreams!")
print(f"🍿 You love {food.lower()} and spend your time doing {hobby.lower()}.")
print(f"🎨 You vibe with the color {color_upper} and your spirit animal is the {animal.lower()}.")
print(f"📅 You’ve lived approximately {age_months} months.")
print(f"🧩 You belong to the {age_tag}")
print(f"🔐 Your secret personality code is: {personality_code} 🤖") 


# Fun suggestion based on hobby length
if len(hobby) > 6:
    print("✨ You seem deeply passionate — that hobby says a lot about your vibe!")
else:
    print("💡 Time to explore more hobbies? You’ve got potential!")

# Optional Boolean flag
is_fun = True

if is_fun:
    print("🌈 You are officially certified as: FUNKY AND FABULOUS!")
print("=" * 60)
print("💬 Share this quiz with a friend and compare your vibes!")

time.sleep(2)

print("Thank you for sharing your details! Your personality analysis is complete. 💖")
print("Remember, personality is complex and unique to each individual. Embrace who you are! 🎯")
print("Have a great day ahead, " + name + "!")


