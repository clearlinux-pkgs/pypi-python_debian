#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBBC17EBB1396F2F7 (stuart@debian.org)
#
Name     : pypi-python_debian
Version  : 0.1.44
Release  : 9
URL      : https://files.pythonhosted.org/packages/52/1e/971d6fc2f9da72155314b3130643198e4f0c029f6e8a8ae040a45e072d44/python-debian-0.1.44.tar.gz
Source0  : https://files.pythonhosted.org/packages/52/1e/971d6fc2f9da72155314b3130643198e4f0c029f6e8a8ae040a45e072d44/python-debian-0.1.44.tar.gz
Source1  : https://files.pythonhosted.org/packages/52/1e/971d6fc2f9da72155314b3130643198e4f0c029f6e8a8ae040a45e072d44/python-debian-0.1.44.tar.gz.asc
Summary  : Debian package related modules
Group    : Development/Tools
License  : GPL-2.0+
Requires: pypi-python_debian-python = %{version}-%{release}
Requires: pypi-python_debian-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(chardet)

%description
The `debian` Python modules work with Debian-related data formats,
providing a means to read data from files involved in Debian packaging,
and the distribution of Debian packages. The ability to create or edit
the files is also available for some formats.

%package python
Summary: python components for the pypi-python_debian package.
Group: Default
Requires: pypi-python_debian-python3 = %{version}-%{release}

%description python
python components for the pypi-python_debian package.


%package python3
Summary: python3 components for the pypi-python_debian package.
Group: Default
Requires: python3-core
Provides: pypi(python_debian)
Requires: pypi(chardet)

%description python3
python3 components for the pypi-python_debian package.


%prep
%setup -q -n python-debian-0.1.44
cd %{_builddir}/python-debian-0.1.44
pushd ..
cp -a python-debian-0.1.44 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656698655
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
