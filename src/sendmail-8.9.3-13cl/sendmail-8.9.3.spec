Name: sendmail
Version: 8.9.3
Release: 13cl
Summary: sendmail mail transport agent
Summary(pt_BR): Sendmail - agente de transporte de mail
Summary(es): Sendmail - agente de transporte de mail
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Provides: smtpdaemon
Source0: ftp://ftp.cs.berkeley.edu/ucb/sendmail/sendmail.8.9.3.tar.bz2
Source1: sendmail.init
Source3: aliases
Source4: sendmail.sysconfig
Source5: sendmail-convert.sh
Source700: sendmail-man-pt_BR.tar
Patch0: sendmail-8.9.1-misc.patch
Patch1: sendmail-8.9.1-miscnoi386.patch
Patch2: sendmail-8.9.1-cf.patch
Patch3: sendmail-8.7.1-makemapman.patch
Patch4: sendmail-8.9.1-smrsh.patch
Patch5: sendmail-8.8.7-rmail.patch
Patch6: sendmail-hf-path.patch
Patch7: sendmail-8.9.2-hprescan-dos.patch
Patch8: sendmail-8.9.2-redir-dos.patch
BuildRoot: /var/tmp/sendmail.root
Prereq: chkconfig
Summary(de): sendmail-Mail-Übertragungsagent
Summary(fr): Agent de transport de courrier sendmail
Summary(tr): Elektronik posta hizmetleri sunucusu

%description
Sendmail is a Mail Transport Agent, which is the program
that moves mail from one machine to another.  Sendmail implements a
general internetwork mail routing facility, featuring aliasing and
forwarding, automatic routing to network gateways, and flexible
configuration.

If you need the ability to send and receive mail via the internet
you'll need sendmail.

%description -l pt_BR
O sendmail é um agente de transporte de correio eletrônico, que move
mensagens entre máquinas. Ele implementa facilidades de internetwork
e roteamento, caracterizando troca de nomes (aliases) e remessa a
novos endereços ( forwarding ), roteamento automático para gateways
da rede e configuração flexível.

Você precisará do sendmail se desejar enviar e receber mensagens
através da Internet.

%description -l es
sendmail es un agente de transporte de correo electrónico, que mueve
mensajes entre máquinas. Implementa facilidades de internetwork y
rutado, caracterizando cambio de nombres (aliases) y envío a nuevas
direcciones ( forwarding ), rutado automático para gateways de la
red y configuración flexible.  Necesitarás del sendmail si deseas
enviar y recibir mensajes a través de la Internet.

%package doc
Summary: sendmail documentation
Summary(pt_BR): Documentação do sendmail
Summary(es): Documentación del sendmail
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
Summary(de): Sendmail-Dokumentation 
Summary(fr): Documentation de sendmail
Summary(tr): sendmail belgeleri

%description doc
This package includes release notes, the sendmail FAQ, and a few
papers written about sendmail.  The papers are available in PostScript
and troff.

%description -l pt_BR doc
Este pacote inclui notas de versão, a FAQ do sendmail e alguns
documentos escritos sobre o sendmail. Estes documentos são disponibilizados
em formato PostScript e troff.

%description -l es doc
Este paquete incluye notas de versión, FAQ del sendmail y algunos
documentos escritos sobre el sendmail. Estos documentos son puestos
a disposición en formato PostScript y troff.

%package cf
Summary: sendmail configuration files and m4 macros
Summary(pt_BR): Arquivos de configuração e macros m4 do sendmail
Summary(es): Archivos de configuración y macros m4 del sendmail
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Summary(de): sendmail-Konfigurationsdateien und m4-Makros 
Summary(fr): fichiers de configuration sendmail et macros m4
Summary(tr): sendmail ayar dosyalarý ve makrolarý

%description cf
This package contains all the configuration files used to generate
the sendmail.cf file distributed with the base sendmail package.
You'll want this package if you need to reconfigure and rebuild
your sendmail.cf file.  For example, the default sendmail.cf is
not configured for UUCP.  If you need to send and receive mail
over UUCP, you may need this package to help you reconfigure sendmail.

