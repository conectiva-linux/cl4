Name: sndconfig
Version: 0.29
Release: 10cl
Copyright: distributable
Summary: Red Hat Sound Configuration tool
Summary(pt_BR): Ferramenta de configuração de som.
Summary(es): Herramienta de configuración de sonido.
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Source: sndconfig-%{PACKAGE_VERSION}.tar.gz
Source1: sndconfig-pt_BR.po
Source2: sndconfig-es.po
%ifarch i386 alpha
Source700: sndconfig-man-pt_BR.tar
Requires: isapnptools >= 1.16
Requires: sox
Requires: awesfx
%endif
BuildRoot: /tmp/rhsound
ExclusiveArch: i386 sparc alpha

%description
The Red Hat sound package includes the sndconfig tool whichs
is a text based sound configuration tool.  You can use
it to set the proper sound type for programs which use the
devices /dev/dsp, /dev/audio, and /dev/mixer.  Sound settings 
are saved via the use of aumix and sysV runlevel scripts.

%description -l pt_BR
Inclui o programa sndconfig que é uma ferramenta baseada em texto
para configuração de som. Você pode usá-lo para configurar o tipo de
som para programas que usam os dispositivos /dev/dsp, /dev/audio,
e /dev/mixer. As configurações de som são salvas com o aumix e
scripts runlevel sysV.

%description -l es
Incluye el programa sndconfig que es una herramienta basada en
texto para configuración de sonido. Puedes usarlo para configurar
el tipo de sonido para programas que usan los dispositivos /dev/dsp,
/dev/audio, y /dev/mixer. Las configuraciones de sonido son guardadas
con el aumix y scripts runlevel sysV.

%prep
%setup -n sndconfig
cp $RPM_SOURCE_DIR/sndconfig-pt_BR.po po/pt_BR.po
cp $RPM_SOURCE_DIR/sndconfig-es.po    po/es.po

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{sbin,man/man8}
mkdir -p $RPM_BUILD_ROOT/usr/share/locale
make prefix=$RPM_BUILD_ROOT/usr install



mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/sndconfig-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
/usr/sbin/sndconfig
%ifarch i386 alpha
/usr/sbin/pnpprobe
/usr/man/man8/pnpprobe.8
%endif
/usr/share/sndconfig/sample.au
/usr/share/locale/*/*/sndconfig.mo
/usr/man/man8/sndconfig.8
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 31 1999 Conectiva <dist@conectiva.com>
- added spanish po

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Feb  3 1999 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Jan 28 1999 Bill Nottingham <notting@redhat.com>
- make everything use two dma= parameters

* Mon Jan 24 1999 Bill Nottingham <notting@redhat.com>
- card lists weren't in sync
- fix pci probing bug

* Sun Jan 10 1999 Bill Nottingham <notting@redhat.com>
- build against gpm (new newt)

* Mon Jan  4 1999 Bill Nottingham <notting@redhat.com>
- more PnP fixes (Opti PnP, CMI8330)
- require newer isapnptools so we don't run into LD bug.

* Mon Dec 28 1998 Bill Nottingham <notting@redhat.com>
- large pile of PnP fixes (Opti, SGalaxy, SSVIVO, ESS1868, others....)
- bump version to 0.29

* Thu Dec  3 1998 Bill Nottingham <notting@redhat.com>
- fix for SoundScape VIVO...

* Mon Nov 16 1998 Bill Nottingham <notting@redhat.com>
- awesfx goes in /bin

* Mon Nov  2 1998 Bill Nottingham <notting@redhat.com>
- added hack to make it less likely to lock up alphas

* Fri Oct 30 1998 Bill Nottingham <notting@redhat.com>
- stupid programmer error, part deux

* Thu Oct 22 1998 Bill Nottingham <notting@redhat.com>
- build for Raw Hide (slang-1.2.2)
- now for alpha
- organize by bus, not platform

* Wed Oct 14 1998 Cristian Gafton <gafton@redhat.com>
- translation updates

* Mon Oct 12 1998 Bill Nottingham <notting@redhat.com>
- fixes to lists of resources
- add more translations
- don't set auto-unload

* Thu Oct  8 1998 Bill Nottingham <notting@redhat.com>
- oops, forgot a newtResume()
- make /etc/conf.modules mode 0644, not 0600
- merge SBPCI entries with ES1370, since we can't tell them apart anyways

* Fri Oct  2 1998 Bill Nottingham <notting@redhat.com>
- added scrollbar to card list
- updated to 0.26

* Wed Sep 30 1998 Bill Nottingham <notting@redhat.com>
- fixes for AudioTrix Pro, add OPL3-SA2/3/x
- assorted random bugfixes
- add Turkish translations (from H. Turgut Uyar <uyar@cs.itu.edu.tr>)
- add Romanian translations

* Thu Sep 24 1998 Bill Nottingham <notting@redhat.com>
- add a few more cards
- disable Wavefront support for now

* Thu Sep 24 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- i18n patches

* Wed Sep 23 1998 Bill Nottingham <notting@redhat.com>
- fix PCI-probing bug

* Tue Sep 22 1998 Bill Nottingham <notting@redhat.com>
- when merging isapnp.conf changes, use current preamble

* Fri Sep 18 1998 Bill Nottingham <notting@redhat.com>
- check that they actually have modular sound

* Fri Sep 11 1998 Bill Nottingham <notting@redhat.com>
- PCI probing!

* Tue Sep  8 1998 Bill Nottingham <notting@redhat.com>
- SPARC support.

* Wed Aug 26 1998 Bill Nottingham <notting@redhat.com>
- YABF

* Tue Aug 25 1998 Bill Nottingham <notting@redhat.com>
- fixed bad logic w/midi assignment

* Fri Aug 21 1998 Bill Nottingham <notting@redhat.com>
- fixed message segfault

* Thu Aug 20 1998 Bill Nottingham <notting@redhat.com>
- changed bug reporting address

* Wed Aug 19 1998 Bill Nottingham <notting@redhat.com>
- introduce support for non SB sound cards

* Sun Aug 02 1998 Erik Troan <ewt@redhat.com>
- built aginst newt 0.30

* Tue May 05 1998 Cristian Gafton <gafton@redhat.com>
- fixed problem with overwriting the conf.modules file

* Tue Dec 30 1997 Erik Troan <ewt@redhat.com>
- fixed problem w/ free()ing bad pointers

* Fri Dec 19 1997 Erik Troan <ewt@redhat.com>
- general Makefile cleanups

* Fri Nov  7 1997 Michael Fulbright <msf@redhat.com>
- fixed bug in reading current settings from conf.modules

* Fri Oct 31 1997 Michael Fulbright <msf@redhat.com>
- fixed behavior to work with rhsound service
- added support for midi in conf.modules, isapnp.conf
- reduced duplicate info stored in /etc/sysconfig/sound

* Wed Oct 29 1997 Mike Wangsmo <wanger@redhat.com>
- removed README's from tarball and coverted to buildroot

* Thu Oct 24 1997 Michael Fulbright <msf@redhat.com>
- added some docs on the sound modules

* Tue Oct 22 1997 Michael Fulbright <msf@redhat.com>
- changed sound sample to linux d00d instead of gorby d00d

* Tue Oct 14 1997 Michael Fulbright <msf@redhat.com>
- fixed creation of temporary files to be more secure.

* Mon Oct  6 1997 Michael Fulbright <msf@redhat.com>
- added man page

* Fri Oct  3 1997 Michael Fulbright <msf@redhat.com>
- first version

