import qrcode, vobject, re

regex = r'(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})?' 
compiled_re = re.compile(regex)

def QRgen(text, url=False):
    global QRcounter
    global compiled_re
    if url:
            if re.match(compiled_re, text):
                code = qrcode.make(text)
            else:
                 return None
    else:
        code = qrcode.make(f'- {text}')

    return code
    
def vcardGen(data, scale=10):
    global QRcounter
    global compiled_re
    vcard = vobject.vCard()

    for k,v in data.items():
        if not v.isspace() and len(v) > 0:
            vcard.add(k).value = v
        
    vcard_data = vcard.serialize()
    code = qrcode.make(vcard_data, box_size=scale)

    return code