%description -l pt_BR cf
Este pacote contém todos os arquivos de configuração usados para
gerar o arquivo sendmail.cf distribuído com o pacote base sendmail.
Você precisará deste pacote se for necessário reconfigurar e
reconstruir seu arquivo sendmail.cf. Por exemplo, o sendmail.cf
default não é configurado para UUCP. Se você precisar enviar e
receber mail através de UUCP, precisará deste pacote para ajudar
na reconfiguração do sendmail.

%description -l es cf
Este paquete contiene todos los archivos de configuración usados
para crear el archivo sendmail.cf distribuido con el paquete base
sendmail.  Te hará falta este paquete si necesitas reconfigurar y
reconstruir tu archivo sendmail.cf. Por ejemplo, el sendmail.cf por
defecto no se configura para UUCP. Si necesitas enviar y recibir
mail a través de UUCP, necesitarás de este paquete para ayudar en
la reconfiguración del sendmail.

%description -l de doc
Dieses Paket beinhaltet Release-Notes, die häufigsten Fragen und 
Antworten (FAQ) zu Sendmail sowie ein paar Artikel über Sendmail. 
Die letzteren sind sowohl in PostScript als auch in troff verfügbar. 

%description -l de cf
Dieses Paket enthält alle Konfigurationsdateien, die zum Erzeugen
der Sendmail.cf-Datei erforderlich sind, die mit dem Basis-
Sendmail-Paket geliefert wird. Sie werden darauf nicht verzichten
wollen, wenn Sie Ihre Sendmail-cf-Datei neu konfigurieren und bauen
wollen. Die Standard-Sendmail.cf.-Datei ist z.B. nicht für UUCP
konfiguriert. Wenn Sie also Post über UUCP versenden und empfangen
wollen, brauchen Sie es für eine Neukonfiguration.

%description -l de
Sendmail überträgt Mails zwischen Rechnern. Es implementiert
eine allgemeine Mail-Routing-Funktion über das Netzwerk mit 
Aliasing und Weiterleiten von Nachrichten, automatischem
Routing an Netzwerk-Gateways und flexible Konfiguration.
Wenn Sie E-Mails über das Internet senden und empfangen
möchten, brauchen Sie sendmail.

%description -l fr doc
Paquetage contenant les remarques sur la version, la FAQ sendmail et
quelques articles sur sendmail. Ces articles sont au format PostScript
et troff.

%description -l fr cf
Ce package contient tous les fichiers de configuration utilisés
pour générer le fichier sendmail.cf distribué avec le package de
base sendmail. Vous n'aurez besoin de ce package que pour 
reconfigurer et reconstruire votre fichier sendmail.cf. Par exemple
Le sendmail.cf par défaut n'est pas configuré pour UUCP. Si vous devez
recevoir des mails avec UUCP, vous aurez besoin de ce package pour
reconfigurer sendmail.

%description -l fr
Sendmail est un agent de transport de courrier, qui est le programme
transférent le courrier d'une machine à l'autre. Sendmail implémente
une facilité générale de routage de courrier entre les réseaux, permet
l'\"aliasing\" et le \"forwarding\", un routage automatique sur les
passerelles du réseau, et une configuration flexible.

%description -l tr doc
Bu paket, sendmail ile ilgili çokça sorulan sorularý ve sendmail hakkýnda
yazýlmýþ makalelerin bir kýsmýný içermektedir.

%description -l tr cf
Bu paket, sendmail paketi ile daðýtýlan sendmail.cf dosyasýný oluþturmak
için kullanýlan tüm ayar dosyalarýný içerir. sendmail.cf dosyasýný baþtan
ayarlayýp kurmak için kullanýlýr.

%description -l tr
Sendmail, bir mektubu bir makineden diðerine taþýr. Pek çok davranýþý
ayarlanabilir. Internet üzerinden mektup almak veya göndermek istiyorsanýz
bu pakete gereksiniminiz olacaktýr.

