# python-rest-api-docker

steps to run the sample rest service on docker -

1. Clone the Repository - git clone https://github.com/nanic/python-rest-api-docker.git

2. Move to the directory - cd python-rest-api-docker

3. Build the docker image - docker build -t python-rest .

4. Create and run a container - docker run -d -p 5000:5000 python-rest

5. Navigate to localhost:5000 to get hello world'd

6. Curl Befehl:
      curl -X POST http://localhost:5000/v1/api -H "Content-Type: application/json" -d '{"name": "naren"}