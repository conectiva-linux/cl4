Summary: A chat program.
Summary(pt_BR): Usa o protocolo de talk da internet para criar sessões de chat entre vários usuários 
Summary(es): Usa el protocolo de talk de la internet para crear sesiones de chat entre varios usuarios 
Name: ytalk
Version: 3.1
Release: 3cl
Copyright: BSD
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source: ftp://quatramaran.ens.fr/pub/orabidoo/ytalk/ytalk-3.1.tar.bz2
Source1: ytalkrc
Patch: ytalk-3.0.3-config.patch
Patch1: ytalk-3.0.2-glibc.patch
BuildRoot: /var/tmp/ytalk-root

%description
The YTalk program is essentially a chat program for multiple users.
YTalk works just like the UNIX talk program and even communicates with
the same talk daemon(s), but YTalk allows for multiple connections (unlike
UNIX talk).  YTalk also supports redirection of program output to other
users as well as an easy-to-use menu of commands.

Install the ytalk package if you need a chat program for multiple users.

%description -l pt_BR
ytalk é uma extensão do protocolo "talk" da Internet que permite
mais de dois usuários por conversação, redirecionamento da saída
do programa para outros, assim como um menu de comandos fácil de
usar. Ele utiliza o mesmo daemon "talk" que o programa "talk" padrão.

%description -l es
ytalk es una extensión del protocolo "talk" de Internet que permite
más de dos usuarios por conversación, nueva orientación de la salida
del programa para otros, así como un menú de comandos fácil de
usar. Utiliza el mismo daemon "talk" que el programa "talk" padrón.

%prep
%setup -q
#%patch -p1 -b .config
#%patch1 -p1 -b .glibc

%build
CFLAGS=$RPM_OPT_FLAGS ./configure --prefix=/usr --sysconfdir=/etc
make 

%install
make install prefix=$RPM_BUILD_ROOT/usr sysconfdir=$RPM_BUILD_ROOT/etc
strip $RPM_BUILD_ROOT/usr/bin/ytalk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/ytalk
/usr/man/man1/ytalk.1
%config /etc/ytalkrc

%changelog
* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Sun Nov 22 1998 Preston Brown <pbrown@redhat.com>
- upgrade to ytalk 3.1

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binary

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
