Summary: Biff mail checker client and comsat mail checking server
Summary(pt_BR): CLiente (biff) e servidor (comsat) verificadores de correio
Summary(es): Cliente (biff) y servidor (comsat) verificadores de correo
Name: biff
Version: 0.10
Release: 7cl
Copyright: BSD
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source0: ftp://sunsite.unc.edu/pub/Linux/system/network/finger/biff+comsat-0.10.tar.gz
Patch0: biff+comsat-0.10-misc.patch
Patch1: biff+comsat-0.10-nobr.patch
Requires: inetd
BuildRoot: /var/tmp/biff-root
Summary(de): Biff-Mail-Checker-Client und comsat-Mail-Checking-Server
Summary(fr): Le client de notification de courrier Biff et le serveur de notification de courrier comsat.
Summary(tr): Ýleti olup olmadýðýný denetleyen istemci ve sunucular

%description
The biff client and comsat server are an antiquated method of asynchronous
mail notification. Although they are still supported, most users use
their shells MAIL variable (or mail under csh variants) to check for
mail, or a dedicated application such as xbiff or xmailbox.

%description -l pt_BR
O cliente biff e o servidor comsat são métodos antiquados para
receber e enviar notificações assíncronas de novas mensagens. Embora
eles ainda sejam suportados, a maioria dos usuários usa suas
variáveis de ambiente MAIL (ou mail sob variante de csh) para
verificar a chegada de novas mensagens, ou uma aplicação dedicada
tal como xbiff ou xmailbox.

%description -l es
Cliente biff y servidor comsat son métodos anticuados para recibir
y enviar notificaciones asíncronas de nuevos mensajes. A pesar de
que aún se soportan, la mayoría de los usuarios usa sus variables
de ambiente MAIL (el mail bajo variante de csh) para verificar
la llegada de nuevos mensajes, o una aplicación dedicada tal como
xbiff o xmailbox.

%description -l de
biff-Client und comsat-Server sind ein veraltetes Verfahren zur asynchronen
Mail-Benachrichtigung. Obwohl es noch unterstützt wird, verwenden die
meisten Benutzer die MAIL-Variable der Shell (bzw. 'mail' unter 
csh-Variationen), oder eine spezielle Anwendung wie xbiff or xmailbox,
um neue Mail-Nachrichten abzufragen.

%description -l fr
Le client biff et le serveur comsat servent à l'antique notification
asynchrone de mail. Bien qu'ils soient toujours supportés, beaucoup
d'utilisateurs utilisent les variables MAIL du shell ( ou mail sous les
variantes csh), pour se tenir au courant du mail, ou des applications
dédiés comme xbiff ou xmailbox.

%description -l tr
biff istemcisi ve comsat sunucusu, eski bir mektup bildirme yöntemini
gerçeklerler. Halen desteklenmelerine karþýn, pek çok kullanýcý, mektup olup
olmadýðýný kontrol etmek için ya bir kabuk deðiþkeni olan MAIL deðiþkenini
(csh kabuðunda mail deðiþkenine karþýlýk gelir) ya da xbiff, xmailbox gibi
uygulamalarý kullanýr.

%prep
%setup -q -n biff+comsat-0.10
%patch0 -p1
%patch1 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1,man/man8,sbin}

make INSTALLROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/biff
/usr/man/man1/biff.1
/usr/sbin/in.comsat
/usr/man/man8/in.comsat.8
/usr/man/man8/comsat.8

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
