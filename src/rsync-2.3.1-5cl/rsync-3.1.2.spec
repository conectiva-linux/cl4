Summary: Program for efficient remote updates of files.
Summary(pt_BR): Programa para atualizar arquivos remotos de forma eficiente.
Summary(es): Programa para actualizar archivos remotos de forma eficiente.
Name: rsync
Version: 2.3.1
Release: 5cl
Group: Applications/Internet
Group(pt_BR): Aplica��es/Internet
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
O rsync � um substituto mais r�pido e flex�vel para o rcp permitindo
sincroniza��o de arquivos ou diret�rios via rede de forma r�pida
e eficiente entre diferentes m�quinas transferindo somente as
diferen�as entre estes diret�rios de forma compactada. Ele n�o
precisa que nenhuma das m�quinas tenha uma c�pia do que est�
na outra.

Um relat�rio t�cnico descrevendo o algoritmo usado pelo rsync est�
dispon�vel neste pacote.

%description -l es
rsync es un substituto m�s r�pido y flexible para rcp que permite la
sincronizaci�n de archivos o directorios, v�a red, de forma r�pida
y eficiente, entre diferentes m�quinas transfiriendo solamente
las diferencias entre estos directorios de forma compactada. No
necesita que ninguna de las m�quinas tengan una copia de lo que
est� en la otra.  Est� disponible en este paquete, una relaci�n
t�cnica describiendo el algoritmo usado por el rsync.

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
