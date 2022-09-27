## Grouprr
#### Plex library access groups made simple
----------------------------------------

### What is this?

Grouparr is simple set of tools to help manage large groups of Plex users as groups. This can be very helpful if you have libraries that you only want a certain subset of people to have access to, like home movies. You can easily share those films with family, while restricting access to friends and other people on your server.

### What's the tech stack

The stack will be pretty simple. We will be using Django for the backend and [PlexAPI](https://pypi.org/project/PlexAPI/) for authentication and making changes on the server. In the future we may want to spruce up the front-end with some React magic, but for now I want to keep this tool simple (from an engineering standpoint).

### TODO:
- [X] Create concept to successfully update a user's library access
- [X] Setup Django project
- [ ] Setup mock DB to test against (with stubbed API endpoints)
- [ ] Design and configure frontend
- [ ] design and configure production level DB
- [ ] Setup authentication through Plex SSO
- [ ] Add job to refresh user and library tables from Plex server
- [ ] Figure out and implement way to get section access list for each user
- [ ] Create permission groups
- [ ] Create job to sync permission groups only on request (when button clicked)
- [X] Dockerize project for easy deployment on common Plex Server hardware (NAS, RaspberryPi, etc)

### Potential additional features
- [ ] Manage multiple Plex servers
- [ ] Integration with Overseerr

### Git Flow
To contribute to this project, please open a PR against the `dev` branch. This will act as a staging/beta branch. Once approved and merged, it will eventually make it's way into the `master` branch. This will serve as the production branch. When a build is successful on the `master` branch, it should be down-merged to the `dev` branch.

### Notes
- [Django/Docker guide used](https://docs.docker.com/samples/django/)
    - Build command
        - `sudo docker-compose run web django-admin startproject grouprr .`
    - Start project
        - `docker-compose up`
