Summary: A list monitor with a visual output.
Summary(pt_BR): Ferramentas de banco de dados para face
Summary(es): Herramientas de banco de datos para face
Name: faces
Version: 1.6.1
Release: 17cl
Copyright: freeware
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet

Source: ftp://ftp.cs.indiana.edu/pub/faces/faces/faces-1.6.1.tar.Z
Patch0: faces-1.6.1-make.patch
Patch1: faces-1.6.1-awk.patch
Patch2: faces-1.6.1-string.patch
Patch3: faces-1.6.1-fix.patch
Requires: libgr-progs
BuildRoot: /var/tmp/faces-root

%description
Faces is a program for visually monitoring a list (typically a list of
incoming mail messages, a list of jobs in a print queue or a list of
system users).  Faces operates in five different modes: monitoring for
new mail, monitoring an entire mail file, monitoring a specified print
queue, monitoring users on a machine and custom monitoring.  Faces also
includes a utility for including a face image (a compressed, scanned
image) with mail messages.  The image has to be compressed in a certain
way, which can then be uncompressed and displayed on-the-fly in the mail
program.  This feature of faces is typically used with the exmh mail
handling system.

Install faces if you'd like to use its list monitoring capability or its
face image inclusion capability.  If you would like to include face
images in email, you'll also need to install the faces-xface package.  If
you would like to develop xface applications, you'll need to also install
faces-devel.

%description -l pt_BR
Este pacote é usado principalmente com o exmh. Você pode pegar uma
foto ou qualquer outra imagem e transformá-la numa "face" que pode
ser transmitida por qualquer programa de email e mostrada no exmh
ou outros programas.  ~

%description -l es
Este paquete se usa principalmente con el exmh. Tu puedes coger
una foto o otra imagen y transformarla en una "face" que puede ser
transmitida por cualquier programa de e-mail y mostrada en el exmh
o otros programas.

%package xface
Requires: libgr-progs
Summary: Utilities needed by mailers for handling Faces' X-face images.
Summary(pt_BR): Utilitários para manipular cabeçalhos X-Face
Summary(es): Utilitarios para manipular cabeceras X-Face
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet

%description xface
Faces-xface includes the utilities that mail user agent programs need to
handle X-Face mail headers.  When an email program reads the X-face
header line in an email message, it calls these utilities to display
the face image included in the message.

You'll need to install faces-xface if you want your mail program to
display Faces' X-face images.

%description -l pt_BR xface
Estes são os utilitários para manipular cabeçalhos de mail X-Face.
São chamados por leitores de mail para mostrar uma face contida em
uma mensagem.

%description -l es xface
Estos son los utilitarios para manipular encabezamientos de mail
X-Face.  Son llamados por lectores de mail para enseñar una face
contenida en un mensaje.

%package devel
Summary: The Faces program's library and header files.
Summary(pt_BR): Bibliotecas e arquivos de inclusão para Faces
Summary(es): Bibliotecas y archivos de inclusión para Faces
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description devel
Faces-devel contains the faces program development environment,
(i.e., the static libraries and header files).

If you want to develop Faces applications, you'll need to install
faces-devel.  You'll also need to install the faces package.

%description -l pt_BR devel
Este é o ambiente de desenvolvimento do xface. Contém as bibliotecas
estáticas e arquivos de inclusão para desenvolvimento xface.

%description -l es devel
Este es el ambiente de desarrollo del xface. Contiene las bibliotecas
estáticas y archivos de inclusión para desarrollo xface.

%prep
%setup -q -n faces
%patch0 -p1 -b .make
%patch1 -p1 -b .awk
%patch2 -p1 -b .string
%patch3 -p1 -b .fix

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" -f Makefile.dist x11

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,include,lib,man/man1,man/man3}

make -f Makefile.dist \
	BINDIR=$RPM_BUILD_ROOT/usr/bin \
	LIBDIR=$RPM_BUILD_ROOT/usr/lib \
	MANDIR=$RPM_BUILD_ROOT/usr/man \
	install

install -m644 compface/compface.h $RPM_BUILD_ROOT/usr/include/compface.h

mkdir -p $RPM_BUILD_ROOT/usr/lib/faces

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/compface
/usr/man/man1/compface.1
/usr/man/man3/compface.3
/usr/bin/icon2ikon
/usr/bin/ikon2icon
/usr/bin/fs2ikon
/usr/bin/rs2icon
/usr/bin/fs2xbm
/usr/bin/xbm2ikon
/usr/bin/xbmcut48
/usr/bin/xbmsize48
/usr/bin/addxface
/usr/bin/mailq.faces
/usr/bin/from.faces
/usr/bin/lpqall.faces
/usr/bin/rotary.faces
/usr/bin/facesaddr
/usr/bin/facesall
/usr/bin/mkfacesindex
/usr/bin/newscheck.faces
/usr/bin/newsfrom.faces
/usr/bin/faces
/usr/bin/face_update
/usr/bin/faces.sendmail
/usr/man/man1/faces.1
/usr/man/man1/face_update.1
/usr/lib/faces

%files xface
%defattr(-,root,root)
/usr/bin/uncompface
/usr/man/man1/uncompface.1
/usr/man/man3/uncompface.3
/usr/bin/ikon2xbm

%files devel
%defattr(-,root,root)
/usr/include/compface.h
/usr/lib/libcompface.a

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Injected new groups into package

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 08 1999 Preston Brown <pbrown@redhat.com>
- fix xbm2ikon problem (bug # 1060).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 14)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- faces-devel moved to Development/Libraries

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- changed netpbm requirement to libgr-progs requirement

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
