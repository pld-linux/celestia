Summary:	A real-time visual space simulation
Summary(pl):	Symulacja przestrzeni kosmicznej w czasie rzeczywistym
Name:		celestia
Version:	1.3.0
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/celestia/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-solar-%{version}.tar.gz
URL:		http://www.shatters.net/celestia/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	glut-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	OpenGL-devel
Requires:	OpenGL
Requires:	%{name}-extrasolar
Requires:	%{name}-stars
Requires:	%{name}-generator
Requires:	%{name}-textures-mercury
Requires:	%{name}-textures-venus
Requires:	%{name}-textures-earth
Requires:	%{name}-textures-earth-clouds
Requires:	%{name}-textures-moon
Requires:	%{name}-textures-mars
Requires:	%{name}-textures-jupiter
Requires:	%{name}-textures-galileanmoons
Requires:	%{name}-textures-saturn
Requires:	%{name}-textures-triton
Requires:	%{name}-textures-pluto
Obsoletes:	%{name}-textures-stars
Obsoletes:	%{name}-asterisms
Obsoletes:	%{name}-galaxies
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
Celestia is a free real-time space simulation that lets you experience
our universe in three dimensions. Unlike most planetarium software,
Celestia doesn't confine you to the surface of the Earth. You can
travel throughout the solar system, to any of over 100,000 stars, or
even beyond the galaxy. All travel in Celestia is seamless; the
exponential zoom feature lets you explore space across a huge range of
scales, from galaxy clusters down to spacecraft only a few meters
across. A 'point-and-goto' interface makes it simple to navigate
through the universe to the object you want to visit.

%description -l pl
Celestia to wolny symulator przestrzeni komicznej w czasie
rzeczywistym, który pozwala do¶wiadczaæ naszego Wszech¶wiata w trzech
wymiarach. W odró¿nieniu od innych programów planetarnych Celestia nie
przywi±zuje Ciê do powierzchni ziemi. Mo¿esz podró¿owaæ przez Uk³ad
S³oneczny do ponad 100,000 gwiazd lub nawet poza galaktykê. Wszystkie
podró¿e w Celestii s± niezauwa¿alne; funkcja wyk³adniczego
przybli¿enia pozwala Ci odkrywaæ Kosmos w ró¿nych skalach - od
spojrzenia na galaktyki do widoku kilkumetrowych statków kosmicznych.
Interfejs typu 'poka¿-i-leæ' czyni nawigacjê przez Wszech¶wiat prost±.

%package task-default
Summary:	Default packages for celestia
Summary(pl):	Domy¶lne pakiety dla celestii
Group:		X11/Applications/Science
Requires:	%{name}-extrasolar-default
Requires:	%{name}-stars-default
Requires:	%{name}-textures-mercury-default
Requires:	%{name}-textures-venus-default
Requires:	%{name}-textures-earth-default
Requires:	%{name}-textures-earth-clouds-default
Requires:	%{name}-textures-moon-default
Requires:	%{name}-textures-mars-default
Requires:	%{name}-textures-jupiter-default
Requires:	%{name}-textures-galileanmoons-default
Requires:	%{name}-textures-saturn-default
Requires:	%{name}-textures-triton-default
Requires:	%{name}-textures-pluto-default

%description task-default
Default packages for celestia. This metapackage contains no files
and can be safely uninstalled after installation.

%description task-default -l pl
Domy¶lne pakiety dla celestii. Ten metapakiet nie zawiera ¿adnych
plików i mo¿e zostaæ usuniêty po instalacji.

%package generator
Summary:	Hack needed because rpm sucks
Summary(pl):	Hack potrzebny z powodu obsysania rpm-a
Group:		X11/Applications/Science

%description generator
Generates solarsys.ssc.

%descreption generator -l pl
Tworzy solarsys.ssc.

