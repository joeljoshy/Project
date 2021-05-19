def admin_auth(func):
    def wrapper(user,pin):
        if user!='admin':
            raise Exception('Not allowed')
        else:
            return func(user,pin)
    return wrapper

@admin_auth
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_auth
def delete_account(user,accno):
    return str(accno)+"deleted"

#print(change_pin('admin',1000))
print(delete_account('joel',1000))
