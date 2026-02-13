import hashlib

def calculate_hash(data):
  return hashlib.sha256(data).hexdigest()