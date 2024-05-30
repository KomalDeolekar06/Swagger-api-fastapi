def userEntity(item) ->  dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "password":item["password"]
    }

def usersEntity(entity) -> dict:  #here it will have list of dictionaried like multiple datas
    return [userEntity(item) for item in entity]
