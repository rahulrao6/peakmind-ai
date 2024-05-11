from datetime import timedelta
import traceback
from couchbase.exceptions import CouchbaseException
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster, ClusterOptions
from .config import (COUCHBASE_ENDPOINT, COUCHBASE_USERNAME, COUCHBASE_PASSWORD,
                     COUCHBASE_BUCKET, COUCHBASE_SCOPE, COUCHBASE_COLLECTION)

def connect_to_cluster():
    """Establishes connection to the Couchbase cluster."""
    auth = PasswordAuthenticator(COUCHBASE_USERNAME, COUCHBASE_PASSWORD)
    options = ClusterOptions(auth)
    options.apply_profile("wan_development")
    cluster = Cluster(f'couchbases://{COUCHBASE_ENDPOINT}', options)
    cluster.wait_until_ready(timedelta(seconds=5))
    return cluster

def perform_document_operations():
    """Performs basic document operations like insert, get, replace, and remove."""
    try:
        cluster = connect_to_cluster()
        cb = cluster.bucket(COUCHBASE_BUCKET)
        cb_coll = cb.scope(COUCHBASE_SCOPE).collection(COUCHBASE_COLLECTION)

        # Key for the document
        key = "airline_8091"
        sample_airline = {
            "type": "airline",
            "id": 8091,
            "callsign": "CBS",
            "iata": None,
            "icao": None,
            "name": "Couchbase Airways",
        }

        # Insert a new document
        try:
            result = cb_coll.insert(key, sample_airline)
            print("\nCreate document success. CAS: ", result.cas)
        except CouchbaseException as e:
            print("Error during document insert:", e)

        # Retrieve a document
        try:
            result = cb_coll.get(key)
            print("\nFetch document success. Result: ", result.content_as[dict])
        except CouchbaseException as e:
            print("Error during document fetch:", e)

        # Update a document
        try:
            sample_airline["name"] = "Couchbase Airways Updated"
            result = cb_coll.replace(key, sample_airline)
            print("\nUpdate document success. CAS: ", result.cas)
        except CouchbaseException as e:
            print("Error during document update:", e)

        # Delete a document
        try:
            result = cb_coll.remove(key)
            print("\nDelete document success. CAS: ", result.cas)
        except CouchbaseException as e:
            print("Error during document removal:", e)

    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()

# To run the operations
if __name__ == "__main__":
    perform_document_operations()
