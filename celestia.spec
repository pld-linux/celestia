Summary:	A real-time visual space simulation
Summary(pl):	Symulacja przestrzeni kosmicznej w czasie rzeczywistym
Name:		celestia
Version:	1.2.5
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/celestia/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	http://www.la-guarida.com/Celestia/Textures/JupiterRings.zip
Source3:	http://www.la-guarida.com/Celestia/Textures/NeptuneRings.zip
Patch0:		%{name}-moon_eclipse.patch
Patch1:		%{name}-planet_rings.patch
Patch2:		%{name}-bumpmaps.patch
URL:		http://www.shatters.net/celestia/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glut-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtkglarea-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
Requires:	OpenGL
Requires:	%{name}-extrasolar
Requires:	%{name}-galaxies
Requires:	%{name}-stars
Requires:	%{name}-textures-stars
Requires:	%{name}-textures-mercury
Requires:	%{name}-textures-earth
Requires:	%{name}-textures-earth-clouds
Requires:	%{name}-textures-earth-night
Requires:	%{name}-textures-moon
Requires:	%{name}-textures-mars
Requires:	%{name}-textures-jupiter
Requires:	%{name}-textures-galileanmoons
Requires:	%{name}-textures-saturn
Requires:	%{name}-textures-triton
Requires:	%{name}-textures-pluto
Obsoletes:	%{name}-asterisms
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
Requires:	%{name}-galaxies-default
Requires:	%{name}-stars-default
Requires:	%{name}-textures-stars-default
Requires:	%{name}-textures-mercury-default
Requires:	%{name}-textures-earth-default
Requires:	%{name}-textures-earth-clouds-default
Requires:	%{name}-textures-earth-night-default
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

%package galaxies-default
Summary:	Galaxy catalog (8 galaxies)
Summary(pl):	Katalog o¶miu galaktyk
Group:		X11/Applications/Science
Requires:	%{name}
Provides:	%{name}-galaxies
Obsoletes:	%{name}-galaxies

%description galaxies-default
Galaxy catalog (8 galaxies).

%description galaxies-default -l pl
Katalog o¶miu galaktyk.

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

%package textures-stars-default
Summary:	Standard stars textures
Summary(pl):	Standardowe tekstury gwiazd
Group:		X11/Applications/Science
Requires:	%{name}
Provides:	%{name}-textures-stars
Obsoletes:	%{name}-textures-stars

%description textures-stars-default
Standard stars textures.

%description textures-stars-default -l pl
Standardowe tekstury gwiazd.

%package textures-mercury-default
Summary:	1k Mercury textures
Summary(pl):	Tekstury Merkurego o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}
Provides:	%{name}-textures-mercury
Obsoletes:	%{name}-textures-mercury

%description textures-mercury-default
1k Mercury textures.

%description textures-mercury-default -l pl
Tekstury Merkurego o wielko¶ci 1024 x 512.

%package textures-earth-default
Summary:	2k Earth textures
Summary(pl):	Tekstury Ziemi o wielko¶ci 2048 x 1024
Group:		X11/Applications/Science
Prereq:		%{name}
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
Prereq:		%{name}
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
Prereq:		%{name}
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
Prereq:		%{name}
Provides:	%{name}-textures-moon
Obsoletes:	%{name}-textures-moon

%description textures-moon-default
1k Moon textures.

%description textures-moon-default -l pl
Tekstury Ksiê¿yca o wielko¶ci 1024 x 512.

%package textures-mars-default
Summary:	1k Mars textures
Summary(pl):	Tekstury Marsa o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}
Provides:	%{name}-textures-mars
Obsoletes:	%{name}-textures-mars

%description textures-mars-default
1k Mars textures.

%description textures-mars-default -l pl
Tekstury Marsa o wielko¶ci 1024 x 512.

%package textures-jupiter-default
Summary:	1k Jupiter textures
Summary(pl):	Tekstury Jowisza o wielko¶ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}
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
Prereq:		%{name}
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
Prereq:		%{name}
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
Prereq:		%{name}
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
Prereq:		%{name}
Provides:	%{name}-textures-pluto
Obsoletes:	%{name}-textures-pluto

%description textures-pluto-default
1k Pluto textures.

%description textures-pluto-default -l pl
Tekstury Plutona o wielko¶ci 1024 x 512.

%prep
%setup -q -a2 -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1

touch PLACEHOLDER-TASK-DEFAULT

