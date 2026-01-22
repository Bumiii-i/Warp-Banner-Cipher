from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# --- LOGIKA KRIPTOGRAFI ---
class WarpBannerCipher:
    def __init__(self):
        self.mapping = {
            'A': ['SE10INNT1', '4427191', '4433598'],
            'B': ['JY10BEDN2', '1023138', '1030591'],
            'C': ['SW11ITRN1', '1977444', '1964361'],
            'D': ['LU11ESCN2', '5051214', '5060244'],
            'E': ['BL12TESE1', '1716507', '1725637'],
            'F': ['KA12PEND2', '2633867', '2617407'],
            'G': ['IL13BRSN1', '6016460', '6027690'],
            'H': ['FX13SEES2', '2009230', '2020460'],
            'I': ['JI14ISSD1', '2997621', '2981253'],
            'J': ['TN14WEBL2', '3794322', '3810321'],
            'K': ['HU15NTFT1', '906738',  '918345'],
            'L': ['AR15ANGE2', '1591798', '1567338'],
            'M': ['RM16PTMR1', '4610791', '4593348'],
            'N': ['DR16BMTT2', '850620',  '853808'],
            'O': ['BS20RDRE1', '1746496', '1741344'],
            'P': ['SP20EYEE2', '7545824', '7549396'],
            'Q': ['AC21AGSE1', '4595508', '4601448'],
            'R': ['AV21IYDY2', '1192968', '1198908'],
            'S': ['RO22FGNW1', '2335196', '2324192'],
            'T': ['BO22SGLE2', '5229432', '5238096'],
            'U': ['FI23WSRT1', '1906240', '1913756'],
            'V': ['JA23YTPS2', '3021720', '3007240'],
            'W': ['YU24DEST1', '6525204', '6535544'],
            'X': ['JI24TESS2', '1897416', '1909404'],
            'Y': ['FE25IVHT1', '201848',  '210240'],
            'Z': ['LI25STTE2', '462528',  '442048'],
            '1': ['RA26NUER1', '3003312', '3015852'],
            '2': ['SU27AGAT1', '1030600', '1004896'],
            '3': ['FU27LGHE2', '3768360', '3753125'],
            '4': ['TH30IOVL1', '750625',  '753375'],
            '5': ['AG30TEGD2', '1305850', '1301125'],
            '6': ['TR31IFFR1', '4944275', '4948450'],
            '7': ['MY31FEPH2', '1522600', '1528075'],
            '8': ['CA32MEBL1', '2712750', '2703825'],
            '9': ['AN32LEFS2', '6008500', '6015750'],
            '0': ['HY33LGSY1', '2315775', '2323125']
        }
        
        # Dictionary terbalik (Cipher -> Huruf)
        self.reverse_mapping = {}
        for char, ciphers in self.mapping.items():
            for cipher in ciphers:
                self.reverse_mapping[cipher] = char

    def encrypt(self, plaintext):
        ciphertext_list = []
        clean_text = plaintext.replace(" ", "")
        
        for char in clean_text:
            upper_char = char.upper()
            if upper_char in self.mapping:
                ciphertext_list.append(random.choice(self.mapping[upper_char]))
            else:
                pass
                
        return "".join(ciphertext_list)

    def decrypt(self, ciphertext):
        plaintext_list = []
        idx = 0
        length = len(ciphertext)
        
        while idx < length:
            found = False
            for check_len in [9, 7, 6]:
                if idx + check_len <= length:
                    chunk = ciphertext[idx : idx+check_len]
                    if chunk in self.reverse_mapping:
                        plaintext_list.append(self.reverse_mapping[chunk])
                        idx += check_len
                        found = True
                        break
            
            if not found:
                idx += 1
                
        return "".join(plaintext_list)

cipher_tool = WarpBannerCipher()

# --- ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    data = request.json
    text = data.get('text', '')
    result = cipher_tool.encrypt(text)
    return jsonify({'result': result})

@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    data = request.json
    text = data.get('text', '')
    result = cipher_tool.decrypt(text)
    return jsonify({'result': result})

if __name__ == '__main__':

    app.run(debug=True)
