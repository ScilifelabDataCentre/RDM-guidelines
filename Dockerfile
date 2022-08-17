# Perform a hugo build and copy the generated files into an nginx image

# Check for recent versions/tags at https://hub.docker.com/r/klakegg/hugo/tags
FROM klakegg/hugo:0.101.0-onbuild AS build
# On run, the image automatically copies the context folder to /src and performs a hugo build to /target

FROM nginx:alpine
COPY --from=build /target /usr/share/nginx/html