%build
#rm -f missing
#%%{__aclocal} -I macros
#%%{__autoconf}
#automake -a -f
CFLAGS="-I%{_includedir} %{rpmcflags}"
CPPFLAGS="-I%{_includedir} %{rpmcflags}"
CXXFLAGS="-I%{_includedir} %{rpmcflags} -fno-rtti -fno-exceptions"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -e DESTDIR=$RPM_BUILD_ROOT install
install -d $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Astronomy
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Astronomy/%{name}.desktop
install {jupiter,neptune}-rings.png $RPM_BUILD_ROOT%{_datadir}/celestia/textures/medres/

cd $RPM_BUILD_ROOT%{_datadir}/celestia/textures/medres
mv moonbump1k.jpg moonbump.jpg
mv marsbump1k.jpg marsbump.jpg
mv plutobump1k.jpg plutobump.jpg

%clean
rm -rf $RPM_BUILD_ROOT

%post textures-mercury-default
umask 022
cd %{_datadir}/celestia/data
sed "s/\"mercury....\"/\"mercury.jpg\"/g;s/\"mercurybump....\"/\"mercurybump.jpg\"/g" solarsys.ssc > .solar
mv -f .solar solarsys.ssc

%post textures-earth-default
umask 022
cd %{_datadir}/celestia/data
sed "s/\"earth....\"/\"earth.png\"/g" solarsys.ssc > .solar
mv -f .solar solarsys.ssc

%post textures-earth-clouds-default
umask 022
cd %{_datadir}/celestia/data
sed "s/\"earth-clouds....\"/\"earth-clouds.png\"/g" solarsys.ssc > .solar
mv -f .solar solarsys.ssc

%post textures-earth-night-default
umask 022
cd %{_datadir}/celestia/data
sed "s/\"earthnight....\"/\"earth-night.png\"/g" solarsys.ssc > .solar
mv -f .solar solarsys.ssc

%post textures-moon-default
umask 022
cd %{_datadir}/celestia/data
sed "s/\"moon....\"/\"moon.jpg\"/g;s/\"moonbump....\"/\"moonbump.jpg\"/g" solarsys.ssc > .solar
mv -f .solar solarsys.ssc

%post textures-mars-default
umask 022
cd %{_datadir}/celestia/data
sed "s/\"mars....\"/\"mars.jpg\"/g;s/\"marsbump....\"/\"marsbump.jpg\"/g" solarsys.ssc > .solar
mv -f .solar solarsys.ssc

%post textures-jupiter-default
umask 022
cd %{_datadir}/celestia/data
sed "s/\"jupiter....\"/\"jupiter.jpg\"/g" solarsys.ssc > .solar
mv -f .solar solarsys.ssc

%post textures-galileanmoons-default
umask 022
cd %{_datadir}/celestia/data
sed "s/\"callisto....\"/\"callisto.jpg\"/g" solarsys.ssc > .solar
sed "s/\"io....\"/\"io.jpg\"/g" .solar > solarsys.ssc
sed "s/\"europa....\"/\"europa.jpg\"/g" solarsys.ssc > .solar
sed "s/\"ganymede....\"/\"ganymede.jpg\"/g" .solar > solarsys.ssc
rm -f .solar

%post textures-saturn-default
umask 022
cd %{_datadir}/celestia/data
sed "s/\"saturn....\"/\"saturn.jpg\"/g" solarsys.ssc > .solar
mv -f .solar solarsys.ssc

%post textures-triton-default
umask 022
cd %{_datadir}/celestia/data
sed "s/\"triton....\"/\"triton.jpg\"/g" solarsys.ssc > .solar
mv -f .solar solarsys.ssc

%post textures-pluto-default
umask 022
cd %{_datadir}/celestia/data
sed "s/\"pluto....\"/\"pluto.jpg\"/g;s/\"plutobump....\"/\"plutobump.jpg\"/g" solarsys.ssc > .solar
mv -f .solar solarsys.ssc

