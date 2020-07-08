#! /bin/sh

if [ $# != 1 ]; then
    echo "usage: pullrpms-lte.sh IMAGE"
    exit 1
fi

image=$1

if [ -d packages ]; then
    echo "Deleting ./packages"
    rm -rf packages
fi
echo "Making ./packages directory"
mkdir -p packages

echo "Copy LTE rpms from $image to ./packages..."

docker run -u root --entrypoint=/bin/sh --rm -i -v $(pwd)/packages:/mnt $image <<COMMANDS
cp /opt/emane-model-lte/.rpmbuild/RPMS/x86_64/emane-model-lte*rpm /mnt
cp /opt/srsLTE/build/srslte-emane*rpm /mnt
cp /opt/opentestpoint-probe-lte/.rpmbuild/RPMS/noarch/opentestpoint-probe-lte*rpm /mnt
COMMANDS

