Summary: Various HOWTOs from the Linux Documentation Project
Summary(pt_BR): V�rios HOWTOs do Projeto de Documenta��o do Linux (LDP)
Summary(es): Varios HOWTOs del Proyecto de Documentaci�n del Linux (LDP)
Name: howto
%define version 6.0
Version: %{version}
Release: 4cl
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n
Source0: HOWTO-%{version}.tar.bz2
Source1: HOWTO-pt_BR.tar.bz2
Source2: HOWTO-es.tar.bz2
Copyright: distributable
BuildRoot: /var/tmp/howto-root
BuildArchitectures: noarch
Obsoletes: ldp

%description
This is the best collection of Linux documentation there is.  It
was put together on Jan 27 1999.  If you want to find newer
versions of these documents, see http://sunsite.unc.edu/linux.
For the versions in this package, see /usr/doc/HOWTO.

%description -l pt_BR
Esta � a melhor cole��o existente de documentos Linux. Se voc�
deseja encontrar as vers�es mais recentes destes documentos
veja em http://sunsite.unc.edu/Linux. As vers�es neste pacote
est�o no diret�rio /usr/doc/HOWTO.

%description -l es
Esta es la mejor colecci�n existente de documentos Linux. Si deseas
encontrar las versiones m�s recientes de estos documentos mira en
http://sunsite.unc.edu/Linux. Las versiones en este paquete est�n
en el directorio /usr/doc/HOWTO.

%package html
Summary: html versions of the HOWTOs
Summary(pt_BR): Vers�es html dos HOWTOs
Summary(es): Versiones html de los HOWTOs
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n

%description html
These are the html versions of the HOWTOs.  You can view them 
with your favorite web browser.

%description -l pt_BR html
Esta � uma vers�o html dos HOWTOs. Voc� pode visualiz�-los com seu
navegador web favorito.

%description -l es html
Esta es una versi�n html de los HOWTOs. Puedes visualizarlos con
tu navegador web favorito.

%package sgml
Summary: sgml source versions of the HOWTOs
Summary(pt_BR): Vers�es em sgml dos HOWTOs (fontes)
Summary(es): Versiones en sgml de los HOWTOs (fuentes)
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n

%description sgml
These are the SGML versions of the HOWTOs.  They are the ``source''
files that the HOWTOs are built from (using linuxdoc-sgml).

%description -l pt_BR sgml
Esta � uma vers�o SGML dos HOWTOs. Eles s�o os arquivos "fontes"
de onde os HOWTOs s�o constru�dos (usando Linuxdoc-sgml).

%description -l es sgml
Esta es una versi�n SGML de los HOWTOs. Son los archivos "fuentes"
a partir de cuales los HOWTOs se construyen (usando Linuxdoc-sgml).

%package spanish
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n
Summary: Spanish versions of the HOWTO documents
Summary(pt_BR): Tradu��es de alguns HOWTOs para Espanhol
Summary(es): Traducciones de algunos HOWTOs para Espa�ol
Obsoletes: howto-translations

%description spanish
This package contains translated versions of the Linux HOWTO into spanish.
Please note that not all the files have been translated, so you most likely
will need the english version installed if you want to have a complete HOWTO
install.

%description -l pt_BR spanish
Tradu��es de alguns HOWTOs para Espanhol

%description -l es spanish
Traducciones de algunos HOWTOs para Espa�ol

%package portuguese
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n
Summary: Portuguese versions of the HOWTO documents
Summary(pt_BR): HOWTOS em Portugu�s
Summary(es): HOWTOS en Portugu�s
Obsoletes: howto-translations

%description portuguese
This package contains translated versions of the Linux HOWTO into portuguese.
Please note that not all the files have been translated, so you most likely
will need the english version installed if you want to have a complete HOWTO
install.

%description -l pt_BR portuguese
Este pacote cont�m alguns HOWTOs traduzidos para o portugu�s.
Inclui tamb�m o "The Linux Manual" do Hugo Cisneiros.

%description -l es portuguese
Este paquete contiene varios HOWTOs traducidos al portugu�s.
Incluye tambi�n el "The Linux Manual" de Hugo Cisneiros.

%prep 
%setup -T -c

%build
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/doc/HOWTO
chmod 755 $RPM_BUILD_ROOT/usr/doc/HOWTO

(cd $RPM_BUILD_ROOT/usr/doc
bunzip2 -cd $RPM_SOURCE_DIR/HOWTO-%{version}.tar.bz2 | tar xvf -
bunzip2 -cd $RPM_SOURCE_DIR/HOWTO-pt_BR.tar.bz2 | tar xvf -
bunzip2 -cd $RPM_SOURCE_DIR/HOWTO-es.tar.bz2 | tar xvf -
cd HOWTO
rm -f Linux-HOWTOs.tar.gz
#the mini howtos are again a nightmare
rm -f mini/*.tar.gz
mv mini/other-formats/html other-formats/html/mini
mv mini/other-formats/sgml other-formats/sgml/mini
rm -rf mini/other-formats
find . -type f -name "*gz" | while read f ; do
    case $f in 
	*.tar.gz | *.tgz )
	    tar -zxf $f -C $(dirname $f)
	    rm -f $f
	    ;;
	*.dvi.gz | *.ps.gz | *.pdf.gz )
	    echo "$f is left compressed"
	    ;;
	*.gz )
	    gunzip -f $f
	    rm -f $f
	    ;;
	* )
	    echo "This should not happen !"
	    ;;
    esac
done

)

%install
cd $RPM_BUILD_ROOT/usr/doc/HOWTO
find . -type f | xargs chmod 644
find . -type d | xargs chmod 755

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/doc/HOWTO/*HOWTO
/usr/doc/HOWTO/mini
/usr/doc/HOWTO/HOWTO-INDEX
/usr/doc/HOWTO/INFO-SHEET
/usr/doc/HOWTO/META-FAQ
/usr/doc/HOWTO/README
/usr/doc/HOWTO/unmaintained

%files sgml
%defattr(-,root,root)
%dir /usr/doc/HOWTO
%dir /usr/doc/HOWTO/other-formats
/usr/doc/HOWTO/other-formats/sgml

%files html
%defattr(-,root,root)
%dir /usr/doc/HOWTO
%dir /usr/doc/HOWTO/other-formats
/usr/doc/HOWTO/other-formats/html

%files spanish
%defattr(-,root,root)
%dir /usr/doc/HOWTO
%dir /usr/doc/HOWTO/translations
/usr/doc/HOWTO/translations/es
/usr/doc/HOWTO/translations/spanish

%files portuguese
%defattr(-,root,root)
%dir /usr/doc/HOWTO
%dir /usr/doc/HOWTO/translations
/usr/doc/HOWTO/translations/pt_BR
/usr/doc/HOWTO/translations/brazilian_portuguese
/usr/doc/HOWTO/TheLinuxManual

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Injected new group into package

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Mar 17 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Atualizados HOWTOs em Ingl�s e espanhol

* Fri Dec 11 1998 Conectiva <dist@conectiva.com>
- atualizados alguns howtos
- final rebuild for 3.0

* Wed Dec 02 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- Atualizados v�rios HOWTOS
- Inclu�do o TheLinuxManual

* Sun Nov 22 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- added Portuguese-Howto 3.0

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations
