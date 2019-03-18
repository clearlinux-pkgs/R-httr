#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-httr
Version  : 1.4.0
Release  : 74
URL      : https://cran.r-project.org/src/contrib/httr_1.4.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/httr_1.4.0.tar.gz
Summary  : Tools for Working with URLs and HTTP
Group    : Development/Tools
License  : MIT
Requires: R-cli
BuildRequires : R-bitops
BuildRequires : R-cli
BuildRequires : R-curl
BuildRequires : R-httpuv
BuildRequires : R-jsonlite
BuildRequires : R-knitr
BuildRequires : R-mime
BuildRequires : R-openssl
BuildRequires : R-png
BuildRequires : R-withr
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
# httr
<!-- badges: start -->
[![Travis build status](https://travis-ci.org/r-lib/httr.svg?branch=master)](https://travis-ci.org/r-lib/httr)
[![Codecov test coverage](https://codecov.io/gh/r-lib/httr/branch/master/graph/badge.svg)](https://codecov.io/gh/r-lib/httr?branch=master)
[![CRAN status](https://www.r-pkg.org/badges/version/httr)](https://cran.r-project.org/package=httr)
<!-- badges: end -->

%prep
%setup -q -c -n httr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552893880

%install
export SOURCE_DATE_EPOCH=1552893880
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library httr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library httr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library httr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  httr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/httr/DESCRIPTION
/usr/lib64/R/library/httr/INDEX
/usr/lib64/R/library/httr/LICENSE
/usr/lib64/R/library/httr/Meta/Rd.rds
/usr/lib64/R/library/httr/Meta/demo.rds
/usr/lib64/R/library/httr/Meta/features.rds
/usr/lib64/R/library/httr/Meta/hsearch.rds
/usr/lib64/R/library/httr/Meta/links.rds
/usr/lib64/R/library/httr/Meta/nsInfo.rds
/usr/lib64/R/library/httr/Meta/package.rds
/usr/lib64/R/library/httr/Meta/vignette.rds
/usr/lib64/R/library/httr/NAMESPACE
/usr/lib64/R/library/httr/NEWS.md
/usr/lib64/R/library/httr/R/httr
/usr/lib64/R/library/httr/R/httr.rdb
/usr/lib64/R/library/httr/R/httr.rdx
/usr/lib64/R/library/httr/demo/connection-sharing.r
/usr/lib64/R/library/httr/demo/oauth1-nounproject.r
/usr/lib64/R/library/httr/demo/oauth1-twitter.r
/usr/lib64/R/library/httr/demo/oauth1-withings.r
/usr/lib64/R/library/httr/demo/oauth1-yahoo.r
/usr/lib64/R/library/httr/demo/oauth2-azure.r
/usr/lib64/R/library/httr/demo/oauth2-facebook.r
/usr/lib64/R/library/httr/demo/oauth2-github.r
/usr/lib64/R/library/httr/demo/oauth2-google.r
/usr/lib64/R/library/httr/demo/oauth2-linkedin.r
/usr/lib64/R/library/httr/demo/oauth2-reddit.R
/usr/lib64/R/library/httr/demo/oauth2-vimeo.r
/usr/lib64/R/library/httr/demo/oauth2-yahoo.r
/usr/lib64/R/library/httr/demo/oauth2-yelp.R
/usr/lib64/R/library/httr/demo/service-account.R
/usr/lib64/R/library/httr/doc/api-packages.R
/usr/lib64/R/library/httr/doc/api-packages.Rmd
/usr/lib64/R/library/httr/doc/api-packages.html
/usr/lib64/R/library/httr/doc/index.html
/usr/lib64/R/library/httr/doc/quickstart.R
/usr/lib64/R/library/httr/doc/quickstart.Rmd
/usr/lib64/R/library/httr/doc/quickstart.html
/usr/lib64/R/library/httr/doc/secrets.R
/usr/lib64/R/library/httr/doc/secrets.Rmd
/usr/lib64/R/library/httr/doc/secrets.html
/usr/lib64/R/library/httr/help/AnIndex
/usr/lib64/R/library/httr/help/aliases.rds
/usr/lib64/R/library/httr/help/httr.rdb
/usr/lib64/R/library/httr/help/httr.rdx
/usr/lib64/R/library/httr/help/paths.rds
/usr/lib64/R/library/httr/html/00Index.html
/usr/lib64/R/library/httr/html/R.css
/usr/lib64/R/library/httr/tests/testthat.R
/usr/lib64/R/library/httr/tests/testthat/data.txt
/usr/lib64/R/library/httr/tests/testthat/test-body.r
/usr/lib64/R/library/httr/tests/testthat/test-callback.R
/usr/lib64/R/library/httr/tests/testthat/test-config.r
/usr/lib64/R/library/httr/tests/testthat/test-content-parse.r
/usr/lib64/R/library/httr/tests/testthat/test-content.R
/usr/lib64/R/library/httr/tests/testthat/test-header.r
/usr/lib64/R/library/httr/tests/testthat/test-http-condition.R
/usr/lib64/R/library/httr/tests/testthat/test-http-error.R
/usr/lib64/R/library/httr/tests/testthat/test-http-head.r
/usr/lib64/R/library/httr/tests/testthat/test-oauth-cache.R
/usr/lib64/R/library/httr/tests/testthat/test-oauth-server-side.R
/usr/lib64/R/library/httr/tests/testthat/test-oauth.R
/usr/lib64/R/library/httr/tests/testthat/test-oauth_signature.R
/usr/lib64/R/library/httr/tests/testthat/test-parse_media.R
/usr/lib64/R/library/httr/tests/testthat/test-request.r
/usr/lib64/R/library/httr/tests/testthat/test-response.r
/usr/lib64/R/library/httr/tests/testthat/test-retry.R
/usr/lib64/R/library/httr/tests/testthat/test-ssl.R
/usr/lib64/R/library/httr/tests/testthat/test-url.r
