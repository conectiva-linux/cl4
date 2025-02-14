Summary: Provides diff file statistics
Summary(pt_BR): Mostra estat�sticas em arquivos diff
Summary(es): Ense�a estad�sticas en archivos diff
Name: diffstat
Version: 1.25
Release: 9cl
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Copyright: distributable
Prefix: /usr
Source: ftp.clark.net:/pub/dickey/diffstat/diffstat-1.25.tgz
BuildRoot: /var/tmp/diffstat-root
Summary(de): Liefert diff-Datei-Statistiken
Summary(fr): Fournit des statistiques sur les diff�rences de fichiers.
Summary(tr): diff dosyas� istatistik bilgileri ��kar�r

%description
'diffstat' provides a number of statistics on a patch generated by diff,
including number of additions, number of removals, and total number of
changes. It can be useful, for example, to find out what changes have been
made to a program, just by feeding the update patch to diffstat.

%description -l pt_BR
'diffstat' oferece v�rias estat�sticas em um patch gerado por
diff, incluindo muitas adi��es, v�rias remo��es e v�rias outras
mudan�as. Ele pode ser �til, por exemplo, para descobrir que mudan�as
foram feitas em um programa, somente fornecendo o patch atualizado
para diffstat.

%description -l es
'diffstat' nos ofrece varias estad�sticas en un patch creado por
diff, incluyendo muchas adiciones, varias remociones y varios
otros cambios. Puede ser �til, por ejemplo, para descubrir que
cambios fueron hechos en un programa, solamente ofreciendo el patch
actualizado para diffstat.

%description -l de
'diffstat' stellt eine Reihe von statistischen Informationen f�r mit 
Patch erzeugte Diffs bereit, u.a. die Zahl der Einf�gungen, der Streichungen
sowie die Gesamtzahl der �nderungen. So ist es m�glich, die �nderungen an 
einem Programm zu ermitteln, indem man das Update-Patch durch diffstat
durchlaufen l��t. 

%description -l fr
� diffstat � offre de nombreuses statistiques sur un patch g�n�r� par diff,
cela comprend le nombre d'ajouts, de suppressions et le nombre total de
modifications. Il peut �tre utile, par exemple, de retrouver les modifications
faites � un programme en fournissant uniquement le patch de mise � jour �
diffstat.

%description -l tr
diffstat program�, diff taraf�ndan �retilen bir yama �zerinden toplama
say�s�, ��karma say�s�, toplam de�i�iklik say�s� gibi baz� istatistiksel
bilgiler ��kart�r.

%prep
%setup -q

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/diffstat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/diffstat
/usr/man/man1/diffstat.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
