# Perform a hugo build and copy the generated files into an nginx image

# Check for recent versions/tags at https://hub.docker.com/r/klakegg/hugo/tags
FROM klakegg/hugo:0.104.3-ubuntu-onbuild AS build
# On run, the image automatically copies the context folder to /src and performs a hugo build to /target

FROM nginxinc/nginx-unprivileged:alpine
COPY --from=build /target /usr/share/nginx/html
