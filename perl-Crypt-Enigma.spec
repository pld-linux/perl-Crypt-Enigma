%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Enigma
Summary:	Crypt::Enigma Perl module - WWII Enigma Machine implementation
Summary(pl):	Modu³ Perla Crypt::Enigma - implementacja maszyny Enigma z IIW¦
Name:		perl-Crypt-Enigma
Version:	1.3
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a complete working Perl implementation of the Enigma
Machine used during World War II. The cipher calculations are based on
actual Enigma values and the resulting ciphered values are as would be
expected from an Enigma Machine.

%description -l pl
Ten modu³ jest pe³n± implementacj± w Perlu maszyny szyfruj±cej Enigma,
u¿ywanej w czasie II Wojny ¦wiatowej. Obliczenia szyfru bazuj± na
prawdziwych warto¶ciach wziêtych z enigmy i daj± wyniki takie, jakie
powinna daæ maszyna.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
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
%{perl_sitelib}/Crypt/Enigma.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