%files
%defattr(644,root,root,755)
%doc README AUTHORS TODO controls.txt
%doc %{_datadir}/celestia/manual
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/celestia
%dir %{_datadir}/celestia/data
%{_datadir}/celestia/data/asterisms.dat
%{_datadir}/celestia/data/boundaries.dat
%{_datadir}/celestia/data/galileo.xyz
# problem: after upgrade it will be lost
%verify(not md5 size mtime) %{_datadir}/celestia/data/solarsys.ssc
%{_datadir}/celestia/data/hdnames.dat
%{_datadir}/celestia/data/starnames.dat
%{_datadir}/celestia/extras
%{_datadir}/celestia/fonts
%{_datadir}/celestia/models
%{_datadir}/celestia/shaders
%dir %{_datadir}/celestia/textures
%{_datadir}/celestia/textures/lores
%dir %{_datadir}/celestia/textures/medres
%{_datadir}/celestia/textures/medres/iss*
%{_datadir}/celestia/textures/medres/ariel.jpg
%{_datadir}/celestia/textures/medres/asteroid.jpg
%{_datadir}/celestia/textures/medres/deimos.jpg
%{_datadir}/celestia/textures/medres/dione.jpg
%{_datadir}/celestia/textures/medres/gasgiant.jpg
%{_datadir}/celestia/textures/medres/iapetus.jpg
%{_datadir}/celestia/textures/medres/jupiter-rings.png
%{_datadir}/celestia/textures/medres/jupiterlike.jpg
%{_datadir}/celestia/textures/medres/mimas.jpg
%{_datadir}/celestia/textures/medres/miranda.jpg
%{_datadir}/celestia/textures/medres/neptune-rings.png
%{_datadir}/celestia/textures/medres/oberon.jpg
%{_datadir}/celestia/textures/medres/phobos.jpg
%{_datadir}/celestia/textures/medres/renova.jpg
%{_datadir}/celestia/textures/medres/rhea.jpg
%{_datadir}/celestia/textures/medres/tethys.jpg
%{_datadir}/celestia/textures/medres/titania.jpg
%{_datadir}/celestia/textures/medres/umbriel.jpg
%{_datadir}/celestia/textures/medres/venus.jpg
%{_datadir}/celestia/textures/medres/venuslike.jpg
%{_datadir}/celestia/textures/flare.jpg
%{_datadir}/celestia/textures/logo.png
%{_datadir}/celestia/celestia.cfg
%{_datadir}/celestia/controls.txt
%{_datadir}/celestia/*.cel
%{_applnkdir}/Scientific/Astronomy/*

%files task-default
%defattr(644,root,root,755)
%doc PLACEHOLDER-TASK-DEFAULT


%files extrasolar-default
%defattr(644,root,root,755)
%{_datadir}/celestia/data/extrasolar.ssc

%files galaxies-default
%defattr(644,root,root,755)
%{_datadir}/celestia/data/galaxies.dat

%files stars-default
%defattr(644,root,root,755)
%{_datadir}/celestia/data/stars.dat

%files textures-stars-default
%defattr(644,root,root,755)
%{_datadir}/celestia/textures/medres/astar.jpg
%{_datadir}/celestia/textures/medres/bstar.jpg
%{_datadir}/celestia/textures/medres/gstar.jpg
%{_datadir}/celestia/textures/medres/mstar.jpg
%{_datadir}/celestia/textures/medres/browndwarf.jpg

%files textures-mercury-default
%defattr(644,root,root,755)
%{_datadir}/celestia/textures/medres/mercury.jpg
%{_datadir}/celestia/textures/medres/mercurybump.jpg

%files textures-earth-default
%defattr(644,root,root,755)
%{_datadir}/celestia/textures/medres/earth.png

%files textures-earth-clouds-default
%defattr(644,root,root,755)
%{_datadir}/celestia/textures/medres/earth-clouds.png

%files textures-earth-night-default
%defattr(644,root,root,755)
%{_datadir}/celestia/textures/medres/earthnight.jpg

%files textures-moon-default
%defattr(644,root,root,755)
%{_datadir}/celestia/textures/medres/moon.jpg
%{_datadir}/celestia/textures/medres/moonbump.jpg

%files textures-mars-default
%defattr(644,root,root,755)
%{_datadir}/celestia/textures/medres/mars.jpg
%{_datadir}/celestia/textures/medres/marsbump.jpg

%files textures-jupiter-default
%defattr(644,root,root,755)
%{_datadir}/celestia/textures/medres/jupiter.jpg

%files textures-galileanmoons-default
%defattr(644,root,root,755)
%{_datadir}/celestia/textures/medres/callisto.jpg
%{_datadir}/celestia/textures/medres/io.jpg
%{_datadir}/celestia/textures/medres/europa.jpg
%{_datadir}/celestia/textures/medres/ganymede.jpg

%files textures-saturn-default
%defattr(644,root,root,755)
%{_datadir}/celestia/textures/medres/saturn.jpg

%files textures-triton-default
%defattr(644,root,root,755)
%{_datadir}/celestia/textures/medres/triton.jpg

%files textures-pluto-default
%defattr(644,root,root,755)
%{_datadir}/celestia/textures/medres/pluto.jpg
%{_datadir}/celestia/textures/medres/plutobump.jpg
