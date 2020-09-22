"""User Model."""
from orator import SoftDeletes
from orator.orm import belongs_to, accessor, scope

from config.database import Model
from app.Account import Account


class User(SoftDeletes, Model):
    """User Model."""

    __fillable__ = ['first_name', 'last_name', 'email', 'password', 'photo_path', 'owner', 'account_id']
    __append__ = ["role", "is_demo_user"]
    __auth__ = 'email'

    @belongs_to
    def account(self):
        return Account
    
    @accessor
    def role(self):
        owner = self.get_raw_attribute('owner')
        return 'owner' if owner else 'user'
    
    @accessor
    def is_demo_user(self):
        return self.email == 'johndoe@example.com'
    
    @scope
    def order_by_name(self, query):
        return query.order_by('last_name').order_by('first_name')

    @scope
    def where_role(self, query, role):
        if role == 'owner':
            return query.where('owner', True)
        else:
            return query.where('owner', False)
    
    @scope
    def filter(self, query, filters):
        if filters.get('search', None):
            search_token = f"%{filters['search']}%"
            query.where('first_name', 'like', search_token) \
            .or_where('last_name', 'like', search_token) \
            .or_where('email', 'like', search_token)
        
        if filters.get('role', None):
            query.where_role(filters['role'])
        
        if filters.get('trashed', None):
            if filters['trashed'] == 'with':
                query.with_trashed()
            else:
                # only trashed, ie User with a not null deleted date
                query.where('deleted_at', None)

        return query
