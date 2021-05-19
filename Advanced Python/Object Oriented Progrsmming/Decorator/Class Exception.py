def invalid(func):
    def wrapper(**kwargs):
        if kwargs['age']<65 or kwargs['health_issues']==False:
            raise Exception(kwargs["name"],"Vaccination only for age 65+!!")
        else:
            return func(**kwargs)
    return wrapper


@invalid
def vaccination(**kwargs):

    for k,v in kwargs.items():
        print(k, ":", v)

    print("Location allocated - EKM\n")

vaccination(name='Johny',age=79,address='Address',health_issues=True)
vaccination(name='Joel',age=77,address='Address',health_issues=True)