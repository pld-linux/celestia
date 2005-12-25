Summary:	A real-time visual space simulation
Summary(pl):	Symulacja przestrzeni kosmicznej w czasie rzeczywistym
Name:		celestia
Version:	1.4.0
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/celestia/%{name}-%{version}.tar.gz
# Source0-md5:	d4bd0029af87fdd9cb4a0828cf62a025
Source1:	%{name}.desktop
Patch0:		%{name}-lua50.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-gcc4.patch
Patch3:		%{name}-extras.patch
URL:		http://www.shatters.net/celestia/
BuildRequires:	GConf2-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	glut-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	lua50-devel
BuildRequires:	pkgconfig
Requires:	OpenGL
Obsoletes:	celestia-textures-stars
Obsoletes:	celestia-asterisms
Obsoletes:	celestia-galaxies
Obsoletes:	celestia-textures-venus-default
Obsoletes:	celestia-textures-jupiter-default
Obsoletes:	celestia-textures-saturn-default
Obsoletes:	celestia-textures-triton-default
Obsoletes:	celestia-textures-pluto-default
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
touch config.h.in
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

CPPFLAGS="-I/usr/X11R6/include -I/usr/include/lua50"
CXXFLAGS="%{rpmcflags} -fno-exceptions"

%configure \
	--disable-rpath \
	--with-kde \
	--without-gtk \
	--with-lua \
	--with-xinerama \
	--with-qt-dir=%{_libdir}

%{__make} ACLOCAL="%{__aclocal} -I macros"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# desktop/icon
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install src/celestia/gtk/data/celestia.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS TODO controls.txt ChangeLog manual/
%attr(755,root,root) %{_bindir}/*
%{_datadir}/celestia
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_datadir}/apps/celestia
%{_datadir}/config/*
%{_datadir}/mimelnk/application/*
%{_datadir}/services/*
%exclude %{_datadir}/celestia/manual
