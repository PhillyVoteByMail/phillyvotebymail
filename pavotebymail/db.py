from typing import List
import firebase_admin
from firebase_admin import firestore
from model import Voter

class VoterDB(object):
    @classmethod
    def connect(cls, collection_name) -> 'VoterDB':
        db = firestore.client()

        return cls(db, collection_name)

    def __init__(self, db, collection_name):
        self._collection = db.collection(collection_name)
        self._db = db

    def add_voters(self, voters: List[Voter]):
        batch = self._db.batch()

        for voter in voters:
            voter_doc_ref = self._collection.document(voter.id)
            batch.set(voter_doc_ref, voter.to_dict())
        
        batch.commit()

    def all_voters_sent_postcards(self) -> List[Voter]:
        return self._voters_from_collection_stream(
            self._collection.where('was_sent_postcard', '==', True).order_by('priority').stream()
        )

    def all_voters(self, limit=None) -> List[Voter]:
        collection = self._collection
        if limit:
            collection = collection.limit(limit)
        return self._voters_from_collection_stream(
            collection.order_by('priority').stream(),
        )

    def choose_random_voters(self, limit: int) -> List[Voter]:
        # Choose voters based on their priority value
        # TODO handle errors
        return self._voters_from_collection_stream(
            self._collection.where('was_sent_postcard', '==', False).order_by('priority').limit(limit).stream()
        )

    def _voters_from_collection_stream(self, stream) -> List[Voter]:
        voters = []
        for voter_doc in stream:
            voter_doc_dict = voter_doc.to_dict()
            voters.append(Voter(
                voter_doc.id,
                voter_doc_dict['priority'],
                voter_doc_dict['first_name'],
                voter_doc_dict['last_name'],
                voter_doc_dict['address'],
                voter_doc_dict['was_sent_postcard'],
            ))
        return voters


    def confirm_postcard_sent_to_voter(self, voter) -> Voter:
        # TODO handle errors
        voter_doc_ref = self._collection.document(voter.id)
        voter_doc_dict = voter_doc_ref.get().to_dict()

        voter_doc_dict['was_sent_postcard'] = True
        voter_doc_ref.set(voter_doc_dict)

        return Voter.from_dict(voter_doc_dict)