%prep
%setup -q -n sendmail-8.9.3
%ifarch i386
%patch0 -p1
%endif
%ifarch alpha
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1 -b .rmail
%patch6 -p1
%patch7 -p1
%build
cd src

./makesendmail

cd ../mailstats
rm -f Makefile
make CFLAGS="$RPM_OPT_FLAGS -I../src -DNEWDB" LDFLAGS=-s mailstats
cd ../rmail

rm -f Makefile
make CFLAGS="$RPM_OPT_FLAGS -I../src -DNEWDB" LDFLAGS=-s rmail
cd ../makemap
   cc -o makemap $RPM_OPT_FLAGS -I../src -DNEWDB -DNOT_SENDMAIL makemap.c ../src/safefile.c ../src/snprintf.c -ldb

cd ../praliases

rm -f Makefile
   cc -I../src $RPM_OPT_FLAGS -DNEWDB -s -o praliases praliases.c -ldb

cd ../smrsh
cc -static -s -o smrsh -DCMDDIR=\"/etc/smrsh\" \
	-DPATH=\"/bin:/sbin:/usr/bin:/usr/sbin\" smrsh.c

cd ../cf/cf 
m4 conectiva.mc > conectiva.cf
cd ../../ # main tree
patch -p1 < $RPM_SOURCE_DIR/sendmail-8.9.2-redir-dos.patch

%install
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/{init,rc0,rc1,rc2,rc3,rc4,rc5,rc6}.d
mkdir -p $RPM_BUILD_ROOT/etc/{mail,sysconfig,smrsh}
mkdir -p $RPM_BUILD_ROOT/usr/man/{man1,man3,man5,man7,man8}
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib,sbin,lib/sendmail-cf}
mkdir -p $RPM_BUILD_ROOT/var/{log,spool}

echo "# sendmail.cw - include all aliases for your machine here." > $RPM_BUILD_ROOT/etc/sendmail.cw
cd src/obj*
install -m6755 -o root -g mail sendmail $RPM_BUILD_ROOT/usr/sbin/sendmail

install -m644 newaliases.1 $RPM_BUILD_ROOT/usr/man/man1/
install -m644 sendmail.8   $RPM_BUILD_ROOT/usr/man/man8/
install -m644 mailq.1      $RPM_BUILD_ROOT/usr/man/man1/
install -m644 aliases.5    $RPM_BUILD_ROOT/usr/man/man5/
install -m644 sendmail.st  $RPM_BUILD_ROOT/var/log/
install -m644 sendmail.hf  $RPM_BUILD_ROOT/usr/lib/
cd ../../

install -s -m755 mailstats/mailstats $RPM_BUILD_ROOT/usr/bin
install -s -m755 praliases/praliases $RPM_BUILD_ROOT/usr/bin

install -s -m755 rmail/rmail       $RPM_BUILD_ROOT/usr/bin
install    -m644 rmail/rmail.8     $RPM_BUILD_ROOT/usr/man/man8
install -s -m755 makemap/makemap   $RPM_BUILD_ROOT/usr/bin
install    -m644 makemap/makemap.8 $RPM_BUILD_ROOT/usr/man/man8

install    -m755 smrsh/smrsh   $RPM_BUILD_ROOT/usr/sbin
install    -m644 smrsh/smrsh.8 $RPM_BUILD_ROOT/usr/man/man8

# install docs by hand
mkdir -p $RPM_BUILD_ROOT/usr/doc/sendmail
cp -ar FAQ KNOWNBUGS README RELEASE_NOTES doc $RPM_BUILD_ROOT/usr/doc/sendmail
cp smrsh/README $RPM_BUILD_ROOT/usr/doc/sendmail/README.smrsh

# install the cf files
cd cf
cp -ar * $RPM_BUILD_ROOT/usr/lib/sendmail-cf
cd -

install -m644 cf/cf/conectiva.cf $RPM_BUILD_ROOT/etc/sendmail.cf
install -m644 $RPM_SOURCE_DIR/aliases $RPM_BUILD_ROOT/etc/aliases

