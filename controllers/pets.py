@auth.requires_login()
# @auth.requires_membership('admin')
def index():
    marcaDagua = MARCADAGUA()
    return dict(marcaDagua=marcaDagua)
