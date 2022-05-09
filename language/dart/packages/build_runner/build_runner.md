# build_runner

The build_runner package provides a concrete way of generating files using Dart code, outside of tools like pub. Unlike pub serve/build, files are always generated directly on disk, and rebuilds are incremental - inspired by tools such as Bazel.
