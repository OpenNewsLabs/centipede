# Centipede

A centipede is a de-centralized pipeline for processing documents. It consists of many stages, which may perform tasks such as downloading files, extracting texts, detecting language and encoding or indexing a document to a search index.


## Components

Centipede processing stacks consist of a number of components, such as: 

* A document manager, which can store documents on S3
* A pipeline manager, which iterates over documents and executes each stage of the pipeline for each document. 
* A pipeline stage, i.e. a web service which receives a document from the pipeline manager and performs some operation on it.


### Examples of Pipeline Stages

* HTTP GET
* Language/Encoding detection
* Entity extraction
* Text extraction 
* HTML cleaning 
* Scoring 
* ElasticSearch indexing 
* Filtering
* Aggregation (?) / reduce

### What is the network protocol?

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
