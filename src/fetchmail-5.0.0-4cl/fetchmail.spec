%define name fetchmail
%define version 5.0.0
%define release 4cl
%define builddir $RPM_BUILD_DIR/%{name}-%{version}
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://www.tuxedo.org/~esr/fetchmail
Source: %{name}-%{version}.tar.bz2
Source800: fetchmail-wmconfig.i18n.tgz
Group: Applications/Internet
Group(pt_BR): Aplica��es/Internet
Group(es): Aplicaciones/Internet
Copyright: GPL
Icon: fetchmail.gif
Requires: smtpdaemon
BuildRoot: /var/tmp/%{name}-%{version}
Summary: Full-featured POP/IMAP mail retrieval daemon
Summary(pt_BR): Baixa mail de um servidor usando POP ou IMAP
Summary(es): Baja mensajes de un servidor usando POP � IMAP
Summary(fr): Collecteur (POP/IMAP) de courrier �lectronique
Summary(de): Program zum Abholen von E-Mail via POP/IMAP
Summary(es_AR): Recolector de correo via POP/IMAP
Summary(pl): Zdalny demon pocztowy do protoko��w POP2, POP3, APOP, IMAP
Summary(tr): POP2, POP3, APOP, IMAP protokolleri ile uzaktan mektup alma yaz�l�m�
Summary(da): Alsidig POP/IMAP post-afhentnings d�mon

%description
Fetchmail is a free, full-featured, robust, and well-documented remote
mail retrieval and forwarding utility intended to be used over
on-demand TCP/IP links (such as SLIP or PPP connections).  It
retrieves mail from remote mail servers and forwards it to your local
(client) machine's delivery system, so it can then be be read by
normal mail user agents such as mutt, elm, pine, (x)emacs/gnus, or mailx.
Comes with an interactive GUI configurator suitable for end-users.

%description -l pt_BR
fetchmail � um programa que � usado para recuperar mensagens de um
servidor de mail remoto. Ele pode usar Post Office Protocol (POP)
ou IMAP (Internet Mail Access Protocol) para isso, e entrega o mail
atrav�s do servidor local SMTP (normalmente sendmail).

%description -l es
fetchmail es un programa utilizado para recuperar mensajes de un
servidor de mail remoto. Para esto, puede usar Post Office Protocol
(POP) o IMAP (Internet Mail Access Protocol), y entrega el mail a
trav�s del servidor local SMTP (normalmente sendmail).

%description -l fr
Fetchmail est un programme qui permet d'aller rechercher du courrier
�lectronique sur un serveur de mail distant. Fetchmail connait les
protocoles POP (Post Office Protocol), IMAP (Internet Mail Access
Protocol) et d�livre le courrier �lectronique a travers le
serveur SMTP local (habituellement sendmail).

%description -l de
Fetchmail ist ein freies, vollst�ndiges, robustes und
wohldokumentiertes Werkzeug zum Abholen und Weiterreichen von E-Mail,
gedacht zum Gebrauch�ber tempor�re TCP/IP-Verbindungen (wie
z.B. SLIP- oder PPP-Verbindungen).  Es holt E-Mail von (weit)
entfernten Mail-Servern abund reicht sie an das Auslieferungssystem
der lokalen Client-Maschine weiter, damit sie dann von normalen MUAs
("mail user agents") wie mutt, elm, pine, (x)emacs/gnus oder mailx
gelesen werden kann.  Ein interaktiver GUI-Konfigurator auch gut
geeignet zum Gebrauch durch Endbenutzer wird mitgeliefert.

%description -l pl
Fetchmail jest programem do �ci�gania poczty ze zdalnych serwer�w
pocztowych. Do �ci�gania poczty mo�e on uzywa� protoko��w POP (Post Office
Protocol) lub IMAP (Internet Mail Access Protocol). �ci�gni�t� poczt�
dostarcza do ko�cowych odbiorc�w poprzez lokalny serwer SMTP.

%description -l tr
fetchmail yaz�l�m�, POP veya IMAP deste�i veren bir sunucuda yer alan
mektuplar�n�z� al�r.

%description -l da
Fetchmail er et gratis, robust, alsidigt og vel-dokumenteret v�rkt�j 
til afhentning og videresending af elektronisk post via TCP/IP
baserede opkalds-forbindelser (s�som SLIP eller PPP forbindelser).   
Den henter post fra en ekstern post-server, og videresender den
til din lokale klient-maskines post-system, s� den kan l�ses af
almindelige mail klienter s�som mutt, elm, pine, (x)emacs/gnus,
eller mailx. Der medf�lger ogs� et interaktivt GUI-baseret
konfigurations-program, som kan bruges af almindelige brugere.

%package -n fetchmailconf
Summary: A GUI configurator for generating fetchmail configuration files
Summary(pt_BR): Um configurador gr�fico para a cria��o de arquivos de configura��o para o fetchmail
Summary(es): Configurador gr�fico para generaci�n de archivos de configuraci�n para fetchmail
Summary(pl): GUI konfigurator do fetchmaila
Summary(fr): GUI configurateur pour fetchmail
Group: Applications/Internet
Group(pt_BR): Aplica��es/Internet
Group(es): Aplicaciones/Internet
Requires: %{name} = %{version}, python

%description -n fetchmailconf
A GUI configurator for generating fetchmail configuration file written in
python

%description -l pt_BR -n fetchmailconf
Um configurador gr�fico para a cria��o de arquivos de configura��o para o fetchmail

%description -l es -n fetchmailconf
Configurador gr�fico para generaci�n de archivos de configuraci�n para fetchmail

%description -n fetchmailconf -l pl
GUI konfigurator do fetchmaila napisany w pythonie.

%prep
%setup -q

%build
CFLAGS="" LDFLAGS="-s" # Add  --enable-nls --without-included-gettext for internationalization
unset LINGUAS
./configure --enable-nls --without-included-gettext --prefix=/usr
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/lib/rhs/control-panel}
make install prefix=$RPM_BUILD_ROOT/usr
cp %{builddir}/rh-config/*.{xpm,init} $RPM_BUILD_ROOT/usr/lib/rhs/control-panel
cp %{builddir}/fetchmail.man $RPM_BUILD_ROOT/usr/man/man1/fetchmail.1
gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/fetchmail.1
cd $RPM_BUILD_ROOT/usr/man/man1
ln -sf fetchmail.1.gz fetchmailconf.1.gz
rm -rf %{builddir}/contrib/RCS
chmod 644 %{builddir}/contrib/*
cp %{builddir}/rh-config/fetchmailconf.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/fetchmailconf





tar xvfpz $RPM_SOURCE_DIR/fetchmail-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (644, root, root, 755)
%doc README NEWS NOTES FAQ COPYING FEATURES sample.rcfile contrib
%doc fetchmail-features.html fetchmail-FAQ.html design-notes.html
/usr/lib/rhs/control-panel/fetchmailconf.xpm
/usr/lib/rhs/control-panel/fetchmailconf.init
/etc/X11/wmconfig/fetchmailconf
%attr(644,root,man) /usr/man/man1/*.1.gz
%attr(644,root,root) /usr/share/locale/*/LC_MESSAGES/fetchmail.mo
%attr(755,root,root) /usr/bin/fetchmail

%files -n fetchmailconf
%attr(755,root,root) /usr/bin/fetchmailconf

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Apr 06 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- prefix to /usr
- fetchmail binary into main package
- final rebuild for 3.0 spanish edition

* Mon Apr 05 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 5.0.0
