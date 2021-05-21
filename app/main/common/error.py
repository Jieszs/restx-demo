from werkzeug.exceptions import HTTPException


class ValidateException(HTTPException):
    """
    为了使代码简洁, 首先定义一个最基本的类, 供其它类继承, 这个自定义的APIException继承HTTPException.
    1. 为了返回特定的body信息, 需要重写get_body;
    2. 为了指定返回类型, 需要重写get_headers.
    3. 为了接收自定义的参数, 重写了__init__;
    4. 同时定义了类变量作为几个默认参数.(code500和error_code:999 均表示未知错误, error_code表示自定义异常code)
    """
    code = 400
    msg = '请求参数错误'
    data = ''

    # 自定义需要返回的信息，在初始化完成并交给父类
    def __init__(self, msg=None, code=None, data=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if data:
            self.data = data
        super(ValidateException, self).__init__(msg, None)
