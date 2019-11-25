STATES := app tests
REPO := tarasshynkler/firstrepos

.PHONY: $(STATES)

$(STATES):
	@docker build -f Dockerfile.$(@) -t $(REPO):$(@) .

run:
	@docker network create --driver=bridge appnet \
	&& docker run --rm --name redis --net=appnet -d redis \
	&& docker run --rm -it --name app --net=appnet -p -d 5000:5000 $(REPO):app

test-app:
	@docker run --rm -it --name test --net=appnet $(REPO):tests

docker-prune:
	@docker rm $$(docker ps -a -q) --force || true \
	&& docker container prune --force \
	&& docker volume prune --force \
	&& docker network prune --force \
	&& docker image prune --force

push:
	@docker push $(REPO):app
	@docker push $(REPO):tests

deleteimages:
	@docker image prune -a --force