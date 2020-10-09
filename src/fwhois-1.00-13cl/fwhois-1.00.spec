Summary: finger-style whois 
Summary(pt_BR): Whois parecido com sa�da do finger
Summary(es): Whois parecido con salida del finger
Name: fwhois
Version: 1.00
Release: 13cl
Copyright: BSD
Group: Applications/Internet
Group(pt_BR): Aplica��es/Internet
Group(es): Aplicaciones/Internet
Source: ftp://sunsite.unc.edu/pub/Linux/distributions/slackware/source/n/tcpip/fwhois-1.00.tar.gz
Buildroot: /var/tmp/fwhois-root
Summary(de): Finger-artiges whois
Summary(fr): Un whois dans le style finger.
Summary(tr): finger tarz� whois

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%description
This is the ``whois'' program.  It will allow you to find out
information on people stored in the whois databases around 
the world.

%description -l pt_BR
Este � o programa "whois". Ele permite achar informa��es sobre
pessoas armazenadas nos bancos de dados "whois" do mundo inteiro.

%description -l es
Este es el programa "whois". Permite encontrar informaci�n sobre
Personas, almacenadas en los bancos de datos "whois" de todo
el mundo.

%description -l de
Dies ist das 'WHOIS'-Programm. Es gestattet Ihnen, in den 
Whois-Datenbanken rund um die Welt nach Personen zu suchen. 

%description -l fr
Programme � whois �. Il vous permet d'obtenir des informations sur les
personnes r�pertori�es dans les bases de donn�es whois de part le monde.

%description -l tr
whois ile d�nyadaki whois veri tabanlar�nda kayd� bulunan ki�iler hakk�nda
bilgi edinebilirsiniz.

%prep
%setup -q

%build
gcc $RPM_OPT_FLAGS -s fwhois.c -o fwhois

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -s -m755 fwhois $RPM_BUILD_ROOT/usr/bin/fwhois
ln -sf fwhois $RPM_BUILD_ROOT/usr/bin/whois

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
/usr/bin/fwhois
/usr/bin/whois
