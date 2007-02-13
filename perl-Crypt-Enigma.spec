%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Enigma
Summary:	Crypt::Enigma Perl module - WWII Enigma Machine implementation
Summary(pl.UTF-8):	Moduł Perla Crypt::Enigma - implementacja maszyny Enigma z IIWŚ
Name:		perl-Crypt-Enigma
Version:	1.3
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	df345b5a952eb63ec37c1fc00776c9c8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a complete working Perl implementation of the Enigma
Machine used during World War II. The cipher calculations are based on
actual Enigma values and the resulting ciphered values are as would be
expected from an Enigma Machine.

%description -l pl.UTF-8
Ten moduł jest pełną implementacją w Perlu maszyny szyfrującej Enigma,
używanej w czasie II Wojny Światowej. Obliczenia szyfru bazują na
prawdziwych wartościach wziętych z enigmy i dają wyniki takie, jakie
powinna dać maszyna.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/Enigma.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
