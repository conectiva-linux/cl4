Summary: Client and server for sending messages to users on remote host
Summary(pt_BR): Cliente e servidor para enviar mensagens para usuários em máquinas remotas
Summary(es): Cliente y servidor para enviar mensajes para usuarios en máquinas remotas
Name: rwall
Version: 0.10
Release: 12cl
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/daemons/netkit-rwall-0.10.tar.gz
Source1: rwalld.init
Patch: netkit-rwall-0.10-misc.patch
Patch1: netkit-rwalld-0.10-banner.patch
Buildroot: /var/tmp/rwall-root
Prereq: chkconfig
Summary(de): Client und Server zum Senden von Nachrichten an Benutzer am entfernten Host
Summary(fr): Client et serveur pour envoyer des messages aux utilisteurs de machines distantes.
Summary(tr): Baþka bir makinada çalýþan tüm kullanýcýlara mesaj gönderme

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed prereqs

* Fri Mar 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initscript i18n

* Fri Mar 12 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Oct 24 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- rwalld.init traduzido

* Tue May 05 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscript

* Tue Oct 28 1997 Erik Troan <ewt@redhat.com>
- fixed init script (didn't include function library)
- doesn't invoke wall with -n anymore

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- added a chkconfig compatible initscript
- added %attr attributes

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>

- initial build

%description
The rwall client sends a message to an rwall daemon running on a remote
machine, which relays the message to all of the users on the remote
machine. The rwall daemon is run from /etc/inetd.conf, and is disabled
by default on Red Hat systems.

%description -l pt_BR
O cliente rwall envia uma mensagem para um servidor rwall rodando
numa máquina remota, o qual retransmite a mensagem para todos
os usuários dessa máquina. O servidor rwall é executado pelo inetd
(/etc/inetd.conf), e é desabilitado por default nos sistemas Conectiva.

%description -l es
El cliente rwall envía un mensaje para un servidor rwall ejecutando
en una máquina remota, que retransmite el mensaje para todos
los usuarios de esta máquina. El servidor rwall es ejecutado por
el inetd (/etc/inetd.conf), y se inhabilita por defecto en los
sistemas Conectiva.

%description -l de
Der rwall-Client sendet eine Meldung an einen rwall-Dämon, der auf
einem entfernten Rechner läuft und die Meldung an alle Benutzer der
des entfernten Rechners verbreitet. Der rwall-Dämon wird von /etc/inetd.conf
betrieben und ist auf Red-Hat-Systemen standardmäßig deaktiviert.

%description -l fr
Le client rwall envoie un message à un démon rwall tournant sur une machine
distante, qui relaie le message vers tous les utilisateurs de la machine
distante. Le démon rwall est lancé  depuis /etc/inetd.conf, et est 
desactivé par défaut sur les systèmes Red Hat.

%description -l tr
Bir rwall sunucusu kendisine istemci tarafýndan gönderilen bir mesajý o anda
çalýþan tüm kullanýcýlara yansýtýr. Bu paket hem istemciyi hem sunucuyu
içermektedir ve /etc/inetd.conf'tan çalýþtýrýlmaktadýr. Öntanýmlý olarak bu
hizmet kullaným dýþý býrakýlmýþtýr.

%prep
%setup -n netkit-rwall-0.10
%patch -p1
%patch1 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
make INSTALLROOT=$RPM_BUILD_ROOT install
install -m 755 $RPM_SOURCE_DIR/rwalld.init $RPM_BUILD_ROOT/etc/rc.d/init.d/rwalld

%clean
rm -rf $RPM_BUILD_ROOT

#%post
#/sbin/chkconfig --add rwalld

%postun
if [ $1 = 0 ]; then
    /sbin/chkconfig --del rwalld
fi

%files
%attr(-,root,root) /usr/sbin/rpc.rwalld
%attr(-,root,root) /usr/man/man8/rpc.rwalld.8
%attr(-,root,root) /usr/man/man8/rwalld.8
%attr(-,root,root) /usr/bin/rwall
%attr(-,root,root) /usr/man/man1/rwall.1
%attr(-,root,root) %config /etc/rc.d/init.d/rwalld
