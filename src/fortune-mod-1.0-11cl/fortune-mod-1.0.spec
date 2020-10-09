Summary: fortune cookie program with bug fixes 
Summary(pt_BR): Fortune: frases famosas e ditados
Summary(es): Fortune: frases famosas y refranes
Name: fortune-mod
Version: 1.0
Release: 11cl
Copyright: BSD
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://sunsite.unc.edu/pub/Linux/games/amusements/fortune-mod-9708.tar.bz2
Patch0: fortune-mod-offense.patch
BuildRoot: /var/tmp/fortune-mod-root
Summary(de): Gl�ckskeks-Programm mit Bugfixes
Summary(fr): Programme fortune cookie avec bugs fix�s.
Summary(tr): Rasgele, minik, sevimli mesajlar g�r�nt�ler

%description
This is the ever popular fortune program.  It will gladly print
a random fortune when run.  Is usually fun to put in the .login
for your users on a system so they see something new every time
they log in.

%description -l pt_BR
Este � o popular programa fortune. Ele ir� alegremente imprimir
um ditado aleat�rio quando rodar. � geralmente engra�ado coloc�-lo
no .login para os seus usu�rios para que eles vejam algo novo toda
vez que entrarem.

%description -l es
Este es el popular programa fortune. Ir� satisfactoriamente imprimir
un dictado aleatorio cuando se ejecute. Generalmente, es gracioso
ponerlo en el .login para sus usuarios, para que vean algo nuevo
cuuando entren.

%description -l de
Dies ist das beliebte Gl�ckskeks-Programm. Es druckt eine zuf�llige
Weisheit. Wenn Sie es in die .login-Datei Ihrer Benutzer schreiben,
erhalten diese bei jedem Anmelden einen neuen Spruch.

%description -l fr
Le c�l�bre programme fortune. Il affiche joyeusement un dicton
al�atoire lorsqu'il est lanc�. Il est g�n�ralement amusant de le
placer dans le .login des utilisateurs d'un syst�me pour qu'ils
voient quelque chose de nouveau � chaque fois qu'ils se loggent.

%description -l tr
Fortune, her �a�r�ld���nda b�y�k bir kitapl�ktan rasgele se�ece�i, e�lenceli
bir metni g�r�nt�leyecektir. A��r� bilimsel ve yararl� bir uygulama olmamas�na
kar��n kullan�c�lar�n her sisteme ba�lan���nda de�i�ik bir mesajla
kar��la�malar�n� sa�lar.

%prep
%setup -q -n fortune-mod-9708
%patch0 -p1

%build
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{games,sbin,man/man1,man/man6,share/games/fortune}

make	FORTDIR=$RPM_BUILD_ROOT/usr/games \
	COOKIEDIR=$RPM_BUILD_ROOT/usr/share/games/fortunes \
	BINDIR=$RPM_BUILD_ROOT/usr/sbin \
	BINMANDIR=$RPM_BUILD_ROOT/usr/man/man1 \
	FORTMANDIR=$RPM_BUILD_ROOT/usr/man/man6 \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog TODO
/usr/games/fortune
/usr/sbin/strfile
/usr/sbin/unstr
/usr/share/games/fortunes
/usr/man/man6/fortune.6
/usr/man/man1/strfile.1
/usr/man/man1/unstr.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Nov 04 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- new version
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
