Summary: Netscape navigator and communicator
Summary(pt_BR): Netscape: navegador e comunicador
Summary(es): Netscape: navegador y comunicador
Name: netscape
Version: 4.61
Serial: 4
Release: 5cl
Copyright: NPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source0: ftp://ftp.netscape.com/pub/communicator/english/4.61/unix/linux20_glibc2/complete_install/communicator-v461-export.x86-unknown-linuxglibc2.0.tar.gz
Source1: ftp://ftp.netscape.com/pub/communicator/english/4.61/unix/linux20_glibc2/complete_install/navigator-v461-export.x86-unknown-linuxglibc2.0.tar.gz
Source800: netscape-wmconfig.i18n.tgz
#Source2: ftp://ftp.netscape.com/pub/communicator/4.51/shipping/english/unix/linux20_sparc_glibc2/complete_install/communicator-v451-export.sparc-unknown-linux2.0.tar.gz
#Source3: ftp://ftp.netscape.com/pub/communicator/4.51/shipping/english/unix/linux20_sparc_glibc2/complete_install/navigator-v451-export.sparc-unknown-linux2.0.tar.gz
Source4: netscape-com.sh
Source5: netscape-communicator.wmconfig
Source6: netscape-navigator.wmconfig
Source7: Netscape.ad.pt_BR
Source8: Fortify-1.4.3-unix-src.tar.gz
#Source9: Fortify-1.4.2-unix-sparc.tar.gz
Buildroot: /var/tmp/ns-root
Obsoletes: nls
Requires: indexhtml
Prefix: /usr
Exclusivearch: i386 sparc

%changelog
* Sun Jun 20 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- updated to 4.61 (intel)
- updated Serial: to 4
- updated Netscape.ad.pt_BR to version 4.61 of Netscape
- updated fortify to 1.4.3
- sparc sources commented out

* Mon May 31 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated to 4.6 (on intel only, as this version is not disponible
  for sparc yet)
- Updated fortify to 1.4.2
- Updated Serial: to 3 (4.51 > 4.6) :(
- Updated Netscape.ad.pt_BR to version 4.6 of Netscape

* Sun Apr 18 1999 Conectiva <dist@conectiva.com>
- update to 4.51 and fortify 1.4.1
- build on sparc.
- remove LD_PRELOAD (ns is now linked against libBrokenLocale....)

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Wed Jan 20 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- minor typo in Netscape.ad.pt_BR

* Mon Dec 14 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- mais revisões na tradução (Netscape.ad.pt_BR)

* Mon Dec 14 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- revisão final do /usr/bin/netscape

* Sat Nov 28 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- parte da tradução já revisada pelo aurélio.

* Mon Nov 23 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- mais traduções! Agora o Aurélio continuará... :)

* Sun Nov 22 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- tradução quase terminada...
- xrdb -nocpp no /usr/bin/netscape, assim não precisamos do egcs

* Sat Nov 21 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- algumas correções na tradução

* Sat Nov 14 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Netscape.ad.pt_BR updated/verified with <CD>/misc/src/scripts/updnetscapead.py

