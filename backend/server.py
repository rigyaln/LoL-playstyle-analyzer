from flask import *
from apiMethods import *
from playstyleCalcMethods import *
from champData.champTagsDic import champ_to_playstyle
from dotenv import load_dotenv
import os
api_key = os.getenv("riot_api_key")
print(f"API Key: {api_key}")

load_dotenv()
app = Flask(__name__,
            static_folder="../frontend/static",  # Path to static files
            template_folder="../frontend/templates")  # Path to templates

@app.route('/')
def home():
    # Renders the HTML template (index.html) from the 'frontend/templates' folder
    return render_template('index.html')
@app.route('/api/playstyle', methods=['POST'])
def playstyle():
    data = request.get_json()  # Get JSON data from POST request
    username = data.get('username')
    tagline = data.get('tagline')

    # Check if username or tagline is missing
    if not username or not tagline:
        return jsonify({'message': 'Missing username or tagline'}), 400

    try:
        # Perform the backend API calls and calculations
        print(username, tagline)
        puuid_json = get_puuid(username, tagline, api_key)
        puuid = puuid_json['puuid']

        masteries = get_masteries(puuid, api_key)
        champs_and_masteries = getChampNames_AND_masteries(masteries)
        tags_count = tally_tags(champs_and_masteries, champ_to_playstyle)
        tag_percentages = calculate_tag_percentages(tags_count)
        playstyle_summary = generate_playstyle_summary(tag_percentages)

        return jsonify(playstyle_summary)

    except Exception as e:
        print(f"Error in playstyle route: {e}")  # Log the error to the console
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
