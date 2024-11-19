from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for activities in Georgia
activities = {
    "Outdoor Adventures": [
        {"name": "Hiking at Tallulah Gorge", 
         "location": "Tallulah Falls", 
         "description": "A scenic hike with waterfalls and views.", 
         "url": "https://gastateparks.org/TallulahGorge",
         "image": "https://lh3.googleusercontent.com/p/AF1QipPJocjoF7vtNvRaWuyFAWoY8ywb8GU_5YN4Vy4p=s3840-w3840-h1982"},
        
        {"name": "Kayaking on the Chattahoochee River", 
         "location": "Atlanta", 
         "description": "A fun river adventure right in the city.", 
         "url": "https://noc.com/trips/chattahoochee-sit-on-top-kayak-metro/",
         "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQM6fQ47UvJIR5r-W5B3rWPMuWhSymzGcgUEA&s"},
        
        {"name": "Sope Creek Mountain Bike Trail", 
         "location": "Marietta", 
         "description": "A mix of terrains suitable for mountain biking, hiking, and trail running.", 
         "url": "https://www.atlantatrails.com/hiking-trails/a-getaway-close-to-home-sope-creek/",
         "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/79/9c/da/fishing-dock-at-sibley.jpg?w=900&h=500&s=1"},
        
         {"name": "Red Top Mountain State Park", 
         "location": "Acworth", 
         "description": "Includes hiking, campsites, cabins, and a marina", 
         "url": "https://gastateparks.org/RedTopMountain",
         "image": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcR46ti3hGmwGye0JGP9eEZrvKJfHAvionR1VABiWAQKwjsnWTmVsPebAS2MWvgF4jIwFMfjkjsHVrYfGlyok4vExomoR9IBZgzGkSZkqw"},
         
         {"name": "Stone Mountain Park",
          "location": "Stone Mountain",
          "description": "Enjoy hiking, laser shows, and beautiful views.",
          "url": "https://www.stonemountainpark.com/",
          "image": "data:image/jpeg;base64,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"},
         
        {"name": "Okefenokee Swamp Park",
         "location": "Waycross",
         "description": "Explore one of the most well-preserved swamps in the U.S.",
         "url": "https://okeswamp.org/",
         "image": "https://exploregeorgia.org/sites/default/files/styles/listing_slideshow/public/listing_images/profile/2702/102_04135bd01e960e9f4756a21498520a3fa4e9.jpg?itok=82BlARuh"}
    ],
    "Historical Sites": [
        {"name": "Savannah Historic District", 
         "location": "Savannah", 
         "description": "Beautiful historic squares and buildings.", 
         "url": "https://www.visitsavannah.com/",
         "image": "https://lh3.googleusercontent.com/p/AF1QipPbIEtN_b1m3oiQYCf9xJT-7weeF02U5gtor-Du=s125-p-k"},
        
        {"name": "Martin Luther King Jr. National Historic Site", 
         "location": "Atlanta", 
         "description": "Explore the history of the civil rights movement.", 
         "url": "https://www.nps.gov/malu/index.htm",
         "image": "https://lh3.googleusercontent.com/p/AF1QipNBbPQZCuATX9EcdAvQlWdA17KH0EP6-cwD0YTf=s125-p-k"},
        
        {"name": "Fort Pulaski National Monument",
         "location": "Savannah",
         "description": "Learn about Civil War history and explore the fort.",
         "url": "https://www.nps.gov/fopu/index.htm",
         "image": "https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcRM_-e7zt4jQBIikDNj5FK9b9uyAcMt12XhJgvjWbDIVJaAvoSbO-kp8PkSdktsKhodcIJ5G5SLg2vUu8GcN4yBPyqWVGPPGKtc5-OHyA"},
        
        {"name": "Andersonville National Historic Site",
         "location": "Andersonville",
         "description": "Visit a historic Civil War prison site and cemetery.",
         "url": "https://www.nps.gov/ande/index.htm",
         "image": "https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcTL4iounpR3AvRU9izPAegAb6rYVj-92qeS0b1efQozOFWgOWscjmiblimPBRE7SFdjKmXaeFn8-5tzBEP7rMfE9wZPzFJyEU00Ns9s6w"}
    ],
    "Food & Drink": [
        {"name": "Georgia Wineries", 
         "location": "North Georgia", 
         "description": "Visit local wineries and enjoy Georgia wines.", 
         "url": "https://wineriesingeorgia.com/",
         "image": "https://wineriesingeorgia.com/wp-content/uploads/2020/09/Montaluce-2thumb.jpeg"},
        
        {"name": "Ponce City Market", 
         "location": "Atlanta", 
         "description": "A great place for food and shopping.", 
         "url": "https://poncecitymarket.com/",
         "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0D9sWrLE2oDZKjnxjI60q0CPXhbyHzN1btQ&s"},
        
        {"name": "Dave's Hot Chicken",
         "location": "Conyers",
         "description": "The first Dave's Hot Chicken to be opened in Georgia. (Be wary, wait times may be long!)",
         "url": "https://daveshotchicken.com/locations/ga/conyers/1447-hwy-138-se/",
         "image": "https://lh3.googleusercontent.com/p/AF1QipMTRMRsshNp3BMpR7QbWO94XhybV8mYITce5rYc=s125-p-k"},
        
        {"name": "Savannah Food Tour",
         "location": "Savannah",
         "description": "Discover Savannah's best cuisine with a guided tour.",
         "url": "https://www.savannahfoodtours.com/",
         "image": "https://savannahfoodtours.com/wp-content/uploads/2023/05/Flavors-Logo.png"}
    ]
}

# Homepage - Ask user what they want to do
@app.route('/')
def home():
    return render_template('index.html', categories=activities.keys())

# Show activities based on user choice
@app.route('/activities', methods=['POST'])
def show_activities():
    category = request.form.get('category')
    chosen_activities = activities.get(category, [])
    return render_template('activities.html', category=category, activities=chosen_activities)

if __name__ == '__main__':
    app.run(debug=True)
