%define kdeprefix /usr
%define version 1.1.1
%define kderelease 3cl
%define sourcedir stable/1.1.1/distribution/tar/generic/source

%define conectiva versão-conectiva >= 4.0
%define qtversion qt >= 1.42

%define kdename kdemultimedia
Name: %{kdename}
Summary: K Desktop Environment - Multimedia Applications
Summary(pt_BR): K Desktop Environment - aplicações multimídia 
Summary(es): K Desktop Environment - aplicaciones multimedia 
Version: %{version}
Release: %{kderelease}
Source: ftp://ftp.kde.org:/pub/kde/%{sourcedir}/%{kdename}-%{version}.tar.bz2
Patch: kdemultimedia-%{version}-redhat.patch
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
BuildRoot: /var/tmp/%{kdename}-buildroot
Copyright: GPL/Artistic
Requires: %{qtversion} %{conectiva}
Prefix: %{kdeprefix}
Obsoletes: kde-multimedia

%description
Multimedia applications for the K Desktop Environment.
Included: kmedia (media player); kmid (midi/karaoke player);
kmidi (midi-to-wav player/converter); kmix (mixer); kscd (CD audio player) 

%description -l pt_BR
Aplicações multimídia para o KDE.

Incluídos neste pacote:


kmedia: ferramenta para tocar multimídias kmid: tocador de
midi/karaoke kmidi: tocador/conversor de midi para wav kmix:
ferramenta mixer kscd: tocador CD de áudio

%description -l es
Aplicaciones multimedia para KDE.  Incluidos en este paquete: kmedia:
herramienta para tocar multimedias kmid: tocador de midi/karaoke
kmidi: tocador/conversor de midi para wav kmix: herramienta mixer
kscd: tocador CD de audio

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n kdemultimedia-%{version}

%patch -p1

%build
[ "$LINGUAS" ] && unset LINGUAS
export KDEDIR=%{kdeprefix}
./configure --prefix=%{kdeprefix}  \
	--with-install-root=$RPM_BUILD_ROOT
make CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti"

%install
make install-strip

cd $RPM_BUILD_ROOT
find . -type d | grep -v "\/usr\/share\/locale" | \
	sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
	$RPM_BUILD_DIR/file.list.%{kdename}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
	-e '/\/config\//s|^|%config|' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{kdename}
rm -rf $RPM_BUILD_DIR/%{kdename}-%{version}

%files -f ../file.list.%{kdename}

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 05 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- requires versão-conectiva >= 4.0 (glibc 2.1, etc)
- fixed specfile wrt rpm 3.0

* Fri May 07 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Updated to 1.1.1

* Sat Apr 03 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed CONFIG_FILE for kmidi (reported by miura@conectiva.com)
- Obsoletes kde-multimedia: thanx to the upgrade from parolin test... ;>

* Thu Mar 25 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed requires
- unset LINGUAS

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Mar 06 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- %dir /usr/share/locale removed from %filelist

* Fri Feb 26 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Compiled with -fno-exceptions -fno-rtti
- Added postinstall script for kappfinder and wmconfig

* Tue Jan 19 1999 Conectiva <dist@conectiva.com>
- Added pt_BR translations

* Wed Jan 06 1999 Preston Brown <pbrown@redhat.com>
- re-merged in updates from Duncan Haldane