%package extrasolar-default
Summary:	Catalog of known extrasolar planetary systems
Summary(pl):	Katalog znanych uk³adów planetarnych
Group:		X11/Applications/Science
Requires:	%{name}
Provides:	%{name}-extrasolar
Obsoletes:	%{name}-extrasolar

%description extrasolar-default
Catalog of known extrasolar planetary systems.

%description extrasolar-default -l pl
Katalog znanych uk³adów planetarnych.

%package stars-default
Summary:	Database with 100 000 stars
Summary(pl):	Baza danych 100 000 gwiazd
Group:		X11/Applications/Science
Requires:	%{name}
Provides:	%{name}-stars
Obsoletes:	%{name}-stars

%description stars-default
Initial Stars database (with about 100 000 Hipparcos stars).

%description stars-default -l pl
Podstawowa baza danych gwiazd (z oko³o 100 000 gwiazd zbadanych
przez sondê kosmiczn± Hipparcos).

%package textures-mercury-default
Summary:	1k Mercury textures
Summary(pl):	Tekstury Merkurego o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-mercury
Obsoletes:	%{name}-textures-mercury

%description textures-mercury-default
1k Mercury textures.

%description textures-mercury-default -l pl
Tekstury Merkurego o wielko¶ci 1024 x 512.

%package textures-mercury-bumpmap-default
Summary:	1k Mercury bump maps
Summary(pl):	Mapa wybojów Merkurego o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-mercury-bumpmap
Obsoletes:	%{name}-textures-mercury-bumpmap

%description textures-mercury-bumpmap-default
1k Mercury bump map.

%description textures-mercury-bumpmap-default -l pl
Mapa wybojów Merkurego o wielko¶ci 1024 x 512.

%package textures-venus-default
Summary:	1k Venus textures
Summary(pl):	Tekstury Wenus o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-venus
Obsoletes:	%{name}-textures-venus

%description textures-venus-default
1k Venus textures.

%description textures-venus-default -l pl
Tekstury Venus o wielko¶ci 1024 x 512.

%package textures-earth-default
Summary:	2k Earth textures
Summary(pl):	Tekstury Ziemi o wielko¶ci 2048 x 1024
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-earth
Obsoletes:	%{name}-textures-earth

%description textures-earth-default
2k Earth textures.

%description textures-earth-default -l pl
Tekstury Ziemi o wielko¶ci 2048 x 1024.

%package textures-earth-clouds-default
Summary:	1k Earth cloud textures
Summary(pl):	Tekstury ziemskich chmur o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-earth-clouds
Obsoletes:	%{name}-textures-earth-clouds

%description textures-earth-clouds-default
1k Earth clouds textures.

%description textures-earth-clouds-default -l pl
Tekstury ziemskich chmur o wielko¶ci 1024 x 512.

%package textures-earth-night-default
Summary:	1k Earth night textures
Summary(pl):	Tekstury nocnych ¶wiate³ miast o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-earth-night
Obsoletes:	%{name}-textures-earth-night

%description textures-earth-night-default
1k Earth night textures.

%description textures-earth-night-default -l pl
Tekstury nocnych ¶wiate³ miast o wielko¶ci 1024 x 512.

%package textures-moon-default
Summary:	1k Moon textures
Summary(pl):	Tekstury Ksiê¿yca o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-moon
Obsoletes:	%{name}-textures-moon

%description textures-moon-default
1k Moon textures.

%description textures-moon-default -l pl
Tekstury Ksiê¿yca o wielko¶ci 1024 x 512.

%package textures-moon-bumpmap-default
Summary:	1k Moon bump map
Summary(pl):	Mapa wybojów Ksiê¿yca o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-moon-bumpmap
Obsoletes:	%{name}-textures-moon-bumpmap

%description textures-moon-bumpmap-default
1k Moon bump map.

%description textures-moon-bumpmap-default -l pl
Mapa wybojów Ksiê¿yca o wielko¶ci 1024 x 512.

