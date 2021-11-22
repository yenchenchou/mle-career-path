docker run \
    -it \
    --rm \
    -d \
    --name leetcode-python \
    --mount type=bind,source="$(pwd)",target=/Career_Learning_Path \
    python:3.8.8