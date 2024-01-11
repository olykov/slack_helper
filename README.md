# slack_helper

slack_helper will update your Slack status and DND (do not disturb) settings based on your shecdule.

---

[Docker image](https://hub.docker.com/repository/docker/lexusobm/slack_helper/general)

### Build

- `docker build -t slack_helper:tag .` Build an image
- `docker login -u="${DOCKER_USERNAME}" -p="${DOCKER_PASSWORD}"` Login to docker hub
- `docker image tag slack_helper:tag accountname/slack_helper:tag` Tag image
- `docker push accountname/slack_helper:tag` Push to dockerhub

### Run

- Specify the `SLACK_USER_ID` and `SLACK_BOT_TOKEN` env variables
- `docker-compose up -d` Up
