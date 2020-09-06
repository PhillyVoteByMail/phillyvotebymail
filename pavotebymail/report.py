import firebase_admin
from firebase_admin import firestore

from db import VoterDB


def main():
    firebase_admin.initialize_app()

    voter_db = VoterDB.connect('voters')

    print("All voters:")
    for voter in voter_db.all_voters():
        print(voter)

    print("")

    print("All voters sent postcards:")
    for voter in voter_db.all_voters_sent_postcards():
        print(voter)


if __name__ == '__main__':
    main()