%package textures-mars-default
Summary:	1k Mars textures
Summary(pl):	Tekstury Marsa o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-mars
Obsoletes:	%{name}-textures-mars

%description textures-mars-default
1k Mars textures.

%description textures-mars-default -l pl
Tekstury Marsa o wielko¶ci 1024 x 512.

%package textures-mars-bumpmap-default
Summary:	1k Mars bump map
Summary(pl):	Mapa wybojów Marsa o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-mars-bumpmap
Obsoletes:	%{name}-textures-mars-bumpmap

%description textures-mars-bumpmap-default
1k Mars bump map.

%description textures-mars-bumpmap-default -l pl
Mapa wybojów Marsa o wielko¶ci 1024 x 512.

%package textures-jupiter-default
Summary:	1k Jupiter textures
Summary(pl):	Tekstury Jowisza o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-jupiter
Obsoletes:	%{name}-textures-jupiter

%description textures-jupiter-default
1k Jupiter textures.

%description textures-jupiter-default -l pl
Tekstury Jowisza o wielko¶ci 1024 x 512.

%package textures-galileanmoons-default
Summary:	1k galilean moons textures
Summary(pl):	Tekstury ksiê¿yców odkrytych przez Galileusza o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-galileanmoons
Obsoletes:	%{name}-textures-galileanmoons

%description textures-galileanmoons-default
1k galilean moons (Io, Europa, Ganymede, Calypso) textures.

%description textures-galileanmoons-default -l pl
Tekstury ksiê¿yców Jowisza odkrytych przez Galileusza (Io,
Europa, Ganimedes, Calypso) o wielko¶ci 1024 x 512.

%package textures-saturn-default
Summary:	256 Saturn textures
Summary(pl):	Tekstury Saturna o wielko¶ci 256 x 128
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-saturn
Obsoletes:	%{name}-textures-saturn

%description textures-saturn-default
256 Saturn textures.

%description textures-saturn-default -l pl
Tekstury Jowisza o wielko¶ci 256 x 128.

%package textures-triton-default
Summary:	512 Triton textures
Summary(pl):	Tekstury Trytona o wielko¶ci 512 x 256
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-triton
Obsoletes:	%{name}-textures-triton

%description textures-triton-default
512 Triton textures.

%description textures-triton-default -l pl
Tekstury najwiêkszego ksiê¿yca Neptuna, Trytona
o wielko¶ci 512 x 256.

%package textures-pluto-default
Summary:	1k Pluto textures
Summary(pl):	Tekstury Plutona o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}-generator
Requires:	%{name}
Provides:	%{name}-textures-pluto
Obsoletes:	%{name}-textures-pluto

%description textures-pluto-default
1k Pluto textures.

%description textures-pluto-default -l pl
Tekstury Plutona o wielko¶ci 1024 x 512.

%prep
%setup -q -a2

echo "You can remove this package safely." > PLACEHOLDER-TASK-DEFAULT

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
	--disable-rpath \
	--with-kde \
	--without-gtk \
	--without-lua \
	--with-xinerama
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Scientific/Astronomy}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# desktop/icon
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Astronomy/%{name}.desktop
cp src/celestia/kde/data/hi48-app-celestia.png $RPM_BUILD_ROOT%{_pixmapsdir}/celestia.png

