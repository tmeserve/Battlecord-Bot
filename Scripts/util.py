import os
import json

class Util:
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'teams')
        print(self.path)

    def create_team(self, name, owner_id):
        with open(os.path.join(self.path, name), 'w+') as team_file:
            data = self.get_data()
            data['name'] = name
            data['owner'] = owner_id

    def add_member(self, name, member):
        pass

    def remove_member(self, name, member):
        pass

    def get_data(self):
        return {'name' : '', 'points': 0, "owner": "", "members": []}