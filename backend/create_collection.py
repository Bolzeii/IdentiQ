from config import rekognition, COLLECTION_ID


def create_collection():

    try:

        response = rekognition.create_collection(
            CollectionId=COLLECTION_ID
        )

        print("Collection Created")
        print(response)

    except rekognition.exceptions.ResourceAlreadyExistsException:

        print("Collection Already Exists")


if __name__ == "__main__":
    create_collection()