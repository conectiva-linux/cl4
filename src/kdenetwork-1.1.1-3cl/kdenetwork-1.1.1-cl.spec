%define kdeprefix /usr
%define version 1.1.1
%define kderelease 3cl
%define sourcedir stable/1.1.1/distribution/tar/generic/source

%define conectiva versão-conectiva >= 4.0
%define qtversion qt >= 1.42

%define kdename kdenetwork 
%define ktalk ktalk-0.2.7
Name: %{kdename}
Summary: K Desktop Environment - Network Applications
Summary(pt_BR): K Desktop Environment - aplicações de rede
Summary(es): K Desktop Environment - aplicaciones de red
Version: %{version}
Release: %{kderelease}
Source: ftp://ftp.kde.org/pub/kde/%{sourcedir}/%{kdename}-%{version}.tar.bz2
Source1: ftp://ftp.kde.org/pub/kde/stable/1.1/apps/network/%{ktalk}.tar.bz2
Patch: kdenetwork-%{version}-ktalkd.patch
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
BuildRoot: /var/tmp/%{kdename}-buildroot
Copyright: GPL
Requires: %{qtversion} %{conectiva} kdesupport
Prefix: %{kdeprefix}
Obsoletes: kde-network

%description
Network applications for the K Desktop Environment. 

Includes:
kbiff (mail delivery notification)
kfinger ("finger" utility)
kmail (mail client)
knu (network utilities)
korn  (mailbox monitor tool)
kppp (easy PPP connection configuration)
krn (news reader); ktalkd (talk daemon)
The talk client %{ktalk} is also added to this package.

%description -l pt_BR
Aplicações de Rede para o KDE.

Incluídos neste pacote:

kmail: leitor de correio knu: utilitários de rede korn: ferramenta
de monitoração da caixa de correio kppp: configuração fácil para
conexão PPP krn: leitor de notícias

%description -l es
Aplicaciones de Red para KDE.  Incluidos en este paquete: kmail:
lector de correo knu: utilitarios de red korn: herramienta de
monitoración de la caja de correo kppp: configuración fácil para
conexión PPP krn: lector de noticias

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n kdenetwork-%{version}
%patch -p1

%setup -q  -T  -n %{ktalk} -b 1

%build

export KDEDIR=%{kdeprefix}
[ "$LINGUAS" ] && unset LINGUAS

#será que dessa vez funciona?
#rm -rf karchie

# compile main package
cd $RPM_BUILD_DIR/%{kdename}-%{version}
    CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS -frtti -fexceptions" \
    ./configure \
    --prefix=%{kdeprefix} --with-install-root=$RPM_BUILD_ROOT
make

# compile ktalk
cd $RPM_BUILD_DIR/%{ktalk}
./configure --prefix=%{kdeprefix}
make

%install
export KDEDIR=%{kdeprefix}
cd $RPM_BUILD_DIR/%{kdename}-%{version}
make install-strip prefix=$RPM_BUILD_ROOT%{kdeprefix}
cd $RPM_BUILD_DIR/%{ktalk}
make install-strip prefix=$RPM_BUILD_ROOT%{kdeprefix}

# Remove suid bit from kppp
chmod 755 $RPM_BUILD_ROOT%{kdeprefix}/bin/kppp

# fix library permisions if ksirc was built
if [ -d $RPM_BUILD_ROOT%{kdeprefix}/lib ] ; then
    chmod a+x $RPM_BUILD_ROOT%{kdeprefix}/lib/*
    chmod a+x $RPM_BUILD_ROOT%{kdeprefix}/lib/ksirc/*
fi

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

%post
ldconfig

# Commented out for now
# modify /etc/inetd.conf for ktalkd
#cp -af /etc/inetd.conf /etc/inetd.conf.kdesave
#grep -v "bin/ktalkd"  /etc/inetd.conf | grep -v "bin/kotalkd" > /etc/inetd.conf_temp.1
#sed -e "/in.talkd/s/^talk/#KDE:talk/" -e "/in.ntalkd/s/^ntalk/#KDE:ntalk/" /etc/inetd.conf_temp.1 > /etc/inetd.conf_temp.2
#sed -e '/in.talkd/s;$;\
#talk    dgram   udp     wait    root    \/usr\/sbin\/tcpd  KDEDIR/bin/kotalkd;' -e '/in.ntalkd/s;$;\
#ntalk   dgram   udp     wait    root    \/usr\/sbin\/tcpd  KDEDIR/bin/ktalkd;' /etc/inetd.conf_temp.2 > /etc/inetd.conf_temp.1
#sed -e "s^KDEDIR^$RPM_INSTALL_PREFIX^g" /etc/inetd.conf_temp.1> /etc/inetd.conf
#rm -f /etc/inetd.conf_temp.1 /etc/inetd.conf_temp.2
#/usr/bin/killall -HUP inetd


%postun
ldconfig


%files -f ../file.list.%{kdename}

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 05 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed specfile wrt rpm 3.0

* Mon May 10 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- karchie again compiling
- updated to KDE 1.1.1
- files in KDEDIR/share/applnk no longer treated as %config files
- integrated the ktalk client (v-0.2.7) into the talk subpackage

* Mon Apr 19 1999 Conectiva <dist@conectiva.com>
- final rebuild for 3.0 server edition
- Removed suid bit from kppp

* Sat Apr 03 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Obsoletes kde-network from parolin

* Thu Apr  1 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed LINGUAS

* Fri Mar 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Compile ksirc together with all programs
- uses -frtti -fexceptions for all programs
- Changed %build and %install a bit

* Mon Mar  1 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Compile ksirc alone, using -fexceptions
- Removed postinstall script (Which belongs to kdestart)
- Removed all /usr/share/locale directories from filelist

* Fri Feb 26 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Compiled with -fno-exceptions -fno-rtti, except ksirc.
- Added postinstall script for kappfinder and wmconfig

* Thu Feb 25 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Retirado karchie e pws.

* Tue Jan 19 1999 Conectiva <dist@conectiva.com>
- Added pt_BR translations

* Wed Jan 06 1999 Preston Brown <pbrown@redhat.com>
- re-merged updates from Duncan Haldane
