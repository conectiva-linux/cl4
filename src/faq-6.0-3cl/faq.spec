Summary: Frequently Asked Questions (FAQ) about Linux.
Summary(pt_BR): FAQ do Linux
Summary(es): FAQ del Linux
Name: faq
%define version 6.0
Version: %{version}
Release: 3cl
Source: ftp://sunsite.unc.edu/pub/Linux/docs/faqs-%{version}.tar.bz2
Copyright: distributable
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
BuildArchitectures: noarch
Buildroot: /var/tmp/faq-root

%description
The faq package includes the text of the Frequently Asked Questions
(FAQ) about Linux from the SunSITE website
(http://sunsite.unc.edu/pub/Linux/docs/faqs/linux-faq/Linux-FAQ).
The Linux FAQ is a great source of information about Linux.

Install faq if you'd like to read the Linux FAQ off your own machine.

%description -l pt_BR
Este é um pacote das Questões Freqüentemente Perguntadas (FAQ)
sobre Linux da sunsite.unc.edu. Ele é uma das melhores fontes de
informação sobre Linux.

%description -l es
Este es un paquete de las Cuestiones Frecuentemente Preguntadas
(FAQ) sobre Linux de la sunsite.unc.edu. Es una de las mejores
fuentes de información sobre Linux.

%prep
%setup -q -n faqs

%build
# kill a dangling symlink
rm -f Wine-FAQ
mv Threads-FAQ/Threads-FAQ-html.tar.gz Threads-FAQ/Threads-FAQ.html.tar.gz

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/doc/FAQ/{txt,html,ps}
for faq in *FAQ ; do
  if [ -d $faq ] ; then
    [ -f $faq/$faq ] && cp $faq/$faq $RPM_BUILD_ROOT/usr/doc/FAQ/txt
    [ -f $faq/$faq.html.tar.gz ] && tar xzvf $faq/$faq.html.tar.gz -C $RPM_BUILD_ROOT/usr/doc/FAQ/html
    [ -f $faq/$faq.ps.gz ] && rm -f $faq/$faq.ps.gz
  else
    cp $faq $RPM_BUILD_ROOT/usr/doc/FAQ/txt
  fi
done

%files
%defattr(-,root,root)
%docdir /usr/doc/FAQ
%dir /usr/doc/FAQ
%attr(-,root,root) /usr/doc/FAQ/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Jun 11 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr 09 1999 Preston Brown <pbrown@redhat.com>
- latest FAQs from metalab.unc.edu

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- rebuilt for 6.0

* Tue Sep 22 1998 Cristian Gafton <gafton@redhat.com>
- updated sources

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- text versions moved under txt dir, so they don't conflict anymore with the
  packages from the 5.0 dist

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu May 07 1998 Erik Troan <ewt@redhat.com>
- changed /usr/doc/FAQ/Linux-FAQ to be directory to match old incarnations
  of the faq package

* Fri May 01 1998 Donnie Barnes <djb@redhat.com>
- added /usr/doc/FAQ as a directory to the file list

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- updated; spec file should now be smarter
- use buildroot

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- updated the faqs
- use install-info

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
