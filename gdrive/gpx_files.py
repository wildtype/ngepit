from io import BytesIO, StringIO
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

class GpxFiles:
    '''Gdrive client, specific for this project, listing gpx files in my drive'''

    def __init__(self):
        credentials = GoogleCredentials.get_application_default()
        self.gdrive_client = build('drive', 'v3', credentials=credentials)
        self.files = self._download_all()

    def __getitem__(self, index):
        return self.files[index]

    def _files(self):
        return self.gdrive_client.files()

    def _fetch_file_ids(self):
        '''return fileIds of gpx files'''

        query = "mimeType = 'text/xml'"
        results = self._files().list(q=query).execute()

        return [file['id'] for file in results['files']]

    def _download_file(self, file_id):
        '''Return StringIO of file content, UTF-8 decoded'''

        file_in_gdrive = self._files().get_media(fileId=file_id)
        file_content = BytesIO()

        downloader = MediaIoBaseDownload(file_content, file_in_gdrive)
        done_downloading = False

        while not done_downloading:
            status, done_downloading = downloader.next_chunk()

        decoded_file_content = file_content.getvalue().decode('utf-8')
        return StringIO(decoded_file_content)


    def _download_all(self):
        file_ids = self._fetch_file_ids()
        files = []
        for file_ids in file_ids:
            files.append(self._download_file(file_ids))

        return files