ln -sf ../sbin/sendmail $RPM_BUILD_ROOT/usr/lib/sendmail 
ln -sf ../sbin/sendmail $RPM_BUILD_ROOT/usr/bin/purgestat
ln -sf ../sbin/sendmail $RPM_BUILD_ROOT/usr/bin/hoststat
ln -sf ../sbin/sendmail $RPM_BUILD_ROOT/usr/bin/mailq
ln -sf ../sbin/sendmail $RPM_BUILD_ROOT/usr/bin/newaliases 

install -d -m755 -g mail -o root $RPM_BUILD_ROOT/var/spool/mqueue

cd $RPM_BUILD_ROOT/etc/mail
touch access.db
touch access

install -m755 -g root -o root $RPM_SOURCE_DIR/sendmail.init $RPM_BUILD_ROOT/etc/rc.d/init.d/sendmail
install -m755 -g root -o root $RPM_SOURCE_DIR/sendmail.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/sendmail
install -m755 -g root -o root $RPM_SOURCE_DIR/sendmail-convert.sh $RPM_BUILD_ROOT/usr/sbin/
ln -sf ../init.d/sendmail $RPM_BUILD_ROOT/etc/rc.d/rc0.d/K30sendmail
ln -sf ../init.d/sendmail $RPM_BUILD_ROOT/etc/rc.d/rc1.d/K30sendmail
ln -sf ../init.d/sendmail $RPM_BUILD_ROOT/etc/rc.d/rc2.d/S80sendmail
ln -sf ../init.d/sendmail $RPM_BUILD_ROOT/etc/rc.d/rc3.d/S80sendmail
ln -sf ../init.d/sendmail $RPM_BUILD_ROOT/etc/rc.d/rc4.d/S80sendmail
ln -sf ../init.d/sendmail $RPM_BUILD_ROOT/etc/rc.d/rc5.d/S80sendmail
ln -sf ../init.d/sendmail $RPM_BUILD_ROOT/etc/rc.d/rc6.d/K30sendmail

cd $RPM_BUILD_ROOT

%ifarch i386
strip usr/bin/mailstats usr/bin/praliases usr/bin/rmail usr/sbin/sendmail
%endif
strip usr/bin/makemap

touch etc/aliases.db
chown root.mail etc/aliases.db
chmod 644 etc/aliases.db





mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/sendmail-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/newaliases > /dev/null 2>&1
#/sbin/chkconfig --add sendmail

if [ ! -f /etc/mail/access -o ! -s /etc/mail/access ] ; then
	/usr/sbin/sendmail-convert.sh 
	/usr/bin/makemap hash /etc/mail/access < /etc/mail/access
fi

%postun
if [ $1 = 0 ]; then
   /sbin/chkconfig --del sendmail
fi

%files
%defattr(-,root,root)
/usr/bin/mailstats
/usr/bin/praliases
/usr/bin/hoststat
/usr/bin/purgestat
/usr/bin/rmail
/usr/bin/makemap
%attr(6755,root,mail) /usr/sbin/sendmail
/usr/bin/newaliases
/usr/bin/mailq
/usr/sbin/smrsh
/usr/lib/sendmail
%attr(755,root,root) /usr/sbin/sendmail-convert.sh

/usr/man/man8/rmail.8
/usr/man/man8/makemap.8
/usr/man/man8/sendmail.8
/usr/man/man5/aliases.5
/usr/man/man1/newaliases.1
/usr/man/man1/mailq.1
%attr(644,root,mail) /var/log/sendmail.st
%attr(644,root,mail) /usr/lib/sendmail.hf
%config /etc/sendmail.cf
%config /etc/sendmail.cw
%config /etc/aliases
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%ghost /etc/aliases.db
%attr(755,root,mail) %dir /var/spool/mqueue
%dir /etc/smrsh
%ghost /etc/mail/access.db
%config /etc/sysconfig/sendmail
%dir /etc/mail
%config /etc/rc.d/init.d/sendmail
%config(missingok) /etc/rc.d/rc0.d/K30sendmail
%config(missingok) /etc/rc.d/rc1.d/K30sendmail
%config(missingok) /etc/rc.d/rc2.d/S80sendmail
%config(missingok) /etc/rc.d/rc3.d/S80sendmail
%config(missingok) /etc/rc.d/rc4.d/S80sendmail
%config(missingok) /etc/rc.d/rc5.d/S80sendmail
%config(missingok) /etc/rc.d/rc6.d/K30sendmail
%config /etc/mail/access

