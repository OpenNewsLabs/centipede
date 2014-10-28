# API documentation for centilope

## Projects

A project is a container for documents. It has a **name** and a **collection** of documents. Every bulk operation on documents will need a project.

    curl --data "name=project_name" -F filedata=@document_1.pdf -F filedata=@document_2.pdf http://centilope.org/api/v1/projects

    POST /api/v1/projects with a project name and the files

Response:

```json
{
    "project": {
        "name": "project_name",
        "size": 2
        ...
    },
    "status": "OK"
}
```
