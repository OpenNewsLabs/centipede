import uuid
import boto
from boto.exception import S3ResponseError
from boto.s3.key import Key


BUCKET_NAME = 'centipede.codingnews.info'


class Uploader(object):
    def __init__(self, project_id=None):
        self.conn = boto.connect_s3()
        self.bucket = self._get_bucket()
        if project_id is None:
            self.project_id = str(uuid.uuid4())
        else:
            self.project_id = uuid

    def upload_bucket(self, files):
        for filename in files:
            self.upload(filename)
        return {
            'project_id': self.project_id,
            'files': files
        }

    def upload(self, filename):
        k = Key(self.bucket)
        k.key = self.project_id + "/" + filename
        k.set_contents_from_filename(filename)
        return filename

    def _get_bucket(self):
        try:
            bucket = self.conn.get_bucket(BUCKET_NAME)
        except S3ResponseError:
            bucket = self.conn.create_bucket(BUCKET_NAME)
        return bucket
