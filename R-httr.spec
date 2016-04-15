#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-httr
Version  : 1.1.0
Release  : 24
URL      : http://cran.r-project.org/src/contrib/httr_1.1.0.tar.gz
Source0  : http://cran.r-project.org/src/contrib/httr_1.1.0.tar.gz
Summary  : Tools for Working with URLs and HTTP
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-jsonlite
Requires: R-openssl
Requires: R-curl
BuildRequires : R-R6
BuildRequires : R-bitops
BuildRequires : R-curl
BuildRequires : R-jsonlite
BuildRequires : R-knitr
BuildRequires : R-openssl
BuildRequires : clr-R-helpers

%description
# httr
[![Build Status](https://travis-ci.org/hadley/httr.png?branch=master)](https://travis-ci.org/hadley/httr)
[![Coverage Status](https://img.shields.io/codecov/c/github/hadley/httr/master.svg)](https://codecov.io/github/hadley/httr?branch=master)
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/httr)](http://cran.r-project.org/web/packages/httr)

%prep
%setup -q -c -n httr

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library httr
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library httr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/httr/DESCRIPTION
/usr/lib64/R/library/httr/INDEX
/usr/lib64/R/library/httr/LICENSE
/usr/lib64/R/library/httr/Meta/Rd.rds
/usr/lib64/R/library/httr/Meta/demo.rds
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
/usr/lib64/R/library/httr/demo/oauth1-twitter.r
/usr/lib64/R/library/httr/demo/oauth1-vimeo.r
/usr/lib64/R/library/httr/demo/oauth1-withings.r
/usr/lib64/R/library/httr/demo/oauth1-yahoo.r
/usr/lib64/R/library/httr/demo/oauth2-azure.r
/usr/lib64/R/library/httr/demo/oauth2-facebook.r
/usr/lib64/R/library/httr/demo/oauth2-github.r
/usr/lib64/R/library/httr/demo/oauth2-google.r
/usr/lib64/R/library/httr/demo/oauth2-linkedin.r
/usr/lib64/R/library/httr/demo/service-account.R
/usr/lib64/R/library/httr/doc/api-packages.R
/usr/lib64/R/library/httr/doc/api-packages.Rmd
/usr/lib64/R/library/httr/doc/api-packages.html
/usr/lib64/R/library/httr/doc/index.html
/usr/lib64/R/library/httr/doc/quickstart.R
/usr/lib64/R/library/httr/doc/quickstart.Rmd
/usr/lib64/R/library/httr/doc/quickstart.html
/usr/lib64/R/library/httr/help/AnIndex
/usr/lib64/R/library/httr/help/aliases.rds
/usr/lib64/R/library/httr/help/httr.rdb
/usr/lib64/R/library/httr/help/httr.rdx
/usr/lib64/R/library/httr/help/paths.rds
/usr/lib64/R/library/httr/html/00Index.html
/usr/lib64/R/library/httr/html/R.css
