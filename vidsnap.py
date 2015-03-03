from pysnap import Snapchat
from prettytable import PrettyTable
import getpass

class SnapChatVideo(object):
    
    def __init__(self):
        
        self.username = None
        self.password = None
        self.credentials()
        self.snapchat = Snapchat()
        self.snapchat.login(self.username, self.password)
        
        self.friends = PrettyTable(["Username", "Display Name", "Status"])
        self.best_friends = PrettyTable(["Username", "Display"])
        self.setup_friends_table()
    
    def credentials(self):
        self.username = raw_input("Username: ")
        self.password = getpass.getpass("Password: ")
        
    
    def download_media(self, url, start=0, duration=10):
        """Downloads media file to temp folder with given duration and start time. """
        pass
    
    def upload_media(self, path):
        """Creates and returns a media id used to send the snap"""
        pass
    
    def send_snap(self, recipients, snap):
        """Sends snap to given recipients"""
        pass
    
    def setup_friends_table(self):
        friend_status = ["FRIENDS", "PENDING", "BLOCKED"]
        
        friends_info = [(username['name'], username['display'], username['type']) \
        for username in self.snapchat.get_friends()]
        
        for (username, display_name, status_code) in friends_info:
            self.friends.add_row([username, display_name, friend_status[status_code]])
        
        best_friends_info = [(username['name'], username['display'], username['type']) \
        for username in self.snapchat.get_best_friends()]
        
        for (username, display_name, status_code) in friends_info:
            self.best_friends.add_row([username, display_name])

    def get_friends(self):
        """Returns a table of friends' information"""
        print(self.friends)
    
    def get_best_friends(self):
        """Returns a table of best friends' information"""
        print(self.best_friends)
    
    def add_friend(self, friend_username):
        """Add a new friend and returns confirmation/failure message"""
        return self.snapchat.add_friend(friend_username)
        # Need to add a new row to existing table.
    
    def delete_friend(self, friend_username):
        """Delete an existing friend and returns confirmation/failure message"""
        return self.snapchat.delete_friend(friend_username)
        # Need to delete the row from the existing table.