# solarsys.ssc generator
install -d $RPM_BUILD_ROOT%{_datadir}/apps/%{name}/data/solarsys
install solar/* $RPM_BUILD_ROOT%{_datadir}/apps/%{name}/data/solarsys
cat > $RPM_BUILD_ROOT%{_datadir}/apps/%{name}/solarsys-gen << EOF
#!/bin/sh
cd %{_datadir}/apps/%{name}/data
LANG=C cat solarsys/* > solarsys.ssc
EOF

%clean
rm -rf $RPM_BUILD_ROOT

# all texture-* here are required in one or another version, so no %%postun
%post	-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-mercury-default	-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-venus-default		-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-earth-default		-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-earth-clouds-default	-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-moon-default		-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-mars-default		-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-jupiter-default	-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-galileanmoons-default	-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-saturn-default		-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-triton-default		-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-pluto-default		-p %{_datadir}/apps/%{name}/solarsys-gen

# optional, so %%postun is also required
%post	textures-mercury-bumpmap-default	-p %{_datadir}/apps/%{name}/solarsys-gen
%postun	textures-mercury-bumpmap-default	-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-earth-night-default	-p %{_datadir}/apps/%{name}/solarsys-gen
%postun	textures-earth-night-default	-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-mars-bumpmap-default	-p %{_datadir}/apps/%{name}/solarsys-gen
%postun	textures-mars-bumpmap-default	-p %{_datadir}/apps/%{name}/solarsys-gen
%post	textures-moon-bumpmap-default	-p %{_datadir}/apps/%{name}/solarsys-gen
%postun	textures-moon-bumpmap-default	-p %{_datadir}/apps/%{name}/solarsys-gen

%files
%defattr(644,root,root,755)
%doc README AUTHORS TODO controls.txt ChangeLog
%doc %{_datadir}/apps/celestia/manual
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/celestia/data/solarsys/37-earth-satellites
%{_datadir}/apps/celestia/data/solarsys/48-mars-moons
%{_datadir}/apps/celestia/data/solarsys/52-jupiter-small-moon
%{_datadir}/apps/celestia/data/solarsys/65-saturn-moons
%{_datadir}/apps/celestia/data/solarsys/70-uranus
%{_datadir}/apps/celestia/data/solarsys/75-uranus-moons
%{_datadir}/apps/celestia/data/solarsys/80-neptune
%{_datadir}/apps/celestia/data/solarsys/84-neptune-moons
%{_datadir}/apps/celestia/data/solarsys/92-pluto-moon
%{_datadir}/apps/celestia/data/solarsys/99-various
%{_datadir}/apps/celestia/data/asterisms.dat
%{_datadir}/apps/celestia/data/boundaries.dat
%{_datadir}/apps/celestia/data/deepsky.dsc
%{_datadir}/apps/celestia/data/galileo.xyz
%verify(not md5 size mtime) %{_datadir}/apps/celestia/data/solarsys.ssc
%{_datadir}/apps/celestia/data/hdnames.dat
%{_datadir}/apps/celestia/data/starnames.dat
%{_datadir}/apps/celestia/extras
%{_datadir}/apps/celestia/favicons
%{_datadir}/apps/celestia/fonts
%{_datadir}/apps/celestia/models
%{_datadir}/apps/celestia/shaders
%dir %{_datadir}/apps/celestia/textures
%{_datadir}/apps/celestia/textures/lores
%{_datadir}/apps/celestia/textures/medres
%exclude %{_datadir}/apps/celestia/textures/medres/callisto.jpg
%exclude %{_datadir}/apps/celestia/textures/medres/earth*
%exclude %{_datadir}/apps/celestia/textures/medres/europa.jpg
%exclude %{_datadir}/apps/celestia/textures/medres/ganymede.jpg
%exclude %{_datadir}/apps/celestia/textures/medres/io.jpg
%exclude %{_datadir}/apps/celestia/textures/medres/jupiter.jpg
%exclude %{_datadir}/apps/celestia/textures/medres/mars*
%exclude %{_datadir}/apps/celestia/textures/medres/mercury*
%exclude %{_datadir}/apps/celestia/textures/medres/moon*
%exclude %{_datadir}/apps/celestia/textures/medres/pluto*
%exclude %{_datadir}/apps/celestia/textures/medres/saturn*
%exclude %{_datadir}/apps/celestia/textures/medres/triton*
%exclude %{_datadir}/apps/celestia/textures/medres/venus.jpg
%exclude %{_datadir}/apps/celestia/textures/medres/venussurface.jpg
%{_datadir}/apps/celestia/textures/flare.jpg
%{_datadir}/apps/celestia/textures/logo.png
%{_datadir}/apps/celestia/bookmarks.xml
%{_datadir}/apps/celestia/celestia.cfg
%{_datadir}/apps/celestia/celestiaui.rc
%{_datadir}/apps/celestia/controls.txt
%{_datadir}/apps/celestia/*.cel

%{_applnkdir}/Scientific/Astronomy/*
%{_pixmapsdir}/*
%{_datadir}/config
%{_datadir}/doc/HTML/en/%{name}
%{_datadir}/mimelnk/application/*
%{_datadir}/services/*

%files task-default
%defattr(644,root,root,755)
%doc PLACEHOLDER-TASK-DEFAULT

%files generator
%defattr(644,root,root,755)
%dir %{_datadir}/apps/celestia
%dir %{_datadir}/apps/celestia/data
%dir %{_datadir}/apps/celestia/data/solarsys
%attr(755,root,root) %{_datadir}/apps/celestia/solarsys-gen

%files extrasolar-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/data/extrasolar.ssc

%files stars-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/data/stars.dat

%files textures-mercury-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/mercury.jpg
%{_datadir}/apps/celestia/data/solarsys/00-mercury
%{_datadir}/apps/celestia/data/solarsys/07-mercury

%files textures-mercury-bumpmap-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/mercurybump.jpg
%{_datadir}/apps/celestia/data/solarsys/05-mercury-bump

%files textures-venus-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/venus.jpg
%{_datadir}/apps/celestia/textures/medres/venussurface.jpg
%{_datadir}/apps/celestia/data/solarsys/10-venus

%files textures-earth-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/earth.png
%{_datadir}/apps/celestia/data/solarsys/20-earth
%{_datadir}/apps/celestia/data/solarsys/24-earth
%{_datadir}/apps/celestia/data/solarsys/28-earth

%files textures-earth-clouds-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/earth-clouds.png
%{_datadir}/apps/celestia/data/solarsys/26-earth-clouds

%files textures-earth-night-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/earthnight.jpg
%{_datadir}/apps/celestia/data/solarsys/22-earth-night

%files textures-moon-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/moon.jpg
%{_datadir}/apps/celestia/data/solarsys/30-moon
%{_datadir}/apps/celestia/data/solarsys/35-moon

%files textures-moon-bumpmap-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/moonbump1k.jpg
%{_datadir}/apps/celestia/data/solarsys/33-moon-bump

%files textures-mars-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/mars.jpg
%{_datadir}/apps/celestia/data/solarsys/40-mars
%{_datadir}/apps/celestia/data/solarsys/44-mars
%{_datadir}/apps/celestia/data/solarsys/46-mars

%files textures-mars-bumpmap-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/marsbump1k.jpg
%{_datadir}/apps/celestia/data/solarsys/42-mars-bump

%files textures-jupiter-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/jupiter.jpg
%{_datadir}/apps/celestia/data/solarsys/50-jupiter

%files textures-galileanmoons-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/callisto.jpg
%{_datadir}/apps/celestia/textures/medres/io.jpg
%{_datadir}/apps/celestia/textures/medres/europa.jpg
%{_datadir}/apps/celestia/textures/medres/ganymede.jpg
%{_datadir}/apps/celestia/data/solarsys/55-jupiter-galilean-moons

%files textures-saturn-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/saturn.jpg
%{_datadir}/apps/celestia/data/solarsys/60-saturn

%files textures-triton-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/triton.jpg
%{_datadir}/apps/celestia/data/solarsys/82-neptune-triton

%files textures-pluto-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/pluto.jpg
%{_datadir}/apps/celestia/textures/medres/plutobump1k.jpg
%{_datadir}/apps/celestia/data/solarsys/90-pluto
