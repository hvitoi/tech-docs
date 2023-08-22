# makepkg

- Build user package in Archlinux
- Requires package `base-devel`

```shell
# Clone and install package from AUR
git clone "https://aur.archlinux.org/google-chrome.git"
cd "./google-chrome/"

# Build package (creates a *.pkg.tar.xz or *.pkg.tar.zst)
makepkg

# Install build dependencies & Build package
makepkg -s

# Install build dependencies & Build package & Install package
makepkg -si
makepkg -sircC # --syncdeps --install --rmdeps --clean  --cleanbuild

# Manually install a built package
pacman -U "pacote.pkg.tar.xz"

# No build
makepkg -od --skippgpcheck # --nobuild --nodeps --skippgpcheck
```

```shell
# Use all available cpus
export MAKEFLAGS=j$(nproc) && makepkg -s --noconfirm
```

## The build process

1. The sources are downloaded into the root level
1. The sources are unpacked into $srcdir
1. Prepare script is run
1. Package script is run (installs to $pkgdir)

## Variables

- `$srcdir`
  - ./src
  - Where the sources are unpacked to
- `$pkgdir`
  - ./pkg
  - Used as a fakeroot for building the package

## Import keys

- Or use `--skippgpcheck` to skip it

```shell
# Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
gpg --keyserver hkps://keys.openpgp.org --recv-keys 3B94A80E50A477C7

# Greg Kroah-Hartman <gregkh@linuxfoundation.org>
gpg --keyserver keyserver.ubuntu.com --recv-keys 38DBBDC86092693E
```

## Files

### Templates

- `PKGBUILD` templates can be found at `/usr/share/pacman`

  - `PKGBUILD-split.proto`: for a group of packages
  - `PKGBUILD-vcs.proto`: for versioning according to the latest commit
  - `PKGBUILD.proto`: for versioning a package
  - `proto.install`: pacman hooks for a package

- Remove the `.proto` when copying the template

### PKGBUILD

- A `PKGBUILD` file is just a shell script!
- Use `namcap` to sanity check your pkgbuild file

```shell
# Maintainer: Your Name <youremail@domain.com>
pkgbase="my-package-base" # (optional) used when a package is part of a collection of packages
pkgname="Henry" # name of the package. If a pkgbase is defined, then an array of package names ("a" "b" "c")
pkgver=1 # version of the application
pkgrel=1 # version of the aur package (version of this config file). Ideally use only integers
epoch=1 # force the package to be seen as new (avoid modifying it)
pkgdesc="My awesome package" # description of the package (less than 80 characters)
arch=("x86_64") # system architecture
url="https://github.com/a/b" # url of the official website application
license=('GPL') # license
groups=() # group to which this package belongs to
depends=("foobar>=1.8.0" "foobar<2.0.0" "pcre") # runtime dependencies
makedepends=("git") # build dependencies
checkdepends=() # test dependencies
optdepends=("cups: printing support"
            "sane: scanners support") # runtime optional dependencies
provides=("package") # the package provided by this build file. For when multiple packages provide the same software (e.g., lala, lala-git, lala-bin). If there is only one package, leave it empty
conflicts=() # example: lf, lf-git, lf-bin : the conflict with each other because they are the same
replaces=() # obsolete packages replaced by the package. E.g., wireshark-qt replaces wireshark
backup=("etc/pacman.conf") # backup of config files (e.g., /etc/pacman.conf) before the installation. These .bak files are restored when uninstalling the package
options=() # change the default behavior of make package (usually if it needs to be modified it is not done here, there are others ways to change this behavior)
install="mypackage.install" # reference to the pacman hook file (*.install)
changelog="CHANGELOG" # reference to the changelog file
source=("$pkgname-$pkgver.tar.gz"
        "$pkgname-$pkgver.patch") # download the source code
source=("awesome::git://github.com/hey/awesome.git") # source code from a git repo
source=("$pkgname-r$pkgver.tag.gz::https://github.com/gokcehan/$pkgname/archive/r$pkgver.tar.gz") # source code from a git archive
noextract=("test.rar") # files that shouldn't be downloaded from the source above
md5sums=("SKIP") # integrity checking. There is also sha1sums, sha256sums, sha224sums, sha384sums, sha124sums, b2sums. Makes sure the source files are actually the files you expect to be
validpgpkeys=() # An array of PGP fingerprints that might be necessary for the source code.

# change the package version number before compiling
pkgver() {
  cd "$pkgname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "(git rev-parse --short HEAD)"
}

# get ready to build the source code
prepare() {
  cd "$pkgname-$pkgver"
  patch -p1 -i "$srcdir/$pkgname-$pkgver.patch"
}

# compile the source code
build() {
  cd "$pkgname-$pkgver"
  ./configure --prefix=/usr
  make
}

# run the test suite
check() {
  cd "$pkgname-$pkgver"
  make -k check
}

# install the software
package() {
  cd "$pkgname-$pkgver"

  # install with "make"
  make DESTDIR="$pkgdir/" install

  # install with "install"
  install -Dm755 ./mybinary "$pkgdir/usr/bin/mybinary" # 755 for binary
  install -Dm644 ./README.md "$pkgdir/usr/share/doc/$pkgname" # 644 for documentation
}
```

### .install

- Defines pacman hooks for `installing`, `upgrading`, `removing` the package

```shell
# arg 1:  the new package version
pre_install() {
  do something here
}

# arg 1:  the new package version
post_install() {
  do something here
}

# arg 1:  the new package version
# arg 2:  the old package version
pre_upgrade() {
  do something here
}

# arg 1:  the new package version
# arg 2:  the old package version
post_upgrade() {
  do something here
}

# arg 1:  the old package version
pre_remove() {
  do something here
}

# arg 1:  the old package version
post_remove() {
  do something here
}
```
