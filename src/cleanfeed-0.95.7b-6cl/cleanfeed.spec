Summary: INN spam filter
Summary(pt_BR): Filtro de SPAM (mensagens não-solicitadas) para o INN
Summary(es): Filtro de SPAM (mensajes no solicitadas) para INN
Name: cleanfeed
%define version 0.95.7b
Version: %{version}
Release: 6cl
Copyright: distributable
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source0: ftp://ftp.exit109.com/users/jeremy/cleanfeed-%{version}.tar.gz
Patch0: cleanfeed-0.95.7b-redhat.patch
Buildroot: /var/tmp/cleanfeed-root
Requires: perl-MD5
BuildArchitectures: noarch

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 17 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Oct 26 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Sep 03 1998 Cristian Gafton <gafton@redhat.com>
- update to 0.95.7b

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- spec file cleanups
- patch to get rod of /usr/local/bin/perl

* Mon Apr 13 1998 Bryan C. Andregg <bandregg@redhat.com>
- first package

%description
Cleanfeed is an automatic filter for INN that removes spam from incoming
newsfeeds.

%description -l pt_BR
Cleanfeed é um filtro automático para o INN que remove spam das
mensagens recebidas (newsfeed).

%description -l es
Cleanfeed es un filtro automático para el INN que elimina spam de
los mensajes proyectados (newsfeed).

%prep
%setup
%patch0 -p1 -b .rh

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/news
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
mkdir -p $RPM_BUILD_ROOT/usr/lib/news/bin/control
install -m 0644  -o news -g news cleanfeed.conf $RPM_BUILD_ROOT/etc/news/
install -m 0644  -o root  -g root cleanfeed.8 $RPM_BUILD_ROOT/usr/man/man8/
install -m 0750  -o news -g news cleanfeed \
	$RPM_BUILD_ROOT/usr/lib/news/bin/control/filter_innd.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,news,news) %config /etc/news/cleanfeed.conf
/usr/man/man8/cleanfeed.8
%attr(-,news,news) /usr/lib/news/bin/control/filter_innd.pl
