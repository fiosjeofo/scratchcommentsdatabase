import scratchattach as sa
from cryptography.fernet import Fernet
def encrypt(message):
    cipher_suite = Fernet(encryption_key)
    encrypted_data = cipher_suite.encrypt(message.encode())
    return encrypted_data.decode("utf-8")
def decrypt(encrypted_message):
    cipher_suite = Fernet(encryption_key)
    decrypted_data = cipher_suite.decrypt(encrypted_message)
    return decrypted_data.decode()
class connection:
    def __init__(self):
        p = None
        sess = None
        encryption_key = None
        username = None
    def set_projectid(self, pid):
        global p
        p = sess.connect_project(pid)
    def session_connect(self, sessid):
        global sess
        sess = sa.Session(sessid, username=username)
    def set_key(self, enckey):
        global encryption_key
        encryption_key = enckey
    def set_random_key(self):
        global encryption_key
        encryption_key = Fernet.generate_key()
    def get_current_key(self):
        global encryption_key
        return encryption_key
    def set_username(self, user_name):
        global username
        username = user_name
    def delete(self, key):
        comments = range(75)
        limit = 75
        offset = 0
        while len(comments) == 75:
            comments = p.comments(limit=limit, offset=offset)
            for c in comments:
                if decrypt(c["content"]).split("|")[0] == key:
                    p.delete_comment(comment_id=c["id"])
            limit += 75
            offset += 75
    def get(self, key):
        comments = range(75)
        limit = 75
        offset = 0
        while len(comments) == 75:
            comments = p.comments(limit=limit, offset=offset)
            for c in comments:
                if decrypt(c["content"]).split("|")[0] == key:
                    return decrypt(c["content"]).split("|")[1]
            limit += 75
            offset += 75
        return "Item not found"
    def store(self, key, value):
        p.post_comment(content=encrypt(key + "|" + value))

        
        


