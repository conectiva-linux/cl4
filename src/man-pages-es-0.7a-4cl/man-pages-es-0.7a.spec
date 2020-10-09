Summary: System manual pages - Spanish versions
Summary(pt_BR): P�ginas de manual, do Projeto de Documenta��o do Linux (LDP) - Vers�es em espanhol
Summary(es): P�ginas de manual del Proyecto de Documentaci�n del Linux (LDP) - Versi�n en espa�ol
Name: man-pages-es
Version: 0.7a
Release: 4cl
Copyright: Varios (distributable)
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n
Source: http://www.ditec.um.es/~piernas/manpages-es/man-pages-es-0.7a.tar.gz
BuildRoot: /usr/tmp/man-pages-es-root
Icon: books-es.gif
URL: http://www.ditec.um.es/~piernas/manpages-es/
BuildArchitectures: noarch
Requires: mktemp, man >= 1.4
Obsoletes: manpages-es

%description
A large collection of man pages covering programming APIs, file
formats, protocols, etc.

    Section 1 = user commands (intro only)
    Section 2 = system calls
    Section 3 = libc calls
    Section 4 = devices (e.g., hd, sd)
    Section 5 = file formats and protocols (e.g., wtmp, /etc/passwd, nfs)
    Section 6 = games (intro only)
    Section 7 = conventions, macro packages, etc. (e.g., nroff, ascii)
    Section 8 = system administration (intro only)

This is the translation to spanish of the Linux man pages.

%description -l pt_BR
Uma larga cole��o de p�ginas de manuais cobrindo programa��o APIs,
formatos de arquivos, protocolos, etc.

    Se��o 1 = comandos de usu�rio (somente introdu��o)
    Se��o 2 = chamadas de sistema
    Se��o 3 = chamadas libc
    Se��o 4 = dispositivos (ex.: hd, sd)
    Se��o 5 = formatos de arquivos e protocolos (ex: wtmp, /etc/passwd, nfs)
    Se��o 6 = jogos (somente introdu��o)
    Se��o 7 = conven��es, pacotes de macros, etc. (ex: nroff, ascii)
    Se��o 8 = administra��o de sistema (somente introdu��o)

Estas s�o as p�ginas de manual do Linux, em espanhol.

%description -l es
P�ginas de manual en espa�ol para Linux. Esta versi�n traduce la versi�n
1.22 de las p�ginas de manual en ingl�s y a�ade otras p�ginas procedentes
de otros paquetes (vea el fichero /usr/doc/man-pages-es-0.7a/EXTRA para m�s
informaci�n). Como podr� comprobar, se trata de una versi�n alfa por lo que
puede encontrar bastantes errores. Cualquier sugerencia, correcci�n o
cr�tica constructiva ser� bien recibida. Puede ponerse en contacto con el
responsable del proyecto enviando un e-mail a piernas@ditec.um.es. Para m�s
informaci�n, lea los ficheros LEEME y PROYECTO que encontrar� en el
directorio /usr/doc/man-pages-es-0.7a.

%prep

%setup -n man-pages-es-%{PACKAGE_VERSION}

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/man/es/man{1,2,3,4,5,6,7,8}
mkdir -p $RPM_BUILD_ROOT/var/catman/es/cat{1,2,3,4,5,6,7,8}
make MANDIR=$RPM_BUILD_ROOT/usr/man/es

gzip -9f $RPM_BUILD_ROOT/usr/man/es/man{1,2,3,4,5,6,7,8}/*

%clean
rm -r $RPM_BUILD_ROOT

%files
%doc PROYECTO LEEME EXTRA
%dir /usr/man/es
/usr/man/es/man?
/var/catman/es

%changelog
* Wed Jun 23 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- compressed all man pages
