from django.db import models


class EnumField(models.Field):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 104
        super(EnumField, self).__init__(*args, **kwargs)
        if not self.choices:
            raise AttributeError('EnumField requires `choices` attribute.')

    def db_type(self):
        return "enum(%s)" % ','.join("'%s'" % k for (k, _) in self.choices)


TRIGGERS=(
    ("WELCOME","WELCOME"),
    ("WELCOME_BONUS","WELCOME_BONUS"),
    ("SIGNUP","SIGNUP"),
    ("SIGNUP_BONUS","SIGNUP_BONUS"),
    ("VERIFICATION","VERIFICATION"),
    ("VERIFICATION_BONUS","VERIFICATION_BONUS"),
    ("LOGIN","LOGIN"),
    ("LOGIN_BONUS","LOGIN_BONUS"),
    ("PASSWORD_RESET","PASSWORD_RESET")
    ) 
    



BONUSTRIGGERTYPE =(
    ("WELCOME","WELCOME"),
    ("REGISTRATION","REGISTRATION"),
    ("VERIFICATION","VERIFICATION"),
    ("LOGIN","LOGIN"),
    ("ADD_INTREST","ADD_INTREST"),
    ("ADD_DEPARTMENT","ADD_DEPARTMENT"),
)


CREDITTYPE=(
    ('POINTS','POINTS'),
    )    




STUDENTLEVEL =(
    ("ZERO","ZERO"),
    ("FIRST",'FIRST'),
    ("SECOND",'SECOND'),
    ("THIRD",'THIRD'),
    ("FOURTH",'FOURTH'),
    
)