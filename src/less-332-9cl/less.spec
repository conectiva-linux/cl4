Summary: text file browser -- less is more
Summary(pt_BR): Browser para arquivo texto (- é +)
Summary(es): Browser para archivo texto (- es +)
Name: less
Version: 332
Release: 9cl
Copyright: distributable
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
Source: ftp://prep.ai.mit.edu:/pub/gnu/less-332.tar.bz2
Source1: less-conectiva.tar.bz2
Buildroot: /var/tmp/less-root

%changelog
* Sat Jun 12 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- included lesspipe and lesskey (thanks to casantos)
- included less.{sh,csh}

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Oct 27 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- updated to 332 and built for Manhattan
- added buildroot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%description
less is a text file viewer much like 'more', only better.  

%description -l pt_BR
less é um visualizador de arquivo texto parecido com 'more', só
que melhor.

%description -l es
less es un visor de archivo texto parecido con 'more', sólo que
mejor.

%description -l de
less ist ein Textdatei-Viewer ähnlich 'more' ... aber besser! 

%description -l fr
less est un visualisateur de fichier texte, comme « more », mais en mieux

%description -l tr
Metin dosyasý görüntüleyici - more benzeri

%prep
%setup -a 1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr
make datadir=/usr/doc

lesskey -o lesskey.out lesskey.in

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr

%ifarch axp
mkdir -p $RPM_BUILD_ROOT/bin
ln -sf /usr/bin/less /bin/more
%endif

mkdir -p $RPM_BUILD_ROOT/etc/profile.d/
install lesspipe    $RPM_BUILD_ROOT/usr/bin/lesspipe
install lesskey.out $RPM_BUILD_ROOT/etc/lesskey
install less.sh     $RPM_BUILD_ROOT/etc/profile.d/
install less.csh    $RPM_BUILD_ROOT/etc/profile.d/

%files
%attr(755,root,root) /usr/bin/*
%attr(644,root,root) /usr/man/man1/*
%attr(644,root,root) %doc lesskey.in
%attr(644,root,root) %config /etc/lesskey
%attr(755,root,root) %config /etc/profile.d/less.sh
%attr(755,root,root) %config /etc/profile.d/less.csh
%ifarch axp
%attr(755,root,root) /bin/more
%endif

%clean
rm -rf $RPM_BUILD_ROOT
