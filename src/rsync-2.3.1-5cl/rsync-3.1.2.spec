Summary: Program for efficient remote updates of files.
Summary(pt_BR): Programa para atualizar arquivos remotos de forma eficiente.
Summary(es): Programa para actualizar archivos remotos de forma eficiente.
Name: rsync
Version: 2.3.1
Release: 5cl
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
#Source: ftp://samba.anu.edu.au/pub/rsync/rsync-%{version}.tar.gz
# recompressed with bzip2
Source: ftp://samba.anu.edu.au/pub/rsync/rsync-%{version}.tar.bz2
BuildRoot: /var/tmp/rsync-root
Copyright: GPL

%description
rsync is a faster flexible replacement for rcp allowing rapid and
network efficient synchronization of files or directories on different
machines by transferring just the differences between those
directories in a compressed form.  It doesn't need either machine to
have a copy of what is on the other.

A technical report describing the rsync algorithm is included in this
package.

%description -l pt_BR
O rsync é um substituto mais rápido e flexível para o rcp permitindo
sincronização de arquivos ou diretórios via rede de forma rápida
e eficiente entre diferentes máquinas transferindo somente as
diferenças entre estes diretórios de forma compactada. Ele não
precisa que nenhuma das máquinas tenha uma cópia do que está
na outra.

Um relatório técnico descrevendo o algoritmo usado pelo rsync está
disponível neste pacote.

%description -l es
rsync es un substituto más rápido y flexible para rcp que permite la
sincronización de archivos o directorios, vía red, de forma rápida
y eficiente, entre diferentes máquinas transfiriendo solamente
las diferencias entre estos directorios de forma compactada. No
necesita que ninguna de las máquinas tengan una copia de lo que
está en la otra.  Está disponible en este paquete, una relación
técnica describiendo el algoritmo usado por el rsync.

%prep
%setup -q

%build
./configure --prefix=/usr --mandir=$RPM_BUILD_ROOT/usr/man/ --bindir=$RPM_BUILD_ROOT/usr/bin
make CCOPTFLAGS="$RPM_OPT_FLAGS"
strip rsync

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1

make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/rsync
/usr/man/man1/rsync.1
/usr/man/man5/rsyncd.conf.5
%doc tech_report.tex
%doc README
%doc COPYING

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 8 1999 Marcelo Tosatti <marcelo@conectiva.com>
- update to 3.1.2

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Nov 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Mon Sep 21 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.1.1

* Mon Aug 17 1998 Erik Troan <ewt@redhat.com>
- updated to 2.1.0

* Thu Aug 06 1998 Erik Troan <ewt@redhat.com>
- buildrooted and attr-rophied
- removed tech-report.ps; the .tex should be good enough

* Mon Aug 25 1997 John A. Martin <jam@jamux.com>
- Built 1.6.3-2 after finding no rsync-1.6.3-1.src.rpm although there
  was an ftp://ftp.redhat.com/pub/contrib/alpha/rsync-1.6.3-1.alpha.rpm
  showing no packager nor signature but giving 
  "Source RPM: rsync-1.6.3-1.src.rpm".
- Changes from 1.6.2-1 packaging: added '$RPM_OPT_FLAGS' to make, strip
  to '%build', removed '%prefix'.

* Thu Apr 10 1997 Michael De La Rue <miked@ed.ac.uk>
- rsync-1.6.2-1 packaged.  (This entry by jam to credit Michael for the
  previous package(s).)
