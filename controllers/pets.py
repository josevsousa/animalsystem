@auth.requires_login()
# @auth.requires_membership('admin')
def index():
    marcaDagua = MARCADAGUA()

    # pets
    PETS = []

    pet = DIV(
        DIV(
            'Cocotinho',
        _class="textPet"),
    _class="card",
    _id="cardPets")

    PETS.append(pet)
    # PETS.append(pet)


    return dict(marcaDagua=marcaDagua,PETS=PETS)
