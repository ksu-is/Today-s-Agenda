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
          "image": "https://scontent-atl3-1.xx.fbcdn.net/v/t1.6435-9/32169054_10155442426796099_6131311616018350080_n.jpg?stp=c182.0.728.728a_dst-jpg_s206x206&_nc_cat=106&ccb=1-7&_nc_sid=c43f2c&_nc_ohc=NiJYIEJokYoQ7kNvgETsRyI&_nc_zt=23&_nc_ht=scontent-atl3-1.xx&_nc_gid=Ad9CIDEfvhNr0VRA1TkyMkN&oh=00_AYA0u6aTCUursPpmluJvNgFO9b4ldGkNcjL5gTOr7ItuWw&oe=676417E7"},
         
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
    ],
    "Arts & Culture": [
        {"name": "High Museum of Art",
         "location": "Atlanta",
         "description": "A premier art museum in the Southeast.",
         "url": "https://high.org/",
         "image": "https://exploregeorgia.org/sites/default/files/listing_images/profile/1783/a05172755d59df6cdd317f9dfe102304_high-museum.jpg"},
        
        {"name": "Fox Theatre",
         "location": "Atlanta",
         "description": "Catch a live performance at this historic theater.",
         "url": "https://www.foxtheatre.org/",
         "image": "https://exploregeorgia.org/sites/default/files/listing_images/profile/1429/yukari_umekawa_Stage2.jpg"},
        
        {"name": "Telfair Museums",
         "location": "Savannah",
         "description": "Explore fine art and historic homes.",
         "url": "https://www.telfair.org/",
         "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmuSzzJftjr-H1p7LlLxNPO0VU4N0eVg1aFQ&s"},
        
        {"name": "Atlanta Botanical Garden",
         "location": "Atlanta",
         "description": "Stroll through beautiful gardens and exhibits.",
         "url": "https://atlantabg.org/",
         "image": "https://lh3.googleusercontent.com/p/AF1QipOrlE1P8aLXBGkAaSHaB7QuG3a-pkHXGlxSiu4X=s188-p-k"}
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
