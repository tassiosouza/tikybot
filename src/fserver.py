from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import os

CURRENT_DIRECTORY_PATH = '/Users/Tassio/tikybot/src/'
SERVICE_ACCOUNT_KEY_PATH = '../serviceAccountKey.json'
STORAGE_BUCKET_NAME = 'tikybot-wordpress.appspot.com'
FIREBASE_REALTIME_DATABASE_URL = 'https://tikybot-wordpress.firebaseio.com'
class Server():

    def __init__(self, x=0):
        self.x = x

        #******************* Cloud Storage *******************
        self.cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
        firebase_admin.initialize_app(self.cred, {
            'storageBucket': STORAGE_BUCKET_NAME
        })
        self.bucket = storage.bucket()

        #******************** Realtime Database *****************
        self.firebase = firebase.FirebaseApplication(FIREBASE_REALTIME_DATABASE_URL, None)

    def get_accounts(self):
        result = self.firebase.get('/users', None)
        account_list = []
        for key, value in result.items():
            temp = value
            account_list.append(temp)

        return account_list

    def save_file(self, file_name, file):

        blob = self.bucket.blob(file_name)

        # Create new dictionary with the metadata
        metadata  = {"firebaseStorageDownloadTokens": '77e4f2db-dd8e-4ba5-99f0-58a3878b5f1e'}
        file.save(file_name)
        # Set metadata to blob
        blob.metadata = metadata
        blob.upload_from_filename(CURRENT_DIRECTORY_PATH + file_name)

        os.remove(CURRENT_DIRECTORY_PATH + file_name)