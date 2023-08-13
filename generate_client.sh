#!/usr/bin/env bash

REPO="openziti/edge-api"
CONTAINER_TAG="v6.6.0"

function _generate {
    local tag="$1"
    
    echo "Generating client for tag: $tag"
    docker run \
        --cap-add ALL \
        --rm \
        --volume "${PWD}":/out:Z \
        docker.io/openapitools/openapi-generator-cli:$CONTAINER_TAG generate \
        --generator-name python-prior \
        --git-host 'github.com' \
        --git-repo-id 'openziti-edge-management-python' \
        --git-user-id 'openziti-test-kitchen' \
        --input-spec "https://raw.githubusercontent.com/$REPO/$tag/management.yml" \
        --output '/out' \
        --package-name 'openziti_edge_management' \
        --additional-properties=packageVersion="${tag#v}" \
        --additional-properties=packageUrl="https://github.com/openziti-test-kitchen/openziti-edge-management-python"
}

function _get_latest_tag {
    curl -sSL "https://api.github.com/repos/$REPO/tags" \
        | jq -r '[.[] | select(.name | startswith("v")) | .name][0]'
}

function _test_tag_exists {
    local tag="$1"
    local tags="$(curl -sSL "https://api.github.com/repos/$REPO/tags")"
    if ! jq --arg tag "$tag" '[.[] | select(.name == $tag)][0] or error("err")' <<< "$tags" &> /dev/null; then
        echo "Tag does not exist: $tag" >&2
        echo "Valid tags are:"
        jq -r '.[].name' <<< "$tags"
        exit 1
    fi
}

function local_modify {
    echo "tags" >> .gitignore
}

function _usage {
    echo "usage: ./generate_client.sh v0.24.83" >&2
}

function _main {
    local tag
    if [ -z "$1" ]; then
        tag="$(_get_latest_tag)"
    else
        tag="$1"
        if ! [[ "$tag" =~ ^v([0-9]+\.){2}[0-9]+ ]]; then
            echo "Tag is not a valid version" >&2
            _usage
            exit 1
        fi
        _test_tag_exists "$tag"
    fi
    _generate "$tag"

    local_modify
}

_main "$@"
