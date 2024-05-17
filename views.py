from flask import Blueprint, render_template, request, jsonify
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
        if request.form.get('id') == 'vcard-form':
            required = ['full-name', 'email', 'phone-number']
            if  any(not request.form.get(x) for x in required):
                result = {
                    'success': False,
                    'message': 'Fill all required fields'
                }
                return jsonify(result)
            data = {
                'FN': request.form.get("full-name"),
                'TITLE': request.form.get("title"),
                'TEL': request.form.get("phone-number"),
                'EMAIL': request.form.get("email"),
                'URL': request.form.get("website"),
                'NOTES': request.form.get("notes")
            }
            scale = 10

            img = vcardGen(data, scale)
            QRcounter +=1
            img_name = f'QR{QRcounter}.png'
            img.save(f'static/images/{img_name}')

            result = {
                'success': True,
                'qr_img': f'static/images/{img_name}'
            }

            return jsonify(result) 
        
        elif request.form.get('id') == 'label-form':
            required = ['ref', 'model', 'quality', 'color', 'combine']
            if any(not request.form.get(x) for x in required):
                result = {
                    'success': False,
                    'message': 'Fill all required fields'
                }
                return jsonify(result)
            url = True
            REF = request.form.get('ref')
            MO = request.form.get('model')
            CA = request.form.get('quality')
            CO = request.form.get('color')
            COMBINE = request.form.get('combine')
            data = f'https://hostingurl.com/?REF={REF}&MO={MO}&CA={CA}&CO={CO}&COMBINE={COMBINE}'
            img = QRgen(data, url)
            if(img):
                QRcounter +=1
                img_name = f'QR{QRcounter}.png'
                img.save(f'static/images/{img_name}')

                result = {
                    'success': True,
                    'qr_img': f'static/images/{img_name}'
                }

            else:
                result = {
                    'success': False,
                    'message': 'Something went wrong'
                }

            return jsonify(result)

        else:
            url = False
            if request.form.get('id') == 'url-form':
                url = True

            if url:
                data = request.form.get('url')
            else:
                data = request.form.get('text')

            img = QRgen(data, url)
            if(img):
                QRcounter +=1
                img_name = f'QR{QRcounter}.png'
                img.save(f'static/images/{img_name}')

                result = {
                    'success': True,
                    'qr_img': f'static/images/{img_name}'
                }

            else:
                result = {
                    'success': False,
                    'message': 'URL pattern must be: Https://example.ex'
                }
            
            return jsonify(result)
            
        

    