Summary: procmail mail delivery agent
Summary(pt_BR): Procmail: agente de entrega de correio eletrônico
Summary(es): Procmail: agente de entrega de mail
Name: procmail
Version: 3.13.1
Release: 17cl
Copyright: distributable
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
#Source: ftp.informatik.rwth-aachen.de:/pub/packages/procmail/procmail-3.10.tar.gz
# recompactado com bzip2
Source: ftp.informatik.rwth-aachen.de:/pub/packages/procmail/procmail-3.13.1.tar.bz2
Patch1: procmail-3.10-000lock.patch
Patch2: procmail-3.10-lockf.patch
BuildRoot: /var/tmp/procmail-root
Summary(de): procmail Postzustellungs-Agent 
Summary(fr): Agent de distribution du courrier procmail
Summary(tr): procmail ileti daðýtýmý

%description
Conectiva Linux uses procmail for all local mail delivery.  In addition
to regluar mail delivery duties, procmail can be used to do many 
different automatic filtering, presorting, and mail handling jobs.
It is the basis for the SmartList mailing list processor.

%description -l pt_BR
O Conectiva Linux utiliza o procmail para todas as entregas de correio eletrônico
locais. Em adição ao serviço de entregas de mails regulares, procmail
pode ser usado para fazer vários filtros automáticos diferentes,
pré-seleção, e trabalhos com mail. Ele é a base para o processador
de lista de mail SmartList.

%description -l es
El Conectiva Linux usa procmail para todas las entregas de mail
locales. En adición al servicio de entregas de mails regulares,
procmail puede ser usado para hacer varios filtros automáticos
diferentes, preselección, y trabajos con mail. Es la base para el
procesador de lista de mail SmartList.

%description -l de
Conectiva Linux verwendet für die Zustellung lokaler Post Procmail. 
Neben den üblichen Postauslieferungsdiensten erledigt procmail auch 
eine Vielzahl von anderen Dingen, etwa automatische Filterung, 
Vorsortieren und Mail-Handling. "Es bildet die Grundlage für den 
SmartList-Mailing-Listen-Prozessor. 

%description -l fr
Conectiva Linux utilise procmail pour la délivrance de tous les courriers locaux.
En plus des tâches classiques de délivrance du courrier, procmail peut servir à
réaliser de nombreux filtrages automatiques, des tris et des travaux de gestion
du courrier. C'est la base du gestionnaire de liste de diffusions SmartList. 

%description -l tr
Conectiva Linux tüm yerel ileti daðýtýmý için procmail kullanýr. Normal ileti
daðýtým görevlerine ek olarak, pek çok deðiþik süzme, önsýralama ve iletiyi
alma iþlerini yapmak için kullanýlabilir. SmartList posta listesi yazýlýmýnýn
temelini oluþturur.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
%patch2 -p1 -b .lockf

%build
echo | make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1,man/man5}

make BASENAME=$RPM_BUILD_ROOT/usr install.bin install.man

strip $RPM_BUILD_ROOT/usr/bin/{procmail,lockfile,formail}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(6755,root,mail)	/usr/bin/procmail
%attr(2755,root,mail)	/usr/bin/lockfile
/usr/bin/formail
/usr/bin/mailstat

/usr/man/man1/procmail.1
/usr/man/man1/formail.1
/usr/man/man1/lockfile.1

/usr/man/man5/procmailrc.5
/usr/man/man5/procmailsc.5
/usr/man/man5/procmailex.5

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue May  4 1999 Conectiva <dist@conectiva.com>
- Adjusted some translations in the spec file

* Mon Apr  8 1999 Marcelo Tosatti <marcelo@conectiva.com>
- update to 3.13.1

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Oct 28 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
