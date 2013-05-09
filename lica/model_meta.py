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
    ("VERIFICATION","VERIFICATION"),
    ) 
    



BONUSTRIGGERTYPE =(
    ("LOGIN","LOGIN"),
    ("REGISTRATION","REGISTRATION"),
    ("ADD_INTREST","ADD_INTREST"),
    ("ADD_DEPARTMENT","ADD_DEPARTMENT"),
    
    
    
)


CREDITTYPE=(
    ('POINTS','POINTS'),
    )    
