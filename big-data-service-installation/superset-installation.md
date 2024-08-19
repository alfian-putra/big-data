## Superset Docker Installation

### Requirement :

- fedora 40
- python 3.12
- Docker
- Docker-compose
- git

### Step :
1. clone superset git
    ```
    git clone https://github.com/apache/superset.git
    ```

2. Set TALISMAN_ENABLED config to false in docker file configuration :
    ```
    vi docker-compose-non-dev.yml


    superset:
        env_file: docker/.env-non-dev
        image: *superset-image
        container_name: superset_app
        command: ["/app/docker/docker-bootstrap.sh", "app-gunicorn"]
        user: "root"
        restart: unless-stopped
        ports:
        - 8088:8088
        depends_on: *superset-depends-on
        volumes: *superset-volumes
        environment:
        - TALISMAN_ENABLED=false

    ```
3. run the following command to start superset
    ```
    git checkout 3.0.0
    TAG=3.0.0 docker-compose -f docker-compose-non-dev.yml up
    ```