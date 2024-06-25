from flask import Flask, render_template, request, jsonify
import random
import os
from datetime import datetime
import base64

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

skills = [
    "Kucing kampung",
    "Anjing kampung",
    "Burung merpati",
    "Ikan mas koki",
    "Ayam kampung",
    "Bebek",
    "Kambing",
    "Sapi",
    "Kerbau",
    "Kuda",
    "Kelinci",
    "Hamster",
    "Kura-kura",
    "Kuda poni",
    "Kupu-kupu",
    "Katak",
    "Tokek",
    "Cicak",
    "Tikus",
    "Landak mini",
    "Bajak laut boneka",
    "Gantungan kunci lucu",
    "Koin emas mainan",
    "Mobil remote control",
    "Pesawat mainan",
    "Bola sepak plastik",
    "Boneka beruang",
    "Boneka panda",
    "Boneka kelinci",
    "Boneka monyet",
    "Boneka anjing",
    "Boneka kucing",
    "Layang-layang",
    "Gasing",
    "Balon udara mainan",
    "Kelereng",
    "Komik",
    "Buku cerita",
    "Gelang karet warna-warni",
    "Topi jerami",
    "Topi koboi",
    "Tas ransel kecil",
    "Tas selempang",
    "Dompet bergambar",
    "Sarung tangan",
    "Kaos kaki lucu",
    "Sepatu roda",
    "Sepeda mini",
    "Sepatu kets bergambar",
    "Jam tangan digital",
    "Kacamata hitam",
    "Kacamata baca",
    "Kalung mutiara mainan",
    "Cincin plastik",
    "Anting-anting lucu",
    "Gelang emas palsu",
    "Bando telinga kelinci",
    "Ikat rambut pita",
    "Bando kucing",
    "Bando bunga",
    "Topi santai",
    "Topi bola",
    "Sapu tangan lucu",
    "Jam dinding bergambar",
    "Lukisan hewan",
    "Poster pemandangan",
    "Puzzle hewan",
    "Bantal bergambar",
    "Selimut bergambar",
    "Guling lucu",
    "Karpet karakter",
    "Lampu tidur"
]


@app.route('/', methods=['GET', 'POST'])
def index():
    skill = None
    name = None
    if request.method == 'POST':
        name = request.form['name']
        skill = random.choice(skills)
    return render_template('index.html', skill=skill, name=name)

@app.route('/upload_screenshot', methods=['POST'])
def upload_screenshot():
    data = request.form['image']
    name = request.form['name']
    skill = request.form['skill']
    
    # Decode the base64 image
    image_data = base64.b64decode(data.split(',')[1])
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f'{name}_{skill}_{timestamp}.png'
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Save the image
    with open(filepath, 'wb') as f:
        f.write(image_data)

    # Return the URL of the saved image
    image_url = request.url_root + filepath
    return jsonify({'image_url': image_url})

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True, host='0.0.0.0')
