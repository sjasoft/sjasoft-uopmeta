from sjasoft.uopmeta.schemas import meta
from sjasoft.uopmeta.schemas.meta import Schema, MetaRole

pkm_schema = Schema(
    name = 'pkm_schema',
    roles = [
        MetaRole(name='group_contains', reverse_name='group_contains*'),
        MetaRole(name='tag_applies', reverse_name='tag_applies*'),
        MetaRole(name='contains_group', reverse_name='contains_group*'),
        MetaRole(name='has_user', reverse_name='in_tenant'),
    ],
    classes = [
        meta.app_class('File', 'DescribedComponent',
                       meta.app_attr('path', 'string', required=True)),
        meta.app_class('WebURL', 'DescribedComponent',
                       meta.app_attr('title', 'string'),
                       meta.app_attr('url', 'string', required=True)),
        meta.app_class('Folder', 'DescribedComponent',
                       meta.app_attr('path', 'string', required=True)),
        meta.app_class('DropboxInfo', 'PersistentObject',
                       meta.app_attr('credentials', 'json'),
                       meta.app_attr('path', 'string')),
        meta.app_class('EvernoteInfo', 'PersistentObject',
                       meta.app_attr('credentials', 'json')),
        meta.app_class('Address', 'PersistentObject',
                       meta.app_attr('street_address1', 'string', required=True),
                       meta.app_attr('street_address2', 'string'),
                       meta.app_attr('city', 'string', required=True),
                       meta.app_attr('state/province', 'string', required=True),
                       meta.app_attr('country', 'string', required=True),
                       meta.app_attr('postal_zip', 'string')),
        meta.app_class('Phone', 'PersistentObject',
                       meta.app_attr('full_number', 'string', required=True),
                       meta.app_attr('category', 'string')),
        meta.app_class('Person', 'DescribedComponent',
                       meta.app_attr('first_name', 'string'),
                       meta.app_attr('last_name', 'string'),
                       meta.app_attr('full_name', 'string'),
                       meta.app_attr('email', 'email'))
    ]
)