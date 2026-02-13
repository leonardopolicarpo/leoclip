# Maintainer: Leonardo Policarpo <https://github.com/leonardopolicarpo>
pkgname=leoclip
pkgver=0.2.0
pkgrel=1
pkgdesc="A minimalist, multimedia clipboard manager for i3wm built with Python & SQLite."
arch=('any')
url="https://github.com/leonardopolicarpo/leoclip"
license=('MIT')
depends=('python' 'xclip' 'rofi' 'scrot')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('SKIP')

build() {
  cd "$pkgname-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$pkgname-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}