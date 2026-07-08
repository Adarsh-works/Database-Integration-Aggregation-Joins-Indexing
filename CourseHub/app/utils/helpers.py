def serialize_doc(document):
    if document:
        document["id"] = str(document.pop("_id"))
    return document

def serialize_docs(documents):
    return [serialize_doc(doc) for doc in documents]