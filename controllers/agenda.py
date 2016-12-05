@auth.requires_login()
def index():
    marcaDagua = MARCADAGUA()
    return dict(marcaDagua=marcaDagua)
