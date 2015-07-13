#
# Conditional build:
%bcond_with	kde		# KDE3 UI as the default one
%bcond_without	gtk		# use GTK+2 UI instead
%bcond_with	gnome		# use libgnome2 UI instead
%bcond_with	glut		# use glut UI instead
%bcond_without	theora		# without theora support

%if %{with kde} || %{with gnome} || %{with glut}
%undefine	with_gtk
%endif
Summary:	A real-time visual space simulation
Summary(pl.UTF-8):	Symulacja przestrzeni kosmicznej w czasie rzeczywistym
Name:		celestia
Version:	1.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://downloads.sourceforge.net/celestia/%{name}-%{version}.tar.gz
# Source0-md5:	02208982a431b984502fac909bf380f4
Patch0:		%{name}-includes.patch
Patch1:		%{name}-as-needed.patch
Patch2:		gtk-enable-locales-early.patch
Patch3:		use-stdint_h.patch
Patch4:		%{name}-desktop.patch
Patch5:		%{name}-gcc47.patch
Patch6:		%{name}-null.patch
#Patch2:		%{name}-extras.patch
#Patch4:		%{name}-lua51.patch
URL:		http://www.shatters.net/celestia/
BuildRequires:	OpenGL-GLU-devel
%{?with_glut:BuildRequires:	OpenGL-glut-devel >= 4.0}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
%if %{with gtk} || %{with gnome}
BuildRequires:	cairo-devel
BuildRequires:	gtk+2-devel >= 2:2.6
BuildRequires:	gtkglext-devel
%endif
BuildRequires:	gettext-tools
%{?with_kde:BuildRequires:	kdelibs-devel}
%{?with_gnome:BuildRequires:	libgnomeui-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
%{?with_theora:BuildRequires:	libtheora-devel}
BuildRequires:	libtool
BuildRequires:	lua51-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
# celestia < 1.4 original packages
Obsoletes:	celestia-extrasolar
Obsoletes:	celestia-generator
Obsoletes:	celestia-stars
Obsoletes:	celestia-task-default
# texture replacement addons, virtual provides
Obsoletes:	celestia-textures-earth
Obsoletes:	celestia-textures-earth-clouds
Obsoletes:	celestia-textures-earth-night
Obsoletes:	celestia-textures-galileanmoons
Obsoletes:	celestia-textures-mars
Obsoletes:	celestia-textures-mars-bumpmap
Obsoletes:	celestia-textures-mercury
Obsoletes:	celestia-textures-mercury-bumpmap
Obsoletes:	celestia-textures-moon
Obsoletes:	celestia-textures-moon-bumpmap
# celestia addons
Obsoletes:	celestia-blackhole
Obsoletes:	celestia-galaxies_extended
Obsoletes:	celestia-galaxy_clusters
Obsoletes:	celestia-globular_clusters
Obsoletes:	celestia-im-starwars
Obsoletes:	celestia-pathfinder
Obsoletes:	celestia-voyager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Celestia to wolny symulator przestrzeni komicznej w czasie
rzeczywistym, który pozwala doświadczać naszego Wszechświata w trzech
wymiarach. W odróżnieniu od innych programów planetarnych Celestia nie
przywiązuje Cię do powierzchni ziemi. Możesz podróżować przez Układ
Słoneczny do ponad 100,000 gwiazd lub nawet poza galaktykę. Wszystkie
podróże w Celestii są niezauważalne; funkcja wykładniczego
przybliżenia pozwala Ci odkrywać Kosmos w różnych skalach - od
spojrzenia na galaktyki do widoku kilkumetrowych statków kosmicznych.
Interfejs typu 'pokaż-i-leć' czyni nawigację przez Wszechświat prostą.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

# ugly hack not to require GConf2-devel if we're not building gnome version
%{!?with_gnome:sed -i "s#AM_GCONF_SOURCE_2##g" configure.in}

%build
%{__gettextize}
cp -a po/Makefile* po2/
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	CFLAGS="%{rpmcflags} $(pkg-config --cflags libpng)" \
	LIBS="-ldl" \
	%{?with_kde:--with-kde} \
	%{?with_gtk:--with-gtk} \
	%{?with_gnome:--with-gnome} \
	%{?with_glut:--with-glut} \
	--disable-rpath \
	%{!?with_theora:--disable-theora} \
	--with-lua \
	--with-qt-dir=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	appsdir=%{_desktopdir}/kde

# desktop/icon
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
%{!?with_kde:install src/celestia/kde/data/celestia.desktop $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop}
cp -p src/celestia/kde/data/hi48-app-celestia.png $RPM_BUILD_ROOT%{_pixmapsdir}/celestia.png

rm -r $RPM_BUILD_ROOT%{_localedir}/no

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with gnome}
%post
%gconf_schema_install celestia.schemas

%preun
%gconf_schema_uninstall celestia.schemas
%endif

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README AUTHORS controls.txt ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/celestia
%{_pixmapsdir}/*
%if %{with kde}
%{_datadir}/apps/celestia
%{_datadir}/config/*
%{_datadir}/mimelnk/application/*
%{_datadir}/services/*
%{_iconsdir}/*/*/apps/%{name}.png
%{_desktopdir}/kde/*.desktop
%else
%{_desktopdir}/*.desktop
%endif
%{?with_gnome:%{_sysconfdir}/gconf/schemas/celestia.schemas}
