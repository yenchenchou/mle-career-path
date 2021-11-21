docker run \
    -it \
    --rm \
    -d \
    --name leetcode-python \
    --mount type=bind,source="$(pwd)",target=/DataStructure_Algorithm \
    python:3.8.8