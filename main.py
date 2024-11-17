from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for activities in Georgia
activities = {
    "Outdoor Adventures": [
        {"name": "Hiking at Tallulah Gorge", "location": "Tallulah Falls", "description": "A scenic hike with waterfalls and views."},
        {"name": "Kayaking on the Chattahoochee River", "location": "Atlanta", "description": "A fun river adventure right in the city."}
        {"name": "Sope Creek Mountain Bike Trail", "location": "Marietta", "description": "A mix of terrains suitable for mountain biking, hiking, and trail running"}
    ],
    "Historical Sites": [
        {"name": "Savannah Historic District", "location": "Savannah", "description": "Beautiful historic squares and buildings."},
        {"name": "Martin Luther King Jr. National Historic Site", "location": "Atlanta", "description": "Explore the history of the civil rights movement."}
    ],
    "Food & Drink": [
        {"name": "Georgia Wine Trail", "location": "North Georgia", "description": "Visit local wineries and enjoy Georgia wines."},
        {"name": "Ponce City Market", "location": "Atlanta", "description": "A great place for food and shopping."}
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
