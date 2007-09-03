%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_subclass	mimeDecode
%define		_status		stable
%define		_pearname	Mail_mimeDecode
Summary:	%{_pearname} - decode MIME messages
Summary(pl.UTF-8):	%{_pearname} - dekodowanie wiadomości MIME
Name:		php-pear-%{_pearname}
Version:	1.5.0
Release:	1
License:	BSD Style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e81f99c951eb5f199caa9dcd9c16f97f
URL:		http://pear.php.net/package/Mail_mimeDecode/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Mail_Mime >= 1.4.0
Requires:	php-pear-PEAR >= 1.6.0
Conflicts:	php-pear-Mail_Mime = 1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a class to deal with the decoding and interpreting of MIME
messages. This package used to be part of the Mail_Mime package, but
has been split off.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa ta dotarcza sposobu na decodowanie i analizę wiadomości MIME.
Funkcjonalność ta była częścią pakietu Mail_Mime, została jednak z
niego wydzielona.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Mail/mimeDecode.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Mail_mimeDecode/tests/parse_header_value.phpt
%{php_pear_dir}/tests/Mail_mimeDecode/tests/semicolon_content_type_bug1724.phpt
