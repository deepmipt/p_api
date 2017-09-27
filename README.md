# Paraphraser REST microservice
```sh
docker run --rm -d -h p_api.local                                     \
           --name p_api                                               \
           -p 5000:80                                                 \
           -e "AMQP_URI=amqp://user:password@host"                    \
            seliverstov/p_api:latest
```
