Summary: System manual pages - Spanish versions
Summary(pt_BR): Páginas de manual, do Projeto de Documentação do Linux (LDP) - Versões em espanhol
Summary(es): Páginas de manual del Proyecto de Documentación del Linux (LDP) - Versión en español
Name: man-pages-es
Version: 0.7a
Release: 4cl
Copyright: Varios (distributable)
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
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
Uma larga coleção de páginas de manuais cobrindo programação APIs,
formatos de arquivos, protocolos, etc.

    Seção 1 = comandos de usuário (somente introdução)
    Seção 2 = chamadas de sistema
    Seção 3 = chamadas libc
    Seção 4 = dispositivos (ex.: hd, sd)
    Seção 5 = formatos de arquivos e protocolos (ex: wtmp, /etc/passwd, nfs)
    Seção 6 = jogos (somente introdução)
    Seção 7 = convenções, pacotes de macros, etc. (ex: nroff, ascii)
    Seção 8 = administração de sistema (somente introdução)

Estas são as páginas de manual do Linux, em espanhol.

%description -l es
Páginas de manual en español para Linux. Esta versión traduce la versión
1.22 de las páginas de manual en inglés y añade otras páginas procedentes
de otros paquetes (vea el fichero /usr/doc/man-pages-es-0.7a/EXTRA para más
información). Como podrá comprobar, se trata de una versión alfa por lo que
puede encontrar bastantes errores. Cualquier sugerencia, corrección o
crítica constructiva será bien recibida. Puede ponerse en contacto con el
responsable del proyecto enviando un e-mail a piernas@ditec.um.es. Para más
información, lea los ficheros LEEME y PROYECTO que encontrará en el
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
