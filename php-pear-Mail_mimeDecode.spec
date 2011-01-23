%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_subclass	mimeDecode
%define		_status		stable
%define		_pearname	Mail_mimeDecode
Summary:	%{_pearname} - decode MIME messages
Summary(pl.UTF-8):	%{_pearname} - dekodowanie wiadomości MIME
Name:		php-pear-%{_pearname}
Version:	1.5.4
Release:	1
License:	BSD Style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	24cc3adf73ffaacc8bd52b92a2a77567
URL:		http://pear.php.net/package/Mail_mimeDecode/
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Mail_Mime > 1.4.0
Obsoletes:	php-pear-Mail_mimeDecode-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a class to deal with the decoding and interpreting of MIME
messages. This package used to be part of the Mail_Mime package, but
has been split off.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa pozwala na dekodowanie i analizę wiadomości MIME.
Funkcjonalność ta była częścią pakietu Mail_Mime, została jednak z
niego wydzielona.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# pear/tests/pearname/tests -> pear/tests/pearname
mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests

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