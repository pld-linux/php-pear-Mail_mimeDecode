%define		pearname	Mail_mimeDecode
Summary:	%{pearname} - decode MIME messages
Summary(pl.UTF-8):	%{pearname} - dekodowanie wiadomości MIME
Name:		php-pear-%{pearname}
Version:	1.5.6
Release:	1
License:	BSD Style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	a2d64cf970cb869ac034493ce6fa53d0
URL:		http://pear.php.net/package/Mail_mimeDecode/
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php-pear
Requires:	php-pear-Mail_Mime > 1.4.0
Obsoletes:	php-pear-Mail_mimeDecode-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a class to deal with the decoding and interpreting of MIME
messages. This package used to be part of the Mail_Mime package, but
has been split off.

%description -l pl.UTF-8
Ta klasa pozwala na dekodowanie i analizę wiadomości MIME.
Funkcjonalność ta była częścią pakietu Mail_Mime, została jednak z
niego wydzielona.

%prep
%pear_package_setup

# pear/tests/pearname/tests -> pear/tests/pearname
mv ./%{php_pear_dir}/tests/%{pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{pearname}/tests

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# not used by this package
%{__rm} $RPM_BUILD_ROOT%{php_pear_dir}/data/Mail_mimeDecode/xmail.dtd
%{__rm} $RPM_BUILD_ROOT%{php_pear_dir}/data/Mail_mimeDecode/xmail.xsl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Mail/mimeDecode.php
