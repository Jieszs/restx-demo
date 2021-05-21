def message(status, msg):
    response_object = {"status": status, "message": msg}
    return response_object


def success(msg):
    return message(True, msg)


def success_data(msg, data):
    suc = success(msg)
    suc['data'] = data
    return suc


def validation_error(status, errors):
    response_object = {"status": status, "errors": errors}
    return response_object


def err_resp(msg, reason, code):
    err = message(False, msg)
    err["error_reason"] = reason
    return err, code


def internal_err_resp():
    err = message(False, "Something went wrong during the process!")
    err["error_reason"] = "server_error"
    return err, 500
