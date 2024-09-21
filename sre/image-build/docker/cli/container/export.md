# export

- Export a container into a tarball

```shell
# export
docker export <container-id> > foo.tar

# extract
mkdir foo
tar -xvf foo.tar --directory foo/
```
