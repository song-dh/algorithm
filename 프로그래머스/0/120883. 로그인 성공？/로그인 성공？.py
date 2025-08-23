def solution(id_pw, db):
    user = findUser(id_pw[0], db)
    if len(user) == 0:
        return "fail"
    elif user[1] == id_pw[1]:
        return "login"
    else:
        return  "wrong pw"
def findUser(userId, db):
    for id, pw in db:
        if id==userId:
            return [id, pw]      
    return []