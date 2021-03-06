from flask import Flask, request
from flask_cors import CORS
import account_access_visualiser as AAG
import json


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return {
        'data' : 'Hello World'
    }

@app.route('/analysis', methods=['POST'])
def analysis():
    request_data = json.loads(request.data)
    analysis=AAG.graph_analysis(request_data)
    return {
        'analysis': analysis
    }

@app.route('/aag', methods=['GET'])
def aag():
    json='{"Device: laptop":{"name":"laptop","type":"Device","ViewWhenLocked":"false","incoming":[{"recovery":false,"needed":["Biometric: finger"]},{"recovery":false,"needed":["Password: stonechat"]}]},"Device: ipad":{"name":"ipad","type":"Device","ViewWhenLocked":"false","incoming":[{"recovery":false,"needed":["Biometric: finger"]},{"recovery":false,"needed":["Password: stonechat"]}]},"Device: iphone":{"name":"iphone","type":"Device","ViewWhenLocked":"false","incoming":[{"recovery":false,"needed":["Biometric: faceid"]}]},"Biometric: finger":{"name":"finger","type":"Biometric","ViewWhenLocked":"","incoming":[]},"Password: stonechat":{"name":"stonechat","type":"Password","ViewWhenLocked":"","incoming":[{"recovery":false,"needed":["Password Manager: book"]},{"recovery":false,"needed":["Password Manager: WordDocFile"]}],"strength":"weak"},"Biometric: faceid":{"name":"faceid","type":"Biometric","ViewWhenLocked":"","incoming":[]},"Email: btinternet":{"name":"btinternet","type":"Email","opensessions":["Device: laptop","Device: ipad","Device: iphone"],"incoming":[{"recovery":false,"needed":["Password: stonechat1"]}]},"Password: stonechat1":{"name":"stonechat1","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: WordDocFile"]},{"recovery":false,"needed":["Password Manager: book"]}],"strength":"average"},"Social Media: facebook":{"name":"facebook","type":"Social Media","opensessions":["Device: ipad"],"incoming":[],"note":"Not used."},"Password: Stonechat12":{"name":"Stonechat12","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]},{"recovery":false,"needed":["Password Manager: WordDocFile"]}],"strength":"average"},"Number: bankGivenNumber":{"name":"bankGivenNumber","type":"Number","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]},{"recovery":false,"needed":["Password Manager: WordDocFile"]}]},"Number: securityNumber":{"name":"securityNumber","type":"Number","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]},{"recovery":false,"needed":["Password Manager: WordDocFile"]}]},"Word: passcode":{"name":"passcode","type":"Word","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]},{"recovery":false,"needed":["Password Manager: WordDocFile"]}]},"Finance: bank":{"name":"bank","type":"Finance","opensessions":[],"incoming":[{"recovery":false,"needed":["Password: Stonechat12","Number: bankGivenNumber","Number: securityNumber","Word: passcode"]}]},"Shopping: amazon":{"name":"amazon","type":"Shopping","opensessions":["Device: ipad","Device: laptop"],"incoming":[{"recovery":false,"needed":["Email: btinternet","Password: stonechat11"]},{"recovery":true,"needed":["Email: btinternet"]}],"note":"Stores credit card."},"Shopping: m&s":{"name":"m&s","type":"Shopping","opensessions":[],"incoming":[{"recovery":false,"needed":["Email: btinternet","Password: stonechat333"]},{"recovery":true,"needed":["Email: btinternet"]}]},"Password: stonechat11":{"name":"stonechat11","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: WordDocFile"]},{"recovery":false,"needed":["Password Manager: book"]}],"strength":"average"},"Password: stonechat333":{"name":"stonechat333","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: WordDocFile"]},{"recovery":false,"needed":["Password Manager: book"]}],"strength":"average"},"Entertainment: netflix":{"name":"netflix","type":"Entertainment","opensessions":[],"incoming":[{"recovery":false,"needed":["Email: btinternet","Password: wettown11"]},{"recovery":true,"needed":["Email: btinternet"]}]},"Password: wettown11":{"name":"wettown11","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: WordDocFile"]},{"recovery":false,"needed":["Password Manager: book"]}],"strength":"average"},"Password Manager: book":{"name":"book","type":"Password Manager","opensessions":[],"incoming":[]},"Password Manager: WordDocFile":{"name":"WordDocFile","type":"Password Manager","opensessions":["Device: laptop"],"incoming":[],"note":"Daughter has access to this file."}}'
    #json='{"Device: desktop":{"name":"desktop","type":"Device","ViewWhenLocked":"false","incoming":[]},"Device: phone":{"name":"phone","type":"Device","ViewWhenLocked":"false","incoming":[]},"Device: tablet":{"name":"tablet","type":"Device","ViewWhenLocked":"false","incoming":[]},"Device: laptop":{"name":"laptop","type":"Device","ViewWhenLocked":"false","incoming":[]},"Password Manager: book":{"name":"book","type":"Password Manager","opensessions":[],"incoming":[]},"Email: gmail":{"name":"gmail","type":"Email","opensessions":[],"incoming":[{"recovery":false,"needed":["Password: alpha"]}]},"Password: alpha":{"name":"alpha","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]}],"strength":"average"},"Social Media: facebook":{"name":"facebook","type":"Social Media","opensessions":["Device: phone"],"incoming":[{"recovery":false,"needed":["Password: beta","Email: gmail"]}]},"Social Media: linkedin":{"name":"linkedin","type":"Social Media","opensessions":[],"incoming":[{"recovery":false,"needed":["Email: gmail","Password: gamma"]},{"recovery":true,"needed":["Email: gmail"]}]},"Password: beta":{"name":"beta","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]}],"strength":"average"},"Password: gamma":{"name":"gamma","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]}],"strength":"average"},"Username: BankUsername":{"name":"BankUsername","type":"Username","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]}]},"Password: Delta":{"name":"Delta","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]}],"strength":"average"},"Finance: bankWebsite1":{"name":"bankWebsite1","type":"Finance","opensessions":[],"incoming":[{"recovery":false,"needed":["Username: BankUsername","Password: Delta"]}]},"Finance: personalBank":{"name":"personalBank","type":"Finance","opensessions":[],"incoming":[{"recovery":false,"needed":["Email: gmail","Password: Epsilon"]},{"recovery":true,"needed":["Email: gmail"]}]},"Password: Epsilon":{"name":"Epsilon","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]}],"strength":"strong"},"Shopping: amazon":{"name":"amazon","type":"Shopping","opensessions":[],"incoming":[{"recovery":false,"needed":["Password: Zeta","Email: gmail"]}]},"Password: Zeta":{"name":"Zeta","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]}],"strength":"average"},"Shopping: m&s":{"name":"m&s","type":"Shopping","opensessions":[],"incoming":[{"recovery":false,"needed":["Password: Eta","Email: gmail"]},{"recovery":true,"needed":["Email: gmail"]}]},"Password: Eta":{"name":"Eta","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]}],"strength":"average"},"Entertainment: iplayer":{"name":"iplayer","type":"Entertainment","opensessions":[],"incoming":[]},"Shopping: dobbies":{"name":"dobbies","type":"Shopping","opensessions":[],"incoming":[{"recovery":false,"needed":["Password: Theta","Email: gmail"]},{"recovery":true,"needed":["Email: gmail"]}]},"Password: Theta":{"name":"Theta","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]}],"strength":"average"},"Other: dropbox":{"name":"dropbox","type":"Other","opensessions":["Device: laptop"],"incoming":[{"recovery":false,"needed":["Email: gmail","Password: Iota"]},{"recovery":true,"needed":["Email: gmail"]}]},"Password: Iota":{"name":"Iota","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]}],"strength":"average"},"Email: universityLib":{"name":"universityLib","type":"Email","opensessions":[],"incoming":[{"recovery":false,"needed":["Password: Kappa"]}]},"Password: Kappa":{"name":"Kappa","type":"Password","opensessions":[],"incoming":[{"recovery":false,"needed":["Password Manager: book"]}],"strength":"strong"}}'
    accountgraph=AAG.convert_json_to_dictionary(json)
    analysis=AAG.graph_analysis(accountgraph)
    return {
        'analysis': analysis
    }    

@app.route('/generate_password', methods=['POST'])
def generate_password():
    data = json.loads(request.data)
    password=AAG.password_generator(data.get("upper"),data.get("lower"),data.get("numbers"),data.get("symbols"),data.get("length"))
    return {
        "password":password
    }

@app.route('/generate_password', methods=['GET'])
def generate_passwordGet():
    password=AAG.password_generator()
    return {
        "password":password
    }




if __name__ == '__main__':
    app.run(debug=True)