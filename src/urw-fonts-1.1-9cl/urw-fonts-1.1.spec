Summary: Free versions of the 35 standard PostScript fonts.
Summary(pt_BR): Mais fontes para o X
Summary(es): Más fuentes para X
Name: urw-fonts
Version: 1.1
Release: 9cl
Source: http://www.gimp.org/urw-fonts.tar.gz
License: GPL, URW holds copyright
Group: User Interface/X
Group(pt_BR): Interface do Usuário/X
Group(es): Interfaz del Usuario/X
URL: http://www.gimp.org/fonts.html
BuildRoot: /var/tmp/URW-root
BuildArchitectures: noarch
Prereq: chkfontpath

%description 
Free versions of the 35 standard PostScript fonts. With newer releases
of ghostscript quality versions of the standard 35 Type 1 PostScript
fonts are shipped. They were donated and licenced under the GPL by
URW. The fonts.dir was specially made to match the original Adobe
names of the fonts, e.g. Times, Helvetica etc. With X, LaTeX, or Ghostscript,
these fonts are a must to have!

%description -l pt_BR
Versões distribuíveis de 35 fontes padrão PostScript. As novas versões
do ghostscript vem com as 35 fontes padrão tipo 1 PostScript de melhor
qualidade. Eles foram doados e licenciados sob a GPL pela URW. O arquivo
fonts.di foi feito especialmente para ficar igual aos nomes originais
da Adobe para as fontes, ex.: Times, Helvetica, etc. No XFree86 estas
fontes são muito interessantes!

%description -l es
Versiones distribuibles de 35 fuentes padrón PostScript. Las nuevas
versiones del ghostscript vienen con las 35 fuentes padrón tipo 1
PostScript de mejor calidad. Fueron donados y licenciados bajo la GPL
por  URW. El archivo fonts.di se hizo especialmente para quedar igual
a los nombres originales del Adobe para las fuentes, ej.: Times,
Helvética, etc. ¡En el XFree86 estas fuentes son mucho interesantes!

%prep
%setup -q -n URW

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/fonts/default/Type1
cp -f *.afm *.pfm *.pfb $RPM_BUILD_ROOT/usr/share/fonts/default/Type1
install -m 644 fonts.dir_fndry_is_urw \
	$RPM_BUILD_ROOT/usr/share/fonts/default/Type1/fonts.dir
cd $RPM_BUILD_ROOT/usr/share/fonts/default/Type1 && \
	ln -s fonts.dir fonts.scale

%post
/usr/sbin/chkfontpath -q -a /usr/share/fonts/default/Type1 2> /dev/null || :

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/chkfontpath -q -r /usr/share/fonts/default/Type1
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%dir /usr/share/fonts/default/Type1
%config /usr/share/fonts/default/Type1/fonts.dir
/usr/share/fonts/default/Type1/fonts.scale
/usr/share/fonts/default/Type1/*.afm
/usr/share/fonts/default/Type1/*.pfb
/usr/share/fonts/default/Type1/*.pfm

%changelog
* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Re-enabled the use of chkfontpath in this package
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 29 1999 Conectiva <dist@conectiva.com>
- removed chkfontpath from scripts

* Sat Mar 27 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- fix %post script error

* Sat Mar 27 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Mar 24 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- fixed up chkfontpath stuff

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Feb 15 1999 Preston Brown <pbrown@redhat.com>
- added missing fonts.dir, fonts.scale, %post, %postun using chkfontpath
- changed foundary from Adobe (which was a lie) to URW.

* Sat Feb 06 1999 Preston Brown <pbrown@redhat.com>
- fonts now live in /usr/share/fonts/default/Type1

* Fri Nov 13 1998 Preston Brown <pbrown@redhat.com>
- eliminated section that adds to XF86Config
- changed fonts to reside in /usr/share/fonts/default/URW, so they can be
  shared between X and Ghostscript (and other, future programs/applications)

* Fri Sep 11 1998 Preston Brown <pbrown@redhat.com>
- integrate adding fontdir to XF86Config

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- eliminate %post output

* Wed Jul  8 1998 Jeff Johnson <jbj@redhat.com>
- create from Stefan Waldherr <swa@cs.cmu.edu> contrib package.
