from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(_name_)

LEADTEX_API_KEY = os.getenv("x2hoZAqSxneFnuLdba3gB1UPjXh7bv3StBeq01LNoBj0oL8DxrSeoQq5E0hb")
LEADTEX_API_URL = "https://api.leadtex.com/contracts"

@app.route("/sign", methods=["POST"])
def sign_document():
    data = request.json
    contract_id = data["contract_id"]
    user_id = data["user_id"]

    sign_url = sign_contract_in_leadtex(contract_id, user_id)
    return jsonify({"status": "success", "sign_url": sign_url})

def sign_contract_in_leadtex(contract_id, user_id):
    url = f"{LEADTEX_API_URL}/{contract_id}/sign"
    payload = {"user_id": user_id}
    headers = {"Authorization": f"Bearer {LEADTEX_API_KEY}", "Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get("signed_document_url")

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
