Summary: A program for handling multimedia mail using the mailcap file.
Summary(pt_BR): Coleção de utilitários de manipulação MIME
Summary(es): Colección de utilitarios de manipulación MIME
Name: metamail
Version: 2.7
Release: 21cl
Copyright: Distributable
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source: ftp://thumper.bellcore.com/pub/nsp/metamail/mm2.7.tar.Z
Patch0: mm-2.7-make.patch
Patch1: mm-2.7-fonts.patch
Patch2: mm-2.7-glibc.patch
Patch3: mm-2.7-csh.patch
Patch4: mm-2.7-uudecode.patch
Patch5: mm-2.7-sunquote.patch
Patch6: mm-2.7-tmpfile.patch
Patch7: mm-2.7-ohnonotagain.patch
Patch8: mm-2.7-arghhh.patch
Requires: mktemp sharutils csh
BuildRoot: /var/tmp/metamail-root

%description
Metamail is a system for handling multimedia mail, using the mailcap
file.  Metamail reads the mailcap file, which tells Metamail what
helper program to call in order to handle a particular type of non-text
mail.  Note that metamail can also add multimedia support to certain
non-mail programs.

Metamail should be installed if you need to add multimedia support to
mail programs and some other programs, using the mailcap file.

%description -l pt_BR
Metamail é uma implementação de MIME ( Multipurpose Internet
Mail Extensions), um padrão proposto para mail multimídia
na Internet. Metamail implementa MIME, e também implementa
extensibilidade e configuração via o mecanismo "mailcap", descrito
em um RFC que acompanha o documento MIME.

%description -l es
Metamail soporta MINE (Multipurpose Internet Mail Extensions),
un padrón propuesto para mail multimedia en la Internet. Metamail
soporta MINE y también soporta la extensibilidad y configuración
a través del mecanismo "mailcap", descripto en un RFC que acompaña
el documento MINE.

%prep
%setup -q -n mm2.7
%patch0 -p1 -b .make
%patch1 -p1 -b .font
%patch2 -p1 -b .glibc
%patch3 -p1 -b .csh
%patch4 -p1 -b .tmpfiles
%patch5 -p1 -b .quote
#%patch6 -p1 -b .tmpagain
%patch7 -p1 -b .sigh
%patch8 -p1 -b .arghhh

%build
cd src
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" basics

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{usr/bin,usr/lib/metamail/fonts,usr/man/man1}

cd src
make INSTROOT=$RPM_BUILD_ROOT/usr install-all

install -m644 fonts/*.pcf $RPM_BUILD_ROOT/usr/lib/metamail/fonts
install -m644 fonts/fonts.alias $RPM_BUILD_ROOT/usr/lib/metamail/fonts
mkfontdir $RPM_BUILD_ROOT/usr/lib/metamail/fonts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/metamail
/usr/bin/audiocompose
/usr/bin/audiosend
/usr/bin/extcompose
/usr/bin/getfilename
/usr/bin/mailserver
/usr/bin/mailto
/usr/bin/mailto-hebrew
/usr/bin/metamail
/usr/bin/metasend
/usr/bin/mimencode
/usr/bin/mmencode
/usr/bin/patch-metamail
/usr/bin/rcvAppleSingle
/usr/bin/richtext
/usr/bin/richtoatk
/usr/bin/showaudio
/usr/bin/showexternal
/usr/bin/shownonascii
/usr/bin/showpartial
/usr/bin/showpicture
/usr/bin/sndAppleSingle
/usr/bin/splitmail
/usr/bin/sun-audio-file
/usr/bin/sun-message.csh
/usr/bin/sun-to-mime
/usr/bin/sun2mime
/usr/man/man1/audiocompose.1
/usr/man/man1/audiosend.1
/usr/man/man1/extcompose.1
/usr/man/man1/getfilename.1
/usr/man/man1/mailto-hebrew.1
/usr/man/man1/mailto.1
/usr/man/man1/metamail.1
/usr/man/man1/metasend.1
/usr/man/man1/mime.1
/usr/man/man1/mimencode.1
/usr/man/man1/mmencode.1
/usr/man/man1/patch-metamail.1
/usr/man/man1/richtext.1
/usr/man/man1/showaudio.1
/usr/man/man1/showexternal.1
/usr/man/man1/shownonascii.1
/usr/man/man1/showpartial.1
/usr/man/man1/showpicture.1
/usr/man/man1/splitmail.1

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 20)

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- rebuild against glibc 2.1

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue Jun 23 1998 Alan Cox <alan@redhat.com>
- Here we go again. One more quoting issue.

* Mon Jun 22 1998 Alan Cox <alan@redhat.com>
- If you want to know how not to write secure software
  then metamail is a good worked example. Mind you to
  be fair the original author wrote it as a prototype
  MIME tool and it stuck. Anyway it might actually be
  safe now. More from the Linux Security Audit Project.

* Tue Jun 16 1998 Alan Cox <alan@redhat.com>
- Round and round the tmp fixes go
  Where they stop nobody knows
- More holes in metamail fixed - (Linux Security Audit Project)

* Tue May 19 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Tue May 19 1998 Alan Cox <alan@redhat.com>
- Fixed the quoting bug in sun mail handling noted by Chris Evans and
  a while back via bugtraq.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Erik Troan <ewt@redhat.com>
- added security fix for uudecode 
- requires mktemp, sharutils

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc 

* Tue Apr 22 1997 Erik Troan <ewt@redhat.com>
- Added security patch from Olaf for csh escapes.
