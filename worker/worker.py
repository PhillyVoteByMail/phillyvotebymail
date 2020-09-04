from typing import List
import firebase_admin
from firebase_admin import firestore

from db import VoterDB


def main():
    # This assumes that your GOOGLE_APPLICATION_CREDENTIALS env var is set at this time
    firebase_admin.initialize_app()
    db = firestore.client()

    voter_db = VoterDB.connect('voters')

    voters = voter_db.choose_random_voters(2)
    
    for voter in voters:
        voter_db.confirm_postcard_sent_to_voter(voter)


if __name__ == '__main__':
    main()
