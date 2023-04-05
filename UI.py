
# Import NiceGUI and other modules
import nicegui
from nicegui import ui
import random

# Read in the words from the text files and create the lists of prompts
with open("names.txt", "r") as f:
    person_list = [line.strip() for line in f]

with open("adject.txt", "r") as f:
    adject_list = [line.strip() for line in f]

with open("locations.txt", "r") as f:
    location_list = [line.strip() for line in f]

with open("verbs.txt", "r") as f:
    action_list = [line.strip() for line in f]

with open("lights.txt", "r") as f:
    light_list = [line.strip() for line in f]

with open("mood.txt", "r") as f:
    mood_list = [line.strip() for line in f]

with open("colours.txt", "r") as f:
    colour_list = [line.strip() for line in f]
    
with open("colours.txt", "r") as f:
    colour_list2 = [line.strip() for line in f]

with open("shoes.txt", "r") as f:
    shoes_list = [line.strip() for line in f]

with open("fabrics.txt", "r") as f:
    fabric_list = [line.strip() for line in f]

with open("fabrics.txt", "r") as f:
    fabric_list2 = [line.strip() for line in f]

with open("tops.txt", "r") as f:
    tops_list = [line.strip() for line in f]

with open("bottoms.txt", "r") as f:
    bottoms_list = [line.strip() for line in f]

with open("outfits.txt", "r") as f:
    outfits_list = [line.strip() for line in f]

with open("patterns.txt", "r") as f:
    patterns_list = [line.strip() for line in f]

with open("age.txt", "r") as f:
    age_list = [line.strip() for line in f]

with open("year.txt", "r") as f:
    year_list = [line.strip() for line in f]




# Use the random module to randomly select one prompt from each category
person = random.choice(person_list)
location = random.choice(location_list)
action = random.choice(action_list)
light = random.choice(light_list)
mood = random.choice(mood_list)
colour = random.choice(colour_list)
colour2 = random.choice(colour_list2)
fabric = random.choice(fabric_list)
fabric2 = random.choice(fabric_list2)
pattern = random.choice(patterns_list)
shoe = random.choice(shoes_list)
top = random.choice(tops_list)
outfit = random.choice(outfits_list)
bottom = random.choice(bottoms_list)
adject = random.choice(adject_list)
age = random.choice(age_list)
year = random.choice(year_list)



# Create a button to generate a prompt
button = nicegui.button("Generate a prompt")




# Create a label to display the prompt
label = ui.label("")

# Define a function to generate a prompt
def generate_prompt():
  # Choose random parameters from the lists
  age = random.choice(age_list)
  adject = random.choice(adject_list)
  person = random.choice(person_list)
  location = random.choice(location_list)
  action = random.choice(action_list)
  light = random.choice(light_list)
  mood = random.choice(mood_list)
  colour = random.choice(colour_list)
  colour2 = random.choice(colour_list2)
  fabric = random.choice(fabric_list)
  fabric2 = random.choice(fabric_list2)
  pattern = random.choice(patterns_list)
  shoe = random.choice(shoes_list)
  top = random.choice(tops_list)
  outfit = random.choice(outfits_list)
  bottom = random.choice(bottoms_list)
  year = random.choice(year_list)

  # Choose whether to use an outfit or not
  useoutfit = random.choice([True, False])

  # Generate the prompt based on the parameters
  if useoutfit:
    prompt = f"analog style RAW photo of {age} {adject} {person} {action} at a {location} with a {mood} expression, wearing a {outfit}, {year}, {light} lighting, ultra realistic, highly detailed, intricate, photorealistic, sharp, focus on eyes, (high detailed skin:1.2), 8k uhd, dslr, film grain, Fujifilm XT3"
  else:
    prompt = f"analog style RAW photo of {age} {adject} {person} {action} at a {location} with a {mood} expression, wearing a {colour} {fabric} {top} and {colour2} {fabric2} {bottom} and {shoe}, {year}, {light} lighting, ultra realistic, highly detailed, intricate, photorealistic, sharp, focus on eyes, (high detailed skin:1.2), 8k uhd, dslr, film grain, Fujifilm XT3"

  # Display the prompt on the label
  label.text = prompt

# Connect the button to the function
button.on_click(generate_prompt)

def generate_prompt():
    # do something when the button is clicked
    pass

# Show the window
window.show()

button.on_click(generate_prompt)

# Run the app
ui.run()