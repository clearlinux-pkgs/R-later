#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-later
Version  : 1.2.0
Release  : 34
URL      : https://cran.r-project.org/src/contrib/later_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/later_1.2.0.tar.gz
Summary  : Utilities for Scheduling Functions to Execute Later with Event
Group    : Development/Tools
License  : MIT Zlib
Requires: R-later-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-rlang
BuildRequires : R-Rcpp
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
time, after the R execution stack has emptied. The functions are scheduled
    in an event loop.

%package lib
Summary: lib components for the R-later package.
Group: Libraries

%description lib
lib components for the R-later package.


%prep
%setup -q -c -n later
cd %{_builddir}/later

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619204461

%install
export SOURCE_DATE_EPOCH=1619204461
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library later
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library later
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library later
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc later || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/later/DESCRIPTION
/usr/lib64/R/library/later/INDEX
/usr/lib64/R/library/later/LICENSE
/usr/lib64/R/library/later/Meta/Rd.rds
/usr/lib64/R/library/later/Meta/features.rds
/usr/lib64/R/library/later/Meta/hsearch.rds
/usr/lib64/R/library/later/Meta/links.rds
/usr/lib64/R/library/later/Meta/nsInfo.rds
/usr/lib64/R/library/later/Meta/package.rds
/usr/lib64/R/library/later/Meta/vignette.rds
/usr/lib64/R/library/later/NAMESPACE
/usr/lib64/R/library/later/NEWS.md
/usr/lib64/R/library/later/R/later
/usr/lib64/R/library/later/R/later.rdb
/usr/lib64/R/library/later/R/later.rdx
/usr/lib64/R/library/later/bgtest.cpp
/usr/lib64/R/library/later/doc/index.html
/usr/lib64/R/library/later/doc/later-cpp.Rmd
/usr/lib64/R/library/later/doc/later-cpp.html
/usr/lib64/R/library/later/help/AnIndex
/usr/lib64/R/library/later/help/aliases.rds
/usr/lib64/R/library/later/help/later.rdb
/usr/lib64/R/library/later/help/later.rdx
/usr/lib64/R/library/later/help/paths.rds
/usr/lib64/R/library/later/html/00Index.html
/usr/lib64/R/library/later/html/R.css
/usr/lib64/R/library/later/include/later.h
/usr/lib64/R/library/later/include/later_api.h
/usr/lib64/R/library/later/tests/testthat.R
/usr/lib64/R/library/later/tests/testthat/test-c-api.R
/usr/lib64/R/library/later/tests/testthat/test-cancel.R
/usr/lib64/R/library/later/tests/testthat/test-private-loops.R
/usr/lib64/R/library/later/tests/testthat/test-run_now.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/later/libs/later.so
