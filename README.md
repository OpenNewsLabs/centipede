
pipeline transforms

* http get
* entity extraction
* text extraction 
* html cleaning 
* language / encoding detection
* scoring 
* elasticsearch indexing 
* filtering
* aggregation (?) / reduce


Metadata: superset of http://dublincore.org/documents/dcmi-terms/ 



HTTP API: transform (sync)
    
    POST (json) -> (magic) -> (json) --> either metadata AND status message


{
    "document": {
        ... 
    },
    "status": {

    }
}


{
    "documents": [
        {"..."}
    ]
}


LOADER Service

    POST /api/post-file ...
    POST /api/post-url ... 

    GET /api/collections/<collection_id>
        -> existing metadata 
        -> a link to an S3 file

    POST /api/collection/<collection_id>/<document_id>




pipeline orchestrator 

    * define a pipeline 
    * define source documents
    * run jobs and monitor progress
