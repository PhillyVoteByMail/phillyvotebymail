import random
import firebase_admin
import names
import uuid
from model import Voter
from db import VoterDB

def main():
    firebase_admin.initialize_app()

    # Create a bunch of voters
    voters = []
    for i in range(10):
        voter = Voter(
            str(uuid.uuid4()),
            random.randint(10,1000),
            names.get_first_name(),
            names.get_last_name(),
            "1234 %s St, Philadelphia, PA 01919" % names.get_first_name(),
            False,
        )
        print(voter)
        voters.append(voter)

    voter_db = VoterDB.connect('voters')

    voter_db.add_voters(voters)


if __name__ == '__main__':
    main()
