#!/bin/bash

set -o errexit

GIT_REPO=git@github.com:ego/cartoonart.git
MAINLINE_BRANCH=main

echo
echo "Fetching updates ..."
git fetch --tags --all

LAST_TAG=`git describe --tags $(git rev-list --tags --max-count=1)`
VERSION_BITS=(${LAST_TAG//./ })
VNUM1=${VERSION_BITS[0]}
VNUM2=${VERSION_BITS[1]}
VNUM3=${VERSION_BITS[2]}

set +o errexit
MAJOR=`git log --format=%B -n 1 HEAD | grep '#major'`
MINOR=`git log --format=%B -n 1 HEAD | grep '#minor'`
set -o errexit

if [ "$MAJOR" ]; then
    VNUM1=$((VNUM1+1))
    VNUM2=0
    VNUM3=0
    echo "New major version $VNUM1"
elif [ "$MINOR" ]; then
    VNUM2=$((VNUM2+1))
    VNUM3=0
    echo "New minor version $VNUM2"
else
    VNUM3=$((VNUM3+1))
    echo "New patch version $VNUM3"
fi
NEW_TAG="$VNUM1.$VNUM2.$VNUM3"

echo
echo "Last tag is $LAST_TAG creating new tag $NEW_TAG ..."
git tag $NEW_TAG

echo
echo "Pushing branch $MAINLINE_BRANCH and new tag $NEW_TAG..."
git push --force-with-lease --atomic origin $MAINLINE_BRANCH $NEW_TAG

echo
echo "Release done."
