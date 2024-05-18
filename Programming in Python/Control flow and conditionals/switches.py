httpStatus = 403

match httpStatus:
    case 400 | 401:
        print("ok")
    case 404:
        print("bad")
    case _:
        print("unknown status")
