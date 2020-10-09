Summary: decompressor for .arj format archives
Summary(pt_BR): Descompactador para arquivos no formato .arj
Summary(es): Descompresor para archivos en formato .arj
Name: unarj
Version: 2.41a
Release: 11cl
Group: Applications/Archiving
Group(pt_BR): Aplica��es/Arquivamento
Group(es): Aplicaciones/Almacenaje
Copyright: distributable
# was .gz
Source: ftp://sunsite.unc.edu/pub/Linux/utils/compress/unarj241a.tar.bz2
BuildRoot: /var/tmp/unarj-root
Summary(de): Dekomprimierer f�r .arj-Archive
Summary(fr): D�compresseur pour les archives .arj .
Summary(tr): ARJ bi�imindeki ar�ivleri a�an ara�

%description
The unarj program is used to uncompress .arj format archives,
which were somewhat popular on DOS based machines.

%description -l pt_BR
O programa unarj � usado para descomprimir armazenagens em formato
.arj, que era algo popular em m�quinas DOS.

%description -l es
El programa unarj se usa para descomprimir almacenajes en formato
.arj, que era algo popular en m�quinas DOS.

%description -l de
Das Programm 'unarj' dient zum Dekomprimieren von Archiven im
.arj-Format, das auf DOS-Rechnern einigerma�en beliebt ware.

%description -l fr
Le programme unarj est utilis� pour d�compresser des archives
au format .arj, qui ont �t� tr�s r�pandeus sur les syst�mes DOS.

%description -l tr
unarj, arj bi�imindeki ar�ivler i�in a�ma program�d�r. ARJ, DOS tabanl�
makinelerde s�k�a kullan�lan bir s�k��t�rma bi�imidir.

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
