Summary: decompressor for .arj format archives
Summary(pt_BR): Descompactador para arquivos no formato .arj
Summary(es): Descompresor para archivos en formato .arj
Name: unarj
Version: 2.41a
Release: 11cl
Group: Applications/Archiving
Group(pt_BR): Aplicações/Arquivamento
Group(es): Aplicaciones/Almacenaje
Copyright: distributable
# was .gz
Source: ftp://sunsite.unc.edu/pub/Linux/utils/compress/unarj241a.tar.bz2
BuildRoot: /var/tmp/unarj-root
Summary(de): Dekomprimierer für .arj-Archive
Summary(fr): Décompresseur pour les archives .arj .
Summary(tr): ARJ biçimindeki arþivleri açan araç

%description
The unarj program is used to uncompress .arj format archives,
which were somewhat popular on DOS based machines.

%description -l pt_BR
O programa unarj é usado para descomprimir armazenagens em formato
.arj, que era algo popular em máquinas DOS.

%description -l es
El programa unarj se usa para descomprimir almacenajes en formato
.arj, que era algo popular en máquinas DOS.

%description -l de
Das Programm 'unarj' dient zum Dekomprimieren von Archiven im
.arj-Format, das auf DOS-Rechnern einigermaßen beliebt ware.

%description -l fr
Le programme unarj est utilisé pour décompresser des archives
au format .arj, qui ont été très répandeus sur les systèmes DOS.

%description -l tr
unarj, arj biçimindeki arþivler için açma programýdýr. ARJ, DOS tabanlý
makinelerde sýkça kullanýlan bir sýkýþtýrma biçimidir.

%prep
%setup -q -n unarj241a

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin

install -m 755 unarj $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc unarj.doc
/usr/bin/unarj

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Otto Hammersmith <otto@redhat.com>
- fixed src url

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
