import datetime

import mongoengine


class PackageDb(mongoengine.Document):
    # declaring field in mongodb and its type
    created = mongoengine.DateTimeField(default=datetime.datetime.now);
    name = mongoengine.StringField(required=True);
    value = mongoengine.StringField(required=True);

    # defining how the document will be
    meta = {

        # database name
        'db_alias': 'DataPoints',
        # collection name
        'collection': 'basicDataPoints',
        'indexes': [
            'created',
            'name',
            'value'
        ],
        'ordering': ['name']

    }