%files cf
%defattr(-,root,root)
/usr/lib/sendmail-cf

%files doc
%defattr(-,root,root)
/usr/doc/sendmail

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Sun Jun  6 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed prereqs

* Sat Mar 13 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Mar 10 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initscript i18n (gprintf)

* Tue Mar 02 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- updated to 8.9.3

* Fri Feb 19 1999 Conectiva <dist@conectiva.com>
- man pages novas/revisadas

* Mon Jan 18 1999 Marcelo Tosatti <marcelo@conectiva.com>
- update to Sendmail 8.9.2
- applied Michal Zalewski patch's to fix two DoS's 
- removed -m486 for non-i386 arch's
 
* Tue Dec 08 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o egcs 1.0.3a e binutils 2.9.1.0.17

* Tue Dec 01 1998 Marcelo Tosatti <marcelo@conectiva.com>
- revisao do spec

* Fri Nov 27 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- versão acertada de 8.9.1 para 8.9.1a

* Tue Nov 17 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Nov 11 1998 Marcelo Tosatti <marcelo@conectiva.com>
- Update to 8.9.1a. 

* Wed Nov 04 1998 Marcelo Tosatti <marcelo@conectiva.com
- Fixed DoS in daemon.c

* Mon Sep 21 1998 Michael K. Johnson <johnsonm@redhat.com>
- Allow empty QUEUE in /etc/sysconfig/sendmail for those who
  want to run sendmail in daemon mode without processing the
  queue regularly.

* Thu Sep 17 1998 Michael K. Johnson <johnsonm@redhat.com>
- /etc/sysconfig/sendmail

* Fri Aug 28 1998 Jeff Johnson <jbj@redhat.com>
- recompile statically linked binary for 5.2/sparc

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscripts

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- added a rmail patch

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- argh!  Fixed some of the db1 handling that had to be added for glibc 2.1

* Fri Oct 24 1997 Donnie Barnes <djb@redhat.com>
- added support for db1 on SPARC

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- added chkconfig support
- various spec file cleanups
- changed group to Networking/Daemons (from Daemons).  Sure, it runs on
  non networked systems, but who really *needs* it then?

* Wed Oct 08 1997 Donnie Barnes <djb@redhat.com>
- made /etc/mail/deny.db a ghost
- removed preun that used to remove deny.db (ghost handles that now)
- NOTE: upgrading from the sendmail packages in 4.8, 4.8.1, and possibly
  4.9 (all Red Hat betas between 4.2 and 5.0) could cause problems.  You
  may need to do a makemap in /etc/mail and a newaliases after upgrading
  from those packages.  Upgrading from 4.2 or prior should be fine.

* Mon Oct 06 1997 Erik Troan <ewt@redhat.com>
- made aliases.db a ghost

* Tue Sep 23 1997 Donnie Barnes <djb@redhat.com>
- fixed preuninstall script to handle aliases.db on upgrades properly

* Mon Sep 15 1997 Donnie Barnes <djb@redhat.com>
- fixed post-install output and changed /var/spool/mqueue to 755

* Thu Sep 11 1997 Donnie Barnes <djb@redhat.com>
- fixed /usr/lib/sendmail-cf paths

* Tue Sep 09 1997 Donnie Barnes <djb@redhat.com>
- updated to 8.8.7
- added some spam filtration
- combined some makefile patches
- added BuildRoot support

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- marked initscript symlinks as missingok
- run newalises after creating /var/spool/mqueue

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- built against glibc, udated release to -6 (skipped -5!)

* Tue Apr 01 1997 Erik Troan <ewt@redhat.com>
- Added -nsl on the Alpha (for glibc to provide NIS functions).

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Added nis support.