* Tue Nov 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0
- serial 1... :( see the comment in the head of this spec...

* Tue Nov 10 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Nov 05 1998 Marcelo Wormsbecker Tosatti <marcelo@conectiva.com>
- added Fortify 1.3.0
- update to 4.5

* Tue Nov 03 1998 Marcelo Wormsbecker Tosatti <marcelo@conectiva.com>
- added i18n scheme and Netscape.ad translated to pt_BR

* Mon Oct 12 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Tue Oct  6 1998 Bill Nottingham <notting@redhat.com>
- update to 4.07

* Tue Aug 18 1998 Bill Nottingham <notting@redhat.com>
- updated to 4.06

* Fri Jul 10 1998 Cristian Gafton <gafton@redhat.com>
- modified to load libBrokenLocale.so.1, so that glibc-devel is no longer
  required

* Thu Jun 11 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu Jun 11 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Jun 10 1998 Erik Troan <ewt@redhat.com>
- replaced LANG=C with a preload of libBrokenLocale.so
- don't point to our html page if a home page is set in the user's preferences
- added missing " to wmconfig files

* Mon May 04 1998 Erik Troan <ewt@redhat.com>
- added LANG=C to netscape start wrapper

* Thu Apr 02 1998 Erik Troan <ewt@redhat.com>
- update to netscape 4.05
- moved common files to netscape-common package which both navigator and
  communicator require
- made relocateable (needs RPM >= 2.4.103 to relocate properly)

* Fri Jan 23 1998 Erik Troan <ewt@redhat.com>
- initial package is rel 3, works on RH 4.x and RH 5.x

%description
Netscape

%description -l pt_BR
Netscape

%description -l es
Netscape

%package common
Serial: 4
Summary: Code shared between navigator and communicator
Summary(pt_BR): Código compartilhado entre o navegador e o comunicador (Netscape)
Summary(es): Código compartido entre el navegador y el comunicador (Netscape)
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet

%description common
Files shared between the Netscape Navigator and Netscape Communicator
web browsers.

%description -l pt_BR common
Arquivos compartilhados entre os navegadores web Netscape Navigator
e o Netscape Communicator

%description -l es common
Archivos compartidos entre los navegadores web Netscape Navigator
y Netscape Communicator

%package communicator
Serial: 4
Requires: netscape-common
Summary: Netscape Communicator internet browser, news reader, and mail client
Summary(pt_BR): Browser Netscape Communicator, leitor de news, e cliente de mail
Summary(es): Browser Netscape Communicator, lector de news, y cliente de mail
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet

%description communicator
Netscape Communicator is the industry-leading web browser. It supports
the latest HTML standards, Java, and JavaScript. It also includes 
full-featured Usenet news reader as well as a complete email client.

Information on the Netscape Communicator license may be found in the file
/usr/doc/netscape-common-%{PACKAGE_VERSION}/LICENSE.

%description -l pt_BR communicator
O Netscape Communicator é o navegador web líder da indústria. Ele
suporta os mais recentes padrões HTML, Java e JavaScript. Ele
também inclui um leitor de news com muitas características
e um leitor completo de mail.  Informações sobre a licença
do Netscape Communicator podem ser encontradas no arquivo
/usr/doc/netscape-3-3/LICENSE.update.

%description -l es communicator
Netscape Communicator es el navegador web líder de la
industria. Soporta los más recientes padrones HTML, Java
y JavaScript. También incluye un lector de news con muchas
características y un lector completo de mail.  Información sobre
la licencia del Netscape Communicator puede ser encontrada en el
archivo /usr/doc/netscape-3-3/LICENSE.update.

%package navigator
Serial: 4
Requires: netscape-common
Summary: Netscape Navigator internet browser
Summary(pt_BR): Browser Netscape Navigator
Summary(es): Browser Netscape Navigator
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Summary(de): Netscape-Navigator-Internet-Browser

%description navigator
Netscape Navigator is the industry-leading web browser. It supports
the latest HTML standards, Java, and JavaScript.

Information on the Netscape Navigator license may be found in the file
/usr/doc/netscape-common-%{PACKAGE_VERSION}/LICENSE.


%description -l pt_BR navigator
Netscape Navigator é o navegador web líder da indústria.   Ele suporta
os mais recentes padrões HTML, Java e JavaScript.  Informações sobre
a licença do Netscape Communicator podem ser encontradas no arquivo
/usr/doc/netscape-3-3/LICENSE.update.

%description -l es navigator
Netscape Navigator es el navegador web líder de la industria. Soporta
los más recientes padrones HTML, Java y JavaScript.  Información
sobre la licencia del Netscape Communicator se puede encontrar en
el archivo /usr/doc/netscape-3-3/LICENSE.update.

%prep
%ifarch i386
%setup -c -b 1 -b 8
%elseifarch sparc
%setup -c -T -b 2 -b 3 -b 9
%endif
mv communic*/* .
rmdir communicator*

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin \
	$RPM_BUILD_ROOT/usr/lib/netscape/plugins \
	$RPM_BUILD_ROOT/usr/lib/netscape/java/classes

for I in *.nif; do
	tar -C $RPM_BUILD_ROOT/usr/lib/netscape -xzvf $I
done

mv $RPM_BUILD_ROOT/usr/lib/netscape/netscape $RPM_BUILD_ROOT/usr/lib/netscape/netscape-communicator
cp -a vreg $RPM_BUILD_ROOT/usr/lib/netscape
cp -a *.jar $RPM_BUILD_ROOT/usr/lib/netscape/java/classes

%ifarch i386
 echo 'Communicator,4.61.0.99147,/usr/lib/netscape' > /tmp/infile

%elseifarch sparc
 echo 'Communicator,4.51.0.99058,/usr/lib/netscape' > /tmp/infile
%endif

./vreg $RPM_BUILD_ROOT/usr/lib/netscape/registry /tmp/infile
rm -f /tmp/infile

# get the netscape-navigator binary now
%ifarch i386
tar xvzf %{SOURCE1} '*/netscape-v461.nif'
tar xvzf navigator*/netscape-v461.nif netscape
%elseifarch sparc
tar xvzf %{SOURCE3} '*/netscape-v451.nif'
tar xvzf navigator*/netscape-v451.nif netscape
%endif
# wmconfig
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

install -m 755 netscape $RPM_BUILD_ROOT/usr/lib/netscape/netscape-navigator

install -m755 $RPM_SOURCE_DIR/netscape-com.sh $RPM_BUILD_ROOT/usr/bin/netscape

# put this stuff into the doc directory
mv $RPM_BUILD_ROOT/usr/lib/netscape/{LICENSE,README,Netscape.ad} .

mkdir -p $RPM_BUILD_ROOT/etc/X11/applnk/Internet
cp -av $RPM_SOURCE_DIR/netscape-communicator.wmconfig \
 $RPM_BUILD_ROOT/etc/X11/applnk/Internet/netscape-communicator.wmconfig
cp -av $RPM_SOURCE_DIR/netscape-navigator.wmconfig \
 $RPM_BUILD_ROOT/etc/X11/applnk/Internet/netscape-navigator.wmconfig

ln -s netscape $RPM_BUILD_ROOT/usr/bin/netscape-navigator
ln -s netscape $RPM_BUILD_ROOT/usr/bin/netscape-communicator

rm -f `find $RPM_BUILD_ROOT -path "*dynMotif*"`

# i18n 
mkdir -p $RPM_BUILD_ROOT/usr/lib/netscape/i18n/
cp $RPM_SOURCE_DIR/Netscape.ad.pt_BR $RPM_BUILD_ROOT/usr/lib/netscape/i18n/

# Fortify
%ifarch i386
cd Fortify-1.4.3-unix-src
%elseifarch sparc
cd Fortify-1.4.2-unix-sparc
%endif
make -C src/common
make -C src/cmdline
./Fortify.sh $RPM_BUILD_ROOT/usr/lib/netscape/{netscape-communicator,netscape-navigator} << EOF
yes
no
no
yes
no
no
EOF



tar xvfpz $RPM_SOURCE_DIR/netscape-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(-,root,root)
/usr/bin/netscape
%dir /usr/lib/netscape
%docdir /usr/lib/netscape/nethelp
%doc README LICENSE Netscape.ad
/usr/lib/netscape/bookmark.htm
/usr/lib/netscape/java
%ifarch i386 
/usr/lib/netscape/libjsd.so
/usr/lib/netscape/dynfonts
%endif
/usr/lib/netscape/movemail
/usr/lib/netscape/movemail-src
/usr/lib/netscape/nethelp
/usr/lib/netscape/registry
/usr/lib/netscape/spell
/usr/lib/netscape/vreg
%dir /usr/lib/netscape/plugins
%dir /usr/lib/netscape/i18n
/usr/lib/netscape/i18n/Netscape.ad.pt_BR

%files navigator
%defattr(-,root,root)
#%config(missingok) /etc/X11/applnk/Internet/netscape-navigator.wmconfig
/usr/bin/netscape-navigator
/usr/lib/netscape/netscape-navigator

%files communicator
%defattr(-,root,root)
#%config(missingok) /etc/X11/applnk/Internet/netscape-communicator.wmconfig
/usr/bin/netscape-communicator
/usr/lib/netscape/netscape-communicator
