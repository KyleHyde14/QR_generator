import qrcode, vobject

def QRgen(text, scale=10):
    global QRcounter
    code = qrcode.make(text, box_size=scale)

    return code
    
def vcardGen(data, scale=10):
    global QRcounter
    vcard = vobject.vCard()

    for k,v in data.items():
        if not v.isspace() and len(v) > 0:
            vcard.add(k).value = v
        

    vcard_data = vcard.serialize()
    code = qrcode.make(vcard_data, box_size=scale)

    return code