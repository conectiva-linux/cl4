Summary: Utility programs for the AWE32 sound driver.
Summary(pt_BR): Programas utilitários para o driver de som AWE32
Summary(es): Programas utilitarios para el driver de sonido AWE32
Name: awesfx
Version: 0.4.3a
Release: 3cl
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
URL: http//bahamut.mm.t.u-tokyo.ac.jp/~iwai/awedrv/index.html
Source: http://bahamut.mm.t.u-tokyo.ac.jp/~iwai/awedrv/awesfx-%{version}.tgz
Source2: http://www.pvv.org/~thammer/localfiles/soundfonts_other/gu11-rom.zip
Source3: awe_voice.h
Patch: awesfx-0.4.3a-make.patch
Copyright: GPL/distributable
Prefix: /usr
ExclusiveArch: i386 alpha
BuildRoot: /var/tmp/awesfx-root
%description
The awesfx package contains necessary utilities for the AWE32
sound driver.

If you must use an AWE32 sound driver, you should install
this package.

%description -l pt_BR
O awesfx inclui alguns utilitários para o driver de som AWE32.
Você precisa destes utilitários para habilitar corretamente os sons
no driver.  Este pacote inclui uma fonte de som que é um substituto
para o arquivo synthgm.sbk que vem com a SB AWE32.

%description -l es
wesfx incluye algunos utilitarios para el driver de sonido AWE32.
Necesitas de estos utilitarios para habilitar correctamente los
sonidos en el driver.  Este paquete incluye una fuente de sonido
que es un substituto al archivo synthgm.sbk que viene con SB AWE32.

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Injected new group into package

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Tue Mar  9 1999 Bill Nottingham <notting@redhat.com>
- update to 0.4.3a

* Mon Nov 16 1998 Bill Nottingham <notting@redhat.com>
- sfxload needs to be on root partition (modules loaded at startup)

* Thu Oct 22 1998 Bill Nottingham <notting@redhat.com>
- build for Alpha

* Wed Sep  9 1998 Bill Nottingham <notting@redhat.com>
- initial packaging

%prep
%setup
mkdir gu11-rom
cd gu11-rom
unzip $RPM_SOURCE_DIR/gu11-rom.zip
cd ..
%patch -p1
mkdir include/linux
cp $RPM_SOURCE_DIR/awe_voice.h include/linux

%build
xmkmf
make Makefiles
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{man/man1,bin}
mkdir -p $RPM_BUILD_ROOT/etc/midi
mkdir -p $RPM_BUILD_ROOT/bin
make install
make install.man
mv $RPM_BUILD_ROOT/usr/bin/sfxload $RPM_BUILD_ROOT/bin/
mv gu11-rom/GU11-ROM.SF2 $RPM_BUILD_ROOT/etc/midi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog.sfx README SBKtoSF2.txt bank-samples
%doc gu11-rom
/etc/midi/GU11-ROM.SF2
/bin/sfxload
/usr/bin/setfx
/usr/bin/sf2text
/usr/bin/text2sf
/usr/bin/gusload
/usr/bin/sfxtest
/usr/man/man1/sfxload.1
