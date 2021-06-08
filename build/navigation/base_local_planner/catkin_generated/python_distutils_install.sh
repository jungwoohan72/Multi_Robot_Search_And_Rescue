#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/morin-sol/ME652/src/navigation/base_local_planner"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/morin-sol/ME652/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/morin-sol/ME652/install/lib/python2.7/dist-packages:/home/morin-sol/ME652/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/morin-sol/ME652/build" \
    "/usr/bin/python2" \
    "/home/morin-sol/ME652/src/navigation/base_local_planner/setup.py" \
     \
    build --build-base "/home/morin-sol/ME652/build/navigation/base_local_planner" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/morin-sol/ME652/install" --install-scripts="/home/morin-sol/ME652/install/bin"
