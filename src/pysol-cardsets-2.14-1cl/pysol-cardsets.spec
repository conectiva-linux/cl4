Summary: A collection of free cardsets adapted for use with PySol
Summary(pt_BR): Uma coleção de cartas de baralho para uso com o PySol
Summary(es): A collection of free cardsets adapted for use with PySol
Name: pysol-cardsets
Version: 2.14
Release: 1cl
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Copyright: GPL
Url: http://wildsau.idv.uni-linz.ac.at/mfx/pysol.html
Source: http://wildsau.idv.uni-linz.ac.at/mfx/download/%{name}-%{version}.tar.gz
Requires: pysol
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-root

%description
A collection of free cardsets adapted for use with PySol.
I'm distributing this as its own package because I want to
keep the main distribution reasonable small.

%description -l pt_BR
Uma coleção de cartas de baralho para uso com o PySol

%description -l es
A collection of free cardsets adapted for use with PySol.
I'm distributing this as its own package because I want to
keep the main distribution reasonable small.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/pysol
rm -rf data/cardset-standard
cp -a data/cardset-* $RPM_BUILD_ROOT/usr/share/pysol


%files
%defattr(-,root,root)
%doc COPYING NEWS README
/usr/share/pysol/cardset-*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun 09 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- updated to 2.14

* Sat Jun 05 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- initial package

