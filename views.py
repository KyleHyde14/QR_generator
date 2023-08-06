from flask import Blueprint, render_template, request, redirect
from QR_gen import QRgen, vcardGen

views = Blueprint(__name__, 'views')

QRcounter = 0

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/api', methods=['POST'])
def createQR():
    global QRcounter
    if request.method == 'POST':
        if request.form.get("email"):
            data = {
                'FN': request.form.get("full-name"),
                'TITLE': request.form.get("title"),
                'TEL': request.form.get("phone-number"),
                'EMAIL': request.form.get("email"),
                'URL': request.form.get("website"),
                'NOTES': request.form.get("notes")
            }
            scale = int(request.form.get('scale'))

            img = vcardGen(data, scale)
            QRcounter +=1
            img_name = f'QR{QRcounter}.png'
            img.save(f'static/images/{img_name}')

            return render_template('qr.html', QRname=img_name )

        else:
            data = request.form.get('text')
            scale = int(request.form.get('scale'))

            img = QRgen(data, scale)
            QRcounter +=1
            img_name = f'QR{QRcounter}.png'
            img.save(f'static/images/{img_name}')

            return render_template('qr.html', QRname=img_name )
            
        

    