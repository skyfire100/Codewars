import hashlib
def crack(hash):
    for i in range(99999):
        if hashlib.md5(str(i).zfill(5).encode("utf")).hexdigest() == hash:
            return str(i).zfill(5)