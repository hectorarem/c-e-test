# c-e-test `InstaShare`

#### The frontend 
should be implemented with the latest stable version of the frontend technology specified by your job application. The frontend should be based on modern UI/UX principles and methodologies.

#### The backend 
should be implemented as an independent JSON-based Web service powered by a database or a distributed file system (DFS).

#### Description
Users of the website should be able to create an account and login with a previously created account.
Once logged in, the user should be able to upload a file that will be processed asynchronously by the backend. Once the file has been uploaded, the user can proceed with uploading more files, review the name, status and size of previously uploaded files, or change the name of a previously uploaded file.
Uploaded files are stored in a database or a distributed file system and a service job should pick up the file from the database / DFS, compress it with ZIP and reinsert it into the database / DFS. 
Once the file has been zipped, the user of the community site can download the file. 


## Frontend Project
<a href="https://github.com/hectorarem/c-e-test/tree/main/frontend/filemanagement">Frontend</a>
### Technologies
1. Node >= `6.0` (local uses `16.4`)
2. Angular `13.x`
3. ngx-toastr `14.x`
4. You can see more <a href="https://github.com/hectorarem/c-e-test/blob/main/frontend/filemanagement/package.json">here</a>
## Backend Project
<a href="https://github.com/hectorarem/c-e-test/tree/main/backend">Backend</a>
### Technologies
1. Python >= `3.7` (local and server uses `3.9`)
2. Django `4.0.4`
3. Django Rest Framework `3.13.x`
4. You can see more <a href="https://github.com/hectorarem/c-e-test/blob/main/backend/requirements.txt">here</a>

### GitHub Kanban

<a href="https://github.com/hectorarem/c-e-test/projects/1">KANBAN</a>