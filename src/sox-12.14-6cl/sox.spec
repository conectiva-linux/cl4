Summary: general purpose sound file conversion tool
Summary(pt_BR): Ferramenta para conversão de arquivos de som
Summary(es): Herramienta para conversión de archivos de sonido
Name: sox
Version: 12.14
Release: 6cl
Copyright: distributable
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
# was .gz
Source: http://home.sprynet.com/sprynet/cbagwell/sox-12.14.tar.bz2
Url: http://home.sprynet.com/sprynet/cbagwell/
Patch0: sox-12.14.patch
Patch1: sox-12.14.make.patch
Patch2: sox-12.14.alpha.patch
BuildRoot: /var/tmp/sox-root

Summary(de): Mehrzweck-Sounddatei-Konvertierungs-Tool 
Summary(fr): outil général de conversion de fichiers son
Summary(tr): Genel amaçlý ses dosyasý çevirme aracý

%description
The self described "swiss army knife of sound tools", sox can convert
between many different digitized sound formats and perform simple sound
manipulation functions.

%description -l pt_BR
O sox se autodenomina "canivete suíço das ferramentas de som". Ele
entende vários formatos de sons digitalizados, podendo fazer
conversões entre esses formatos e desempenhar funções simples de
manipulação de som.

%description -l es
sox se autodenomina "navaja suiza de las herramientas de sonido".
Entiende varios formatos de sonidos digitalizados, pudiendo hacer
conversiones entre estos formatos y desempeñar funciones sencillas
de manejo de sonido.

%package -n  sox-devel
Summary: sox library files
Summary(pt_BR): Arquivos da biblioteca do sox
Summary(es): Archivos de la biblioteca del sox
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description -n sox-devel 
Libraries that can be used to compile applications using sox libraries.

%description -l pt_BR -n sox-devel
Bibliotecas que podem ser usadas para compilar aplicações que usem as
bibliotecas do sox.

%description -l es -n sox-devel
Bibliotecas que pueden ser usadas para compilar aplicaciones que
usen las bibliotecas del sox.

%prep
%setup -q 
%patch0 -p1 -b .sox
%patch1 -p1 -b .make

%ifarch alpha
%patch2 -p1 -b .alpha
%endif 
ln -s Makefile.unx Makefile

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/usr/lib/
mkdir -p $RPM_BUILD_ROOT/usr/man/man1/
mkdir -p $RPM_BUILD_ROOT/usr/man/man3/

make install INSTALL_DIR=$RPM_BUILD_ROOT 
make install-lib INSTALL_DIR=$RPM_BUILD_ROOT 

echo "#!/bin/sh" > $RPM_BUILD_ROOT/usr/bin/soxplay
echo "" >> $RPM_BUILD_ROOT/usr/bin/soxplay
echo '/usr/bin/sox $1 -t .au - > /dev/audio' >> $RPM_BUILD_ROOT/usr/bin/soxplay
chmod 755 $RPM_BUILD_ROOT/usr/bin/soxplay

strip $RPM_BUILD_ROOT/usr/bin/sox

%clean
rm -rf $RPM_BUILD_ROOT

%doc README.cb  README README2 Setup TIPS TODO INSTALL CHEAT 
%files
%defattr(-,root,root)
/usr/bin/sox
/usr/bin/play   
/usr/bin/rec  
/usr/bin/soxplay
/usr/man/man1/sox.1
%files -n sox-devel
%defattr(-,root,root)
/usr/lib/libst.a

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Oct 19 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Sat Oct 10 1998 Michael Maher <mike@redhat.com>
- fixed broken spec file

* Mon Jul 13 1998 Michael Maher <mike@redhat.com>
- updated source from Chris Bagwell.

* Wed Jun 23 1998 Michael Maher <mike@redhat.com>
- made patch to fix the '-e' option. BUG 580
- added buildroot

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Nov 06 1997 Erik Troan <ewt@redhat.com>
- built against glibc
