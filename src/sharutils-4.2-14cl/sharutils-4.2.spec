Summary: GNU shar utils - shar, unshar, uuencode, uudecode
Summary(pt_BR): Utilitários shar da GNU - shar, unshar, uuencode, uudecode
Summary(es): Utilitarios shar de la GNU - shar, unshar, uuencode, uudecode
Name: sharutils
Version: 4.2
Release: 14cl
copyright: GPL
Group: Applications/Archiving
Group(pt_BR): Aplicações/Arquivamento
Group(es): Aplicaciones/Almacenaje
# was .gz
Source: ftp://prep.ai.mit.edu/pub/gnu/sharutils-4.2.tar.bz2
Source1: sharutils-4.2.pt_BR.po
Patch1: sharutils-4.2-gmo.patch
Patch2: sharutils-4.2-man.patch
Patch3: sharutils-4.2.pt_BR.patch
Patch4: sharutils-4.2-po.patch
Patch5: sharutils-4.2-tmprace.patch
Prereq: info
BuildRoot: /var/tmp/shar-root

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- unset LINGUAS

* Tue Mar 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- fixed prereq

* Mon Nov 30 1998 Marcelo Tosatti <marcelo@conectiva.com>
- arrumados tmp races no mailshar e remsync

* Mon Oct 26 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed nl.po, pt.po missing '\n' in some msgstr
- included pt_BR.po

* Sun Apr 19 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- added pt_BR.po

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- ALRIGHT!  Woo-hoo!  Erik already did the install-info stuff!
- added BuildRoot
- spec file cleanups

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- uses install-info

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%description
The shar utilities can be used to encode and package a number of
files, binary and/or text, in a special plain text format.  This
format can safely be sent through email or other means where
sending binary files is difficult.

%description -l pt_BR
Os utilitários shar podem ser usados para codificar e empacotar
vários arquivos, binários e/ou texto, em um formato especial de
texto plano. Este formato pode ser seguramente mandado através de
mail ou outros meios onde mandar arquivos binários é difícil.

%description -l es
Los utilitarios shar pueden ser usados para codificar y empaquetar
varios archivos, binarios y/o texto, en un formato especial de
texto plano. Este formato puede ser seguramente mandado a través
de mail o otros medios donde mandar archivos binarios sea difícil.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3
%patch4 -p1
%patch5 -p1
cp $RPM_SOURCE_DIR/sharutils-4.2.pt_BR.po po/pt_BR.po

%build
[ "$LINGUAS" ] && unset LINGUAS
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr
make

%install
rm -f $RPM_BUILD_ROOT/usr/info/sharutils* $RPM_BUILD_ROOT/usr/info/remsync*
make prefix=$RPM_BUILD_ROOT/usr install
make prefix=$RPM_BUILD_ROOT/usr install-man
gzip -9nf $RPM_BUILD_ROOT/usr/info/sharutils*
gzip -9nf $RPM_BUILD_ROOT/usr/info/remsync*

strip $RPM_BUILD_ROOT/usr/bin/shar $RPM_BUILD_ROOT/usr/bin/unshar $RPM_BUILD_ROOT/usr/bin/uuencode $RPM_BUILD_ROOT/usr/bin/uudecode

%post
/sbin/install-info /usr/info/sharutils.info.gz /usr/info/dir

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete /usr/info/sharutils.info.gz /usr/info/dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/*
/usr/info/sharutils*
/usr/info/remsync*
/usr/man/*/*
/usr/share/locale/*/*/*
