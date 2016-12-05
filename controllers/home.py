
# @auth.requires_login()
# @auth.requires_membership('admin')
def index():
    # ver se esta logado

    return dict(msg="Hello AnimalSystem")

def tic():
    return 'jose vicente'

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()




# LOGIN
def user():
    """
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)

    """
    if request.args(0) == 'not_authorized':
        redirect(URL('home','nao_autorizado'))
        pass
    if request.args(0) == 'login':
        redirect(URL('home','cadastro', vars=request.vars))
        pass
    if request.args(0) == 'profile':
        redirect(URL('home','registro', vars=request.vars))
        pass
    if request.args(0) == 'register':
        redirect(URL('home','cadastro', vars=request.vars))
        pass
    if request.args(0) == 'request_reset_password':
        redirect(URL('home','reset_passwold', vars=request.vars))
        pass

    return dict(form=auth())

def cadastro():

    login = auth.login()
    # alterar atributos dos elementos do form login
    login.elements('input')[0].attributes['_type'] = 'email'
    login.elements('input')[3].attributes['_class'] = 'btn btn-info btn-fill btn-wd'

    # alterando atributos dos elementos do form cadastro
    cadastro = auth.register()
    cadastro.elements('input')[2].attributes['_type'] = 'email'
    cadastro.elements('input')[5].attributes['_class'] = 'btn btn-info btn-fill btn-wd'

    logomin = LOGINMIN()

    return dict(cadastro=cadastro,login=login, logomin=logomin)

def reset_passwold():
    logo = IMG(_src=URL('static','images/logo/logo_m.png'),_width='150px')
    reset = auth.request_reset_password()
    return dict(reset=reset,logo=logo)

def nao_autorizado():
    logo ='ok'
    return dict(logo=logo)
