Summary: Process accounting tools
Summary(pt_BR): Ferramentas de contabilização de processos
Summary(es): Herramientas de contabilidad de procesos
Name: psacct
Version: 6.3.2
Release: 3cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://prep.ai.mit.edu/pub/gnu/acct-6.3.2.tar.gz
Patch0: acct-6.3.2-path.patch
Patch1: acct-6.3.2-aclocal.patch
Buildroot: /var/tmp/psacct-root
Prereq: /sbin/install-info
Summary(de): Prozeßabrechnungs-Tools
Summary(fr): Outils pour les processus
Summary(tr): Süreç izleme araçlarý

%description
The tools necessary for accounting the activities of processes are
included here.

%description -l pt_BR
As ferramentas necessárias para contabilizar as atividades de
processos estão incluídas aqui.

%description -l es
Están incluidas aquí las herramientas necesarias para contabilizar
las actividades de procesos.

%description -l de
Hier sind die Tools enthalten, die zum Abrechnen von Prozeßaktivitäten
erforderlich sind.

%description -l fr
Outils nécessaires pour la prise en compte des activités des processus.

%description -l tr
Bu pakette, süreçlerin etkinliðinin hesaplanmasý için gerekli araçlar yer
alýr.

%prep
%setup -q -n acct-6.3.2
%patch -p1 -b .sopwith
%patch1 -p0 -b .aclocal

%build
automake --add-missing
autoconf
sleep 2
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{sbin,usr,var/log}

make prefix=$RPM_BUILD_ROOT/usr install

( cd $RPM_BUILD_ROOT
# move accton to /sbin -- leave historical symlink
  mv ./usr/sbin/accton ./sbin/accton
  ln -s ../../sbin/accton ./usr/sbin/accton

  gzip -9f ./usr/info/*
  :> ./var/log/pacct
  :> ./var/log/usracct
  :> ./var/log/savacct
)


%clean
rm -rf $RPM_BUILD_ROOT

%post
grep -v '* accounting: (psacct)' < /usr/info/dir > /usr/info/dir.new
mv -f /usr/info/dir.new /usr/info/dir
/sbin/install-info /usr/info/accounting.info.gz /usr/info/dir --entry="* accounting: (psacct).            The GNU Process Accounting Suite."

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete /usr/info/accounting.info.gz /usr/info/dir --entry="* accounting: (psacct).            The GNU Process Accounting Suite."
fi

%files
%defattr(-,root,root)
%attr(0600,root,root)	%config /var/log/pacct
%attr(0600,root,root)	%config /var/log/usracct
%attr(0600,root,root)	%config /var/log/savacct
/sbin/accton
/usr/sbin/accton
/usr/sbin/sa
/usr/sbin/dump-utmp
/usr/sbin/dump-acct
/usr/bin/ac
/usr/bin/lastcomm
/usr/man/man1/ac.1
/usr/man/man1/lastcomm.1
/usr/man/man8/sa.8
/usr/man/man8/accton.8
/usr/info/accounting.info.gz

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr  1 1999 Conectiva <dist@conectiva.com>
- small patch to aclocal.m4
- final rebuild for 3.0 spanish edition

* Mon Oct 26 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- accton needs to be accessible to /etc/rc.d/init.d/halt

* Fri May 08 1998 Erik Troan <ewt@redhat.com>
- install-info sucks

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 6.2 to 6.3

